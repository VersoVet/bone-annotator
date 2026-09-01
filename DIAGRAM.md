# bone-annotator - Diagramme Architecture

## Vue Générale des Composants

```mermaid
graph TB
    subgraph External["Services Externes"]
        BS["BoneStore NFS<br/>/mnt/bonestore<br/>Raw .b2nd"]
        PG["PostgreSQL<br/>10.0.0.44:5432<br/>bone_annotations"]
        QD["Qdrant<br/>10.0.0.59:6333<br/>bone_atlas"]
        CVAT["CVAT v2.72<br/>10.0.0.59:8080<br/>Annotation UI"]
        BONEML["bone-ml<br/>10.0.0.59:9463<br/>BoneSeg + YOLO"]
        MC["ml-compute<br/>10.0.0.44:9469<br/>GPU Jobs"]
        LG["label-generator<br/>10.0.0.59:9466<br/>Labels anatomiques"]
        PACS["OnyxBoneDatasetTraining<br/>10.0.0.90:8042<br/>PNG 16-bit datasets"]
    end

    subgraph BoneAnnotator["bone-annotator (FastAPI)<br/>Port 9468 - OnyxSynapse"]
        Main["main.py<br/>FastAPI + Lifespan"]
        
        subgraph Modules["Modules Fonctionnels"]
            SourcesM["sources<br/>Config YAML<br/>Multi-source"]
            PrepM["preparation<br/>imaging-sdk Pipeline<br/>.b2nd → PNG 16-bit"]
            AnnotationM["annotation<br/>Workflow Orchestration<br/>Create/Sync/Validate"]
            BoneStoreM["bonestore<br/>NFS Traversal"]
            ImagingM["imaging<br/>Frame Loading<br/>Cache LRU"]
            StorageM["storage<br/>pg_db + task_db"]
            IngestionM["ingestion<br/>BoneStore Sync"]
            CVATModuleM["cvat<br/>Client v2 + Sync"]
            DatasetM["dataset<br/>Export YOLO"]
            DashboardM["dashboard<br/>SSE Events"]
            LabelsM["labels<br/>label-generator Cache"]
            AnalysisM["analysis<br/>Morphometrics"]
            BoneSegM["boneseg<br/>Active Learning<br/>Test Set + GPU"]
        end
    end

    %% Core workflow
    SourcesM -->|Config| BoneStoreM
    BoneStoreM -->|Raw frames| ImagingM
    ImagingM -->|Load .b2nd| PrepM
    PrepM -->|PNG 16-bit| PACS
    AnnotationM -->|Labels| LabelsM
    AnnotationM -->|Create task| CVATModuleM
    AnnotationM -->|Pre-annotate| BONEML
    BoneSegM -->|AL cycle| BONEML
    BoneSegM -->|GPU check| MC
    BoneSegM -->|Create tasks| AnnotationM
    AnnotationM -->|Store tasks| StorageM
    CVATModuleM -->|Sync annotations| StorageM

    %% External connections
    LabelsM --> LG
    CVATModuleM --> CVAT
    StorageM --> PG
    StorageM --> QD
    DatasetM --> StorageM
    IngestionM --> BS
    DashboardM --> Modules
    PrepM -->|Upload prepared| CVAT

    style BoneAnnotator fill:#e8f4f8
    style External fill:#fff4e6
    style Modules fill:#f0f8ff
```

## Workflow Annotation Complet

```mermaid
sequenceDiagram
    participant User as Utilisateur
    participant BA as bone-annotator
    participant SDK as imaging-sdk
    participant LG as label-generator
    participant CVAT as CVAT v2
    participant BML as bone-ml
    participant PG as PostgreSQL

    User->>BA: POST /api/annotation/task
    BA->>PG: save task (status=preparing)
    BA-->>User: 201 {id, status=preparing} (< 1s)

    par Background preparation
        BA->>BA: sources.get_acquisition_path()
        BA->>SDK: prepare_dataset (pipeline)
        SDK-->>BA: PNG 16-bit images
        BA->>PG: update (status=uploading, frame_count)
        BA->>LG: get_labels_for_bone(type)
        LG-->>BA: zones + landmarks
        BA->>CVAT: create_task + set_labels
        BA->>CVAT: upload_image_paths (PNG)
        BA->>PG: update (status=created, cvat_task_id)
    end

    User->>BA: GET /api/annotation/tasks/{id} (poll)
    BA-->>User: progress + status

    opt Pre-annotation ML
        BA->>BML: POST /api/boneseg/annotate (preferred)
        alt BoneSeg unavailable
            BA->>BML: POST /api/cvat/annotate (YOLO fallback)
        end
        BML->>CVAT: Fetch frames + predict
        BML->>CVAT: Push pre-annotations
    end

    User->>CVAT: Annoter / Corriger

    User->>BA: POST /api/annotation/sync/{id}
    BA->>CVAT: Pull annotations
    BA->>CVAT: Get assignee (auteur)
    BA->>PG: Save frame_annotations (author)

    User->>BA: POST /api/annotation/validate/{id}
    BA->>PG: Update status=validated
```

## Pipeline Préparation Images

```mermaid
graph LR
    A["BoneStore<br/>.b2nd raw uint16"] --> B["imaging-sdk<br/>Pipeline filters"]
    B --> C["PNG 16-bit<br/>Annotation-ready"]
    C --> D["PACS 10.0.0.90<br/>OnyxBoneDatasetTraining"]
    C --> E["CVAT Upload<br/>Tâche annotation"]

    subgraph Pipelines["Presets imaging-sdk"]
        P1["replay_membre"]
        P2["high_contrast"]
        P3["soft_denoise"]
    end

    B --- Pipelines

    style A fill:#e8f4f8
    style B fill:#fff4e6
    style C fill:#f0fff0
    style D fill:#f0f8ff
    style E fill:#ffe8e8
```

## Modules & Responsabilités

```mermaid
graph LR
    subgraph Sources["Source Layer"]
        SM["sources<br/>(YAML Config)"]
        BM["bonestore<br/>(NFS)"]
        IM["imaging<br/>(Frames)"]
    end

    subgraph Preparation["Preparation Layer"]
        PM["preparation<br/>(imaging-sdk)"]
    end

    subgraph Workflow["Workflow Layer"]
        AM["annotation<br/>(Orchestration)"]
        BSM["boneseg<br/>(Active Learning)"]
        CM["cvat<br/>(REST v2)"]
        LM["labels<br/>(label-generator)"]
    end

    subgraph Storage["Storage Layer"]
        DB["storage/pg_db<br/>(Annotations)"]
        TD["storage/task_db<br/>(Tasks)"]
    end

    subgraph Export["Export Layer"]
        DM["dataset<br/>(YOLO)"]
        AN["analysis<br/>(Morpho)"]
    end

    SM --> BM --> IM --> PM
    PM --> AM
    LM --> AM
    BSM --> AM
    AM --> CM
    AM --> TD
    CM --> DB
    DB --> DM
    
    style Sources fill:#e8f4f8
    style Preparation fill:#fff4e6
    style Workflow fill:#ffe8e8
    style Storage fill:#f0f8ff
    style Export fill:#f0fff0
```

---

**Dernière mise à jour**: 2026-08-30
**Phase**: Dashboard admin + imaging-sdk pipelines
**Version**: v0.1.61









