"""pgvector store for the bone atlas.

Uses OnyxPlex pgvector (onyx_vectors database)
with 1024D embeddings (bge-m3 via embedding-proxy) and JSONB payloads
for similarity search, conformation analysis, and population statistics.
"""

import logging
from typing import Any

import psycopg

logger = logging.getLogger(__name__)

BONE_TYPES = ["femur", "humerus", "radius", "ulna", "scapula", "fibula"]


class BoneAtlasStore:
    """Manages the bone_atlas collection in pgvector."""

    def __init__(
        self,
        host: str = "10.0.0.8",
        port: int = 5432,
        database: str = "onyx_vectors",
        user: str = "onyx",
        password: str = "",
        collection: str = "bone_atlas",
        vector_size: int = 1024,
    ) -> None:
        """Initialize bone atlas pgvector store.

        Args:
            host: PostgreSQL host.
            port: PostgreSQL port.
            database: Database name (onyx_vectors).
            user: Database user.
            password: Database password.
            collection: Collection name in embeddings table.
            vector_size: Embedding vector dimension (1024 for bge-m3).
        """
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.collection = collection
        self.vector_size = vector_size
        self._conn: psycopg.Connection | None = None
        logger.info(
            "BoneAtlasStore initialized for %s:%d/%s (collection=%s, dim=%d)",
            host,
            port,
            database,
            collection,
            vector_size,
        )

    def _get_conn(self) -> psycopg.Connection:
        """Get or create psycopg connection."""
        if self._conn is None or self._conn.closed:
            conninfo = f"host={self.host} port={self.port} user={self.user} dbname={self.database}"
            if self.password:
                conninfo += f" password={self.password}"
            self._conn = psycopg.connect(conninfo, autocommit=True)
        return self._conn

    @staticmethod
    def _normalize_point_id(point_id: str | int) -> str:
        """Normalize point ID to a string suitable for pgvector point_id."""
        if isinstance(point_id, int):
            return str(point_id)
        return str(point_id)

    def ensure_collection(self) -> None:
        """Verify pgvector table exists (created by OnyxPlex, idempotent check)."""
        try:
            conn = self._get_conn()
            row = conn.execute(
                "SELECT count(*) FROM embeddings WHERE collection = %s",
                (self.collection,),
            ).fetchone()
            count = row[0] if row else 0
            logger.info("Collection '%s' ready (%d points)", self.collection, count)
        except Exception as e:
            logger.warning("pgvector collection check failed: %s", e)

    def upsert_bone(
        self,
        point_id: str | int,
        embedding: list[float],
        payload: dict[str, Any],
    ) -> None:
        """Insert or update a bone entry in the atlas.

        Args:
            point_id: Point ID.
            embedding: 1024D vector.
            payload: Rich metadata (JSONB).
        """
        try:
            conn = self._get_conn()
            pid = self._normalize_point_id(point_id)
            conn.execute(
                """INSERT INTO embeddings (collection, point_id, vector, payload)
                   VALUES (%s, %s, %s::vector, %s::jsonb)
                   ON CONFLICT (collection, point_id)
                   DO UPDATE SET vector = EXCLUDED.vector, payload = EXCLUDED.payload""",
                (self.collection, pid, embedding, psycopg.types.json.Json(payload)),
            )
        except Exception as e:
            logger.error("pgvector upsert failed for %s: %s", point_id, e)

    def upsert_batch(self, points: list[dict[str, Any]]) -> None:
        """Batch insert/update. Each dict needs 'id', 'embedding', 'payload'.

        Args:
            points: List of point dicts.
        """
        try:
            conn = self._get_conn()
            for p in points:
                pid = self._normalize_point_id(p["id"])
                conn.execute(
                    """INSERT INTO embeddings (collection, point_id, vector, payload)
                       VALUES (%s, %s, %s::vector, %s::jsonb)
                       ON CONFLICT (collection, point_id)
                       DO UPDATE SET vector = EXCLUDED.vector, payload = EXCLUDED.payload""",
                    (self.collection, pid, p["embedding"], psycopg.types.json.Json(p["payload"])),
                )
            logger.info("Upserted %d points to '%s'", len(points), self.collection)
        except Exception as e:
            logger.error("pgvector batch upsert failed: %s", e)

    def search_similar(
        self,
        embedding: list[float],
        bone_type: str | None = None,
        side: str | None = None,
        region: str | None = None,
        limit: int = 10,
        score_threshold: float = 0.0,
    ) -> list[dict[str, Any]]:
        """Search for similar bones by embedding (cosine similarity).

        Args:
            embedding: 1024D query vector.
            bone_type: Optional filter by bone type.
            side: Optional filter by side.
            region: Optional filter by region.
            limit: Max results.
            score_threshold: Minimum cosine similarity (0-1).

        Returns:
            List of search results with id, score, payload.
        """
        try:
            conn = self._get_conn()
            conditions = ["collection = %s"]
            params: list[Any] = [self.collection]

            if bone_type:
                conditions.append("payload->>'bone_type' = %s")
                params.append(bone_type)
            if side:
                conditions.append("payload->>'side' = %s")
                params.append(side)
            if region:
                conditions.append("payload->>'region' = %s")
                params.append(region)

            where = " AND ".join(conditions)
            # cosine distance: <=> returns distance (0=identical, 2=opposite)
            # similarity = 1 - distance
            query = f"""SELECT point_id, 1 - (vector <=> %s::vector) as score, payload
                        FROM embeddings WHERE {where}
                        ORDER BY vector <=> %s::vector LIMIT %s"""
            query_params = (*params, embedding, embedding, limit)

            rows = conn.execute(query, query_params).fetchall()

            results = []
            for row in rows:
                sim = float(row[1])
                if sim >= score_threshold:
                    results.append(
                        {
                            "id": str(row[0]),
                            "score": sim,
                            "payload": row[2],
                        }
                    )
            return results
        except Exception as e:
            logger.error("pgvector search failed: %s", e)
            return []

    def find_atypical(
        self,
        bone_type: str,
        mahalanobis_threshold: float = 2.0,
        limit: int = 50,
    ) -> list[dict[str, Any]]:
        """Find bones with atypical conformation via payload filter.

        Args:
            bone_type: Type of bone.
            mahalanobis_threshold: Threshold for Mahalanobis distance.
            limit: Max results.

        Returns:
            List of atypical bones.
        """
        try:
            conn = self._get_conn()
            rows = conn.execute(
                """SELECT point_id, payload FROM embeddings
                   WHERE collection = %s
                     AND payload->>'bone_type' = %s
                     AND (payload->'conformation'->>'mahalanobis_distance')::float >= %s
                   LIMIT %s""",
                (self.collection, bone_type, mahalanobis_threshold, limit),
            ).fetchall()
            return [{"id": str(r[0]), "payload": r[1]} for r in rows]
        except Exception as e:
            logger.error("pgvector find_atypical failed: %s", e)
            return []

    def get_population_stats(self, bone_type: str | None = None) -> dict[str, int]:
        """Get statistics about the atlas population.

        Args:
            bone_type: Optional bone type filter.

        Returns:
            Dict with population statistics.
        """
        try:
            conn = self._get_conn()
            if bone_type:
                row = conn.execute(
                    "SELECT count(*) FROM embeddings WHERE collection = %s AND payload->>'bone_type' = %s",
                    (self.collection, bone_type),
                ).fetchone()
                return {"total": row[0] if row else 0}

            row = conn.execute(
                "SELECT count(*) FROM embeddings WHERE collection = %s",
                (self.collection,),
            ).fetchone()
            stats: dict[str, int] = {"total": row[0] if row else 0}

            for bt in BONE_TYPES:
                row = conn.execute(
                    "SELECT count(*) FROM embeddings WHERE collection = %s AND payload->>'bone_type' = %s",
                    (self.collection, bt),
                ).fetchone()
                stats[bt] = row[0] if row else 0
            return stats
        except Exception as e:
            logger.error("pgvector stats failed: %s", e)
            return {"total": 0}

    def delete_collection(self) -> None:
        """Delete all points in this collection."""
        try:
            conn = self._get_conn()
            conn.execute(
                "DELETE FROM embeddings WHERE collection = %s",
                (self.collection,),
            )
            logger.info("Deleted collection '%s'", self.collection)
        except Exception as e:
            logger.error("pgvector delete failed: %s", e)

    def build_payload(
        self,
        bone_type: str,
        side: str,
        region: str,
        confidence: dict[str, Any],
        source: dict[str, Any],
        angle: dict[str, Any],
        density: dict[str, Any] | None = None,
        landmarks: list | None = None,
        conformation: dict[str, Any] | None = None,
        measurements: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Build a complete payload for a bone atlas entry.

        Args:
            bone_type: Type of bone.
            side: Side (left/right/bilateral).
            region: Region (proximal/distal/entire).
            confidence: Confidence dict.
            source: Source metadata.
            angle: Angle information.
            density: Optional density analysis.
            landmarks: Optional landmarks.
            conformation: Optional conformation analysis.
            measurements: Optional measurements.

        Returns:
            Complete payload dict.
        """
        payload: dict[str, Any] = {
            "bone_type": bone_type,
            "side": side,
            "region": region,
            "confidence": confidence,
            "source": source,
            "angle": angle,
        }
        if density:
            payload["density"] = density
        if landmarks:
            payload["landmarks"] = landmarks
        if conformation:
            payload["conformation"] = conformation
        if measurements:
            payload["measurements"] = measurements
        return payload
