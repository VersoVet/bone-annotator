"""Qdrant vector store for the bone atlas.

Manages the `bone_atlas` collection with 512D embeddings and rich payloads
for similarity search, conformation analysis, and population statistics.
"""

import logging
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
        logger.info(
            "BoneAtlasStore initialized for %s:%d/%s",
            host,
            port,
            collection,
        )

    def ensure_collection(self) -> None:
        """Create the collection if it doesn't exist."""
        try:
            from qdrant_client import QdrantClient
            from qdrant_client.http import models as qmodels

            if self.client is None:
                self.client = QdrantClient(host=self.host, port=self.port)

            collections = [c.name for c in self.client.get_collections().collections]
            if self.collection in collections:
                logger.info("Collection '%s' already exists", self.collection)
                return

            self.client.create_collection(
                collection_name=self.collection,
                vectors_config=qmodels.VectorParams(
                    size=self.vector_size,
                    distance=qmodels.Distance.COSINE,
                ),
            )

            # Create payload indexes for common filters
            for field in ["bone_type", "side", "region", "source.specimen_id"]:
                self.client.create_payload_index(
                    collection_name=self.collection,
                    field_name=field,
                    field_schema=qmodels.PayloadSchemaType.KEYWORD,
                )

            # Numeric indexes for range queries
            for field in ["conformation.mahalanobis_distance", "confidence.bone"]:
                self.client.create_payload_index(
                    collection_name=self.collection,
                    field_name=field,
                    field_schema=qmodels.PayloadSchemaType.FLOAT,
                )

            logger.info("Created collection '%s' with indexes", self.collection)
        except ImportError:
            logger.warning("qdrant-client not available")

    def upsert_bone(
        self,
        point_id: str,
        embedding: list[float],
        payload: dict[str, Any],
    ) -> None:
        """Insert or update a bone entry in the atlas.

        Args:
            point_id: Point ID.
            embedding: 512D vector.
            payload: Rich metadata.
        """
        try:
            from qdrant_client import QdrantClient
            from qdrant_client.http import models as qmodels

            if self.client is None:
                self.client = QdrantClient(host=self.host, port=self.port)

            self.client.upsert(
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

    def upsert_batch(
        self,
        points: list[dict[str, Any]],
    ) -> None:
        """Batch insert/update. Each dict needs 'id', 'embedding', 'payload'.

        Args:
            points: List of point dicts.
        """
        try:
            from qdrant_client import QdrantClient
            from qdrant_client.http import models as qmodels

            if self.client is None:
                self.client = QdrantClient(host=self.host, port=self.port)

            qdrant_points = [
                qmodels.PointStruct(
                    id=p["id"],
                    vector=p["embedding"],
                    payload=p["payload"],
                )
                for p in points
            ]
            # Upsert in chunks of 100
            chunk_size = 100
            for i in range(0, len(qdrant_points), chunk_size):
                chunk = qdrant_points[i : i + chunk_size]
                self.client.upsert(
                    collection_name=self.collection,
                    points=chunk,
                )
            logger.info("Upserted %d points to '%s'", len(points), self.collection)
        except ImportError:
            logger.warning("qdrant-client not available")

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
            from qdrant_client import QdrantClient
            from qdrant_client.http import models as qmodels

            if self.client is None:
                self.client = QdrantClient(host=self.host, port=self.port)

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

            results = self.client.query_points(
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
            from qdrant_client import QdrantClient
            from qdrant_client.http import models as qmodels

            if self.client is None:
                self.client = QdrantClient(host=self.host, port=self.port)

            results = self.client.scroll(
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
            from qdrant_client import QdrantClient
            from qdrant_client.http import models as qmodels

            if self.client is None:
                self.client = QdrantClient(host=self.host, port=self.port)

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

            count = self.client.count(
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
                    stats[bt] = self.client.count(
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
            from qdrant_client import QdrantClient

            if self.client is None:
                self.client = QdrantClient(host=self.host, port=self.port)

            self.client.delete_collection(self.collection)
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
