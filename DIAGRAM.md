# bone-annotator - Diagramme Architecture

## Vue Générale des Composants

```mermaid
graph TB
    subgraph External["Services Externes"]
        BS["BoneStore NFS<br/>10.0.0.52<br/>/mnt/bonestore"]
        PG["PostgreSQL<br/>10.0.0.59:5433<br/>bone_annotations"]
        QD["Qdrant<br/>10.0.0.59:6333<br/>bone_atlas + bone_annotations"]
        CVAT["CVAT Server<br/>Synapse<br/>Annotation séries"]
        ML["ml-compute<br/>10.0.0.44:9469<br/>Ray Jobs API"]
        LG["label-generator<br/>10.0.0.59:9466<br/>Labels anatomiques"]
    end

    subgraph BoneAnnotator["bone-annotator (FastAPI)<br/>Port 9468 - OnyxSynapse"]
        Main["main.py<br/>FastAPI App<br/>Lifespan"]
        
        subgraph Modules["Modules Fonctionnels"]
            BoneStoreM["bonestore<br/>NFS Traversal"]
            ImagingM["imaging<br/>Frame Loading<br/>Cache LRU GPU"]
            AnnotationM["annotation<br/>CVAT Orchestration"]
            StorageM["storage<br/>PostgreSQL + Qdrant"]
            IngestionM["ingestion<br/>BoneStore Sync<br/>Registry"]
            PredictM["predict<br/>YOLO Inference"]
            TrainingM["training<br/>Ray Jobs Submit"]
            DatasetM["dataset<br/>Export YOLO Format"]
            CVATModuleM["cvat<br/>CVAT REST API"]
            DashboardM["dashboard<br/>SSE Events"]
        end
        
        Models["models.py<br/>Pydantic Schemas"]
    end

    subgraph Flows["Flux de Données"]
        Flow1["Ingestion Pipeline"]
        Flow2["Pre-annotation Pipeline"]
        Flow3["Annotation Pipeline"]
        Flow4["Training Pipeline"]
    end

    %% Connections
    Main --> Modules
    Modules --> Models
    
    BoneStoreM --> BS
    ImagingM --> BS
    AnnotationM --> CVAT
    StorageM --> PG
    StorageM --> QD
    IngestionM --> BS
    IngestionM --> StorageM
    PredictM --> ML
    TrainingM --> ML
    DatasetM --> StorageM
    CVATModuleM --> CVAT
    AnnotationM --> CVATModuleM
    PredictM --> ImagingM
    DashboardM --> Modules
    
    %% Flow connections
    Flow1 -.->|BoneStore NFS Discovery| IngestionM
    Flow1 -.->|Store Metadata| StorageM
    
    Flow2 -.->|Load Frames| ImagingM
    Flow2 -.->|YOLO Predict| PredictM
    Flow2 -.->|Push to CVAT| AnnotationM
    
    Flow3 -.->|Manual Annotations| AnnotationM
    Flow3 -.->|Store in DB| StorageM
    
    Flow4 -.->|Export Dataset| DatasetM
    Flow4 -.->|Submit Training| TrainingM
    Flow4 -.->|Store Models| StorageM
    
    LG -.->|Fetch Labels| AnnotationM

    style BoneAnnotator fill:#e8f4f8
    style External fill:#fff4e6
    style Modules fill:#f0f8ff
    style Flows fill:#f0fff0
```

## Flux Détaillés

### 1. Ingestion (Sync BoneStore)

```mermaid
sequenceDiagram
    participant Cron
    participant Ingestion as ingestion.service
    participant NFS as BoneStore NFS
    participant DB as PostgreSQL
    participant Registry as ingestion_registry.db

    Cron->>Ingestion: sync_acquisitions()
    Ingestion->>NFS: Scan /mnt/bonestore
    NFS-->>Ingestion: List acquisitions
    Ingestion->>Registry: Get last_sync_time
    Registry-->>Ingestion: timestamp
    Ingestion->>DB: Store new acquisitions
    DB-->>Ingestion: Stored IDs
    Ingestion->>Registry: Update sync status
    Registry-->>Ingestion: OK
    Ingestion-->>Cron: synced=5, new=2, pending=12
```

### 2. Pré-annotation (YOLO)

```mermaid
sequenceDiagram
    participant Annotation
    participant Imaging as imaging.service
    participant Predict as predict.service
    participant CVAT as CVAT API
    participant NFS as BoneStore NFS

    Annotation->>Imaging: load_frames(acq_id)
    Imaging->>NFS: Read .b2nd file
    NFS-->>Imaging: Frames (GPU cache)
    Imaging-->>Annotation: Frame array[]
    Annotation->>Predict: predict(frames)
    Predict-->>Annotation: Predictions[]
    Annotation->>CVAT: push_predictions(task_id, preds)
    CVAT-->>Annotation: OK
    Annotation-->>Annotation: Display SSE event
```

### 3. Annotation Manuelle (CVAT)

```mermaid
sequenceDiagram
    participant Radiologist
    participant CVAT
    participant CVATModule as cvat.sync
    participant DB as PostgreSQL
    participant Qdrant

    Radiologist->>CVAT: Edit annotations
    Radiologist->>CVAT: Submit task
    CVAT-->>CVAT: Task completed
    CVATModule->>CVAT: sync_from_cvat(task_id)
    CVAT-->>CVATModule: Annotations XML/JSON
    CVATModule->>DB: Store zones, landmarks, measurements
    DB-->>CVATModule: OK
    CVATModule->>Qdrant: Vectorize + Store embeddings
    Qdrant-->>CVATModule: OK
    CVATModule-->>CVATModule: Emit SSE event
```

### 4. Training Actif (YOLO)

```mermaid
sequenceDiagram
    participant Dashboard
    participant Dataset as dataset.service
    participant Training as training.service
    participant MLCompute as ml-compute Ray
    participant DB as PostgreSQL
    participant Training as training.callback

    Dashboard->>Dataset: export_to_yolo(acquisitions)
    Dataset->>DB: Query annotations
    DB-->>Dataset: Annotations[]
    Dataset-->>Dataset: Export YAML config
    Dataset-->>Dashboard: dataset.yaml path
    
    Dashboard->>Training: submit_training(dataset.yaml)
    Training->>MLCompute: POST /api/jobs
    MLCompute-->>Training: job_id
    Training-->>Dashboard: job_id, ETA
    
    MLCompute->>MLCompute: Training (GPU, epochs)
    MLCompute->>Training: POST /callback (success)
    Training->>DB: Store model path, metrics
    DB-->>Training: OK
    Training-->>Dashboard: SSE: training_complete
```

### 5. Boucle d'Apprentissage Actif

```mermaid
graph TB
    A["1. Acquisitions<br/>BoneStore"] --> B["2. Pre-annotation<br/>YOLO v1"]
    B --> C["3. CVAT Task<br/>Created"]
    C --> D["4. Radiologist<br/>Annotates"]
    D --> E["5. Export<br/>Dataset"]
    E --> F["6. Training<br/>YOLO v2"]
    F --> G["7. Store<br/>Model v2"]
    G --> B
    
    style A fill:#e8f4f8
    style B fill:#fff4e6
    style C fill:#ffe8e8
    style D fill:#ffe8e8
    style E fill:#e8f4f8
    style F fill:#fff4e6
    style G fill:#f0f8ff
```

## Modules & Responsabilités

```mermaid
graph LR
    subgraph IO["I/O Layer"]
        BM["bonestore<br/>(NFS)"]
        IM["imaging<br/>(Frames)"]
    end
    
    subgraph Storage["Storage Layer"]
        SM["storage<br/>(DB)"]
        QM["Qdrant<br/>(Vectors)"]
    end
    
    subgraph ML["ML Layer"]
        PM["predict<br/>(YOLO)"]
        TM["training<br/>(Ray)"]
        DM["dataset<br/>(Export)"]
    end
    
    subgraph Integration["Integration Layer"]
        AM["annotation<br/>(CVAT)"]
        CM["cvat<br/>(REST API)"]
        IM2["ingestion<br/>(Sync)"]
    end
    
    subgraph Presentation["Presentation Layer"]
        Dashboard["dashboard<br/>(SSE)"]
        API["REST API<br/>(FastAPI)"]
    end
    
    BM --> IM
    IM --> PM
    PM --> AM
    AM --> CM
    CM --> Storage
    Storage --> TM
    TM --> DM
    DM --> Storage
    IM2 --> BM
    IM2 --> Storage
    AM --> Dashboard
    TM --> Dashboard
    API --> Dashboard
    
    style IO fill:#e8f4f8
    style Storage fill:#f0f8ff
    style ML fill:#fff4e6
    style Integration fill:#ffe8e8
    style Presentation fill:#f0fff0
```

---

**Dernière mise à jour**: 2026-08-09
**Phase**: 2 (CVAT Enhancement & ml-compute Training)
**Version**: v0.1.11+
