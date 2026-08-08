"""Service d'annotation CVAT et YOLO.

Orchestration: pré-annotation automatique YOLO → CVAT → annotations manuelles.
"""


async def get_acquisition_status(acquisition_id: str) -> dict:
    """Récupère le statut d'une acquisition dans le pipeline annotation.

    Args:
        acquisition_id: ID de l'acquisition BoneStore.

    Returns:
        Dictionnaire avec le statut et métadonnées.
    """
    # TODO: Implémenter récupération statut depuis PostgreSQL
    return {
        "acquisition_id": acquisition_id,
        "status": "pending",
        "frames": 0,
        "annotated": 0,
    }
