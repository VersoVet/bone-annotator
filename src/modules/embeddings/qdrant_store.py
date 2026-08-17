"""Qdrant vector store for the bone atlas.

Manages the `bone_atlas` collection with 512D embeddings and rich payloads
for similarity search, conformation analysis, and population statistics.
"""

import logging
import threading
import uuid
from typing import Any

logger = logging.getLogger(__name__)

# Bone types - import from config when available
BONE_TYPES = ["femur", "humerus", "radius", "ulna", "scapula", "fibula"]


class BoneAtlasStore:
    """Manages the bone_atlas Qdrant collection."""

    def __init__(
        self,
        host: str = "localhost",
        port: int = 6333,
        collection: str = "bone_atlas",
        vector_size: int = 512,
    ) -> None:
        """Initialize bone atlas store.

        Args:
            host: Qdrant server host.
            port: Qdrant server port.
            collection: Collection name.
            vector_size: Embedding vector size.
        """
        self.host = host
        self.port = port
        self.collection = collection
        self.vector_size = vector_size
        self.client = None
        self._lock = threading.Lock()
        logger.info(
            "BoneAtlasStore initialized for %s:%d/%s",
            host,
            port,
            collection,
        )

    def _get_client(self) -> Any:
        """Get or create Qdrant client (thread-safe lazy init)."""
        if self.client is None:
            with self._lock:
                if self.client is None:
                    from qdrant_client import QdrantClient

                    self.client = QdrantClient(host=self.host, port=self.port)
        return self.client

    @staticmethod
    def _normalize_point_id(point_id: str | int) -> str | int:
        """Normalize point ID for Qdrant (must be int or valid UUID string)."""
        if isinstance(point_id, int):
            return point_id
        try:
            uuid.UUID(point_id)
            return point_id
        except ValueError:
            return str(uuid.uuid5(uuid.NAMESPACE_DNS, point_id))

    def ensure_collection(self) -> None:
        """Create the collection if it doesn't exist (fully idempotent)."""
        try:
            from qdrant_client.http import models as qmodels
            from qdrant_client.http.exceptions import UnexpectedResponse

            client = self._get_client()

            # Check if collection exists (catch only "not found", not network errors)
            try:
                client.get_collection(self.collection)
                logger.info("Collection '%s' already exists", self.collection)
                return
            except UnexpectedResponse as e:
                if e.status_code != 404:
                    raise  # Re-raise network/auth errors

            client.create_collection(
                collection_name=self.collection,
                vectors_config=qmodels.VectorParams(
                    size=self.vector_size,
                    distance=qmodels.Distance.COSINE,
                ),
            )

            # Create payload indexes (each wrapped individually for idempotence)
            keyword_fields = ["bone_type", "side", "region", "source.specimen_id"]
            float_fields = ["conformation.mahalanobis_distance", "confidence.bone"]
            for field in keyword_fields:
                try:
                    client.create_payload_index(
                        collection_name=self.collection,
                        field_name=field,
                        field_schema=qmodels.PayloadSchemaType.KEYWORD,
                    )
                except Exception as idx_err:
                    logger.warning("Index '%s' creation skipped: %s", field, idx_err)
            for field in float_fields:
                try:
                    client.create_payload_index(
                        collection_name=self.collection,
                        field_name=field,
                        field_schema=qmodels.PayloadSchemaType.FLOAT,
                    )
                except Exception as idx_err:
                    logger.warning("Index '%s' creation skipped: %s", field, idx_err)

            logger.info("Created collection '%s' with indexes", self.collection)
        except ImportError:
            logger.warning("qdrant-client not available")

    def upsert_bone(
        self,
        point_id: str | int,
        embedding: list[float],
        payload: dict[str, Any],
    ) -> None:
        """Insert or update a bone entry in the atlas.

        Args:
            point_id: Point ID (int or UUID string).
            embedding: 512D vector.
            payload: Rich metadata.
        """
        try:
            from qdrant_client.http import models as qmodels

            client = self._get_client()
            point_id = self._normalize_point_id(point_id)
            client.upsert(
                collection_name=self.collection,
                points=[
                    qmodels.PointStruct(
                        id=point_id,
                        vector=embedding,
                        payload=payload,
                    ),
                ],
            )
        except ImportError:
            logger.warning("qdrant-client not available")
        except Exception as e:
            logger.error("Qdrant upsert failed for %s: %s", point_id, e)

    def upsert_batch(
        self,
        points: list[dict[str, Any]],
    ) -> None:
        """Batch insert/update. Each dict needs 'id', 'embedding', 'payload'.

        Args:
            points: List of point dicts.
        """
        try:
            from qdrant_client.http import models as qmodels

            client = self._get_client()
            qdrant_points = [
                qmodels.PointStruct(
                    id=self._normalize_point_id(p["id"]),
                    vector=p["embedding"],
                    payload=p["payload"],
                )
                for p in points
            ]
            chunk_size = 100
            for i in range(0, len(qdrant_points), chunk_size):
                chunk = qdrant_points[i : i + chunk_size]
                client.upsert(collection_name=self.collection, points=chunk)
            logger.info("Upserted %d points to '%s'", len(points), self.collection)
        except ImportError:
            logger.warning("qdrant-client not available")
        except Exception as e:
            logger.error("Qdrant batch upsert failed: %s", e)

    def search_similar(
        self,
        embedding: list[float],
        bone_type: str | None = None,
        side: str | None = None,
        region: str | None = None,
        limit: int = 10,
        score_threshold: float = 0.0,
    ) -> list[dict[str, Any]]:
        """Search for similar bones by embedding.

        Args:
            embedding: 512D query vector.
            bone_type: Optional filter by bone type.
            side: Optional filter by side.
            region: Optional filter by region.
            limit: Max results.
            score_threshold: Minimum cosine similarity.

        Returns:
            List of search results.
        """
        try:
            from qdrant_client.http import models as qmodels

            client = self._get_client()

            # Build filter conditions
            conditions: list = []
            if bone_type:
                conditions.append(
                    qmodels.FieldCondition(
                        key="bone_type",
                        match=qmodels.MatchValue(value=bone_type),
                    )
                )
            if side:
                conditions.append(
                    qmodels.FieldCondition(
                        key="side",
                        match=qmodels.MatchValue(value=side),
                    )
                )
            if region:
                conditions.append(
                    qmodels.FieldCondition(
                        key="region",
                        match=qmodels.MatchValue(value=region),
                    )
                )

            query_filter = None
            if conditions:
                query_filter = qmodels.Filter(must=conditions)

            results = client.query_points(
                collection_name=self.collection,
                query=embedding,
                query_filter=query_filter,
                limit=limit,
                score_threshold=score_threshold,
            )

            return [
                {
                    "id": str(r.id),
                    "score": r.score,
                    "payload": r.payload,
                }
                for r in results.points
            ]
        except ImportError:
            logger.warning("qdrant-client not available")
            return []

    def find_atypical(
        self,
        bone_type: str,
        mahalanobis_threshold: float = 2.0,
        limit: int = 50,
    ) -> list[dict[str, Any]]:
        """Find bones with atypical conformation.

        Args:
            bone_type: Type of bone.
            mahalanobis_threshold: Threshold for Mahalanobis distance.
            limit: Max results.

        Returns:
            List of atypical bones.
        """
        try:
            from qdrant_client.http import models as qmodels

            client = self._get_client()
            results = client.scroll(
                collection_name=self.collection,
                scroll_filter=qmodels.Filter(
                    must=[
                        qmodels.FieldCondition(
                            key="bone_type",
                            match=qmodels.MatchValue(value=bone_type),
                        ),
                        qmodels.FieldCondition(
                            key="conformation.mahalanobis_distance",
                            range=qmodels.Range(gte=mahalanobis_threshold),
                        ),
                    ]
                ),
                limit=limit,
            )

            return [{"id": str(r.id), "payload": r.payload} for r in results[0]]
        except ImportError:
            logger.warning("qdrant-client not available")
            return []

    def get_population_stats(self, bone_type: str | None = None) -> dict[str, int]:
        """Get statistics about the atlas population.

        Args:
            bone_type: Optional bone type filter.

        Returns:
            Dict with population statistics.
        """
        try:
            from qdrant_client.http import models as qmodels

            client = self._get_client()
            # Count total
            count_filter = None
            if bone_type:
                count_filter = qmodels.Filter(
                    must=[
                        qmodels.FieldCondition(
                            key="bone_type",
                            match=qmodels.MatchValue(value=bone_type),
                        )
                    ]
                )

            count = client.count(
                collection_name=self.collection,
                count_filter=count_filter,
            ).count

            stats: dict[str, int] = {"total": count}

            if bone_type is None:
                # Count per bone type
                for bt in BONE_TYPES:
                    bt_filter = qmodels.Filter(
                        must=[
                            qmodels.FieldCondition(
                                key="bone_type",
                                match=qmodels.MatchValue(value=bt),
                            )
                        ]
                    )
                    stats[bt] = client.count(
                        collection_name=self.collection,
                        count_filter=bt_filter,
                    ).count

            return stats
        except ImportError:
            logger.warning("qdrant-client not available")
            return {"total": 0}

    def delete_collection(self) -> None:
        """Delete the entire collection (use with caution)."""
        try:
            client = self._get_client()
            client.delete_collection(self.collection)
            logger.info("Deleted collection '%s'", self.collection)
        except ImportError:
            logger.warning("qdrant-client not available")

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
