"""PostgreSQL schema migrations for bone_annotations.

All migrations are idempotent (IF NOT EXISTS / ADD COLUMN IF NOT EXISTS).
"""

SCHEMA = "bone_annotations"

MIGRATIONS = [
    # --- frame_annotations columns ---
    f"""ALTER TABLE {SCHEMA}.frame_annotations
        ADD COLUMN IF NOT EXISTS author VARCHAR(100) DEFAULT 'unknown'""",
    f"""ALTER TABLE {SCHEMA}.frame_annotations
        ADD COLUMN IF NOT EXISTS source VARCHAR(20) DEFAULT 'manual'""",
    f"""ALTER TABLE {SCHEMA}.frame_annotations
        ADD COLUMN IF NOT EXISTS confidence FLOAT""",
    f"""ALTER TABLE {SCHEMA}.frame_annotations
        ADD COLUMN IF NOT EXISTS validated_by VARCHAR(100)""",
    f"""ALTER TABLE {SCHEMA}.frame_annotations
        ADD COLUMN IF NOT EXISTS validated_at TIMESTAMPTZ""",
    f"""ALTER TABLE {SCHEMA}.frame_annotations
        ADD COLUMN IF NOT EXISTS created_at TIMESTAMPTZ DEFAULT NOW()""",
    f"""ALTER TABLE {SCHEMA}.frame_annotations
        ADD COLUMN IF NOT EXISTS model_version VARCHAR(200)""",
    # --- annotation_tasks table ---
    f"""CREATE TABLE IF NOT EXISTS {SCHEMA}.annotation_tasks (
        id SERIAL PRIMARY KEY,
        acquisition_id VARCHAR(100) NOT NULL,
        cvat_task_id INTEGER,
        source_name VARCHAR(50) DEFAULT 'bonestore',
        bone_type VARCHAR(50) NOT NULL,
        region VARCHAR(50) DEFAULT 'entire',
        status VARCHAR(20) DEFAULT 'created',
        assignee VARCHAR(100),
        author VARCHAR(100) NOT NULL DEFAULT 'system',
        has_pre_annotations BOOLEAN DEFAULT FALSE,
        frame_count INTEGER DEFAULT 0,
        annotated_frames INTEGER DEFAULT 0,
        cvat_url VARCHAR(500),
        dataset_path VARCHAR(500),
        pipeline_preset VARCHAR(100),
        pipeline_config JSONB,
        created_at TIMESTAMPTZ DEFAULT NOW(),
        updated_at TIMESTAMPTZ DEFAULT NOW(),
        validated_at TIMESTAMPTZ,
        validated_by VARCHAR(100),
        notes TEXT
    )""",
    f"""ALTER TABLE {SCHEMA}.annotation_tasks
        ADD COLUMN IF NOT EXISTS parent_task_id INTEGER""",
    # --- Multi-objective annotation profiles ---
    f"""ALTER TABLE {SCHEMA}.annotation_tasks
        ADD COLUMN IF NOT EXISTS profile_id VARCHAR(50)""",
    f"""ALTER TABLE {SCHEMA}.annotation_tasks
        ADD COLUMN IF NOT EXISTS objective VARCHAR(50)""",
    f"""ALTER TABLE {SCHEMA}.annotation_tasks
        ADD COLUMN IF NOT EXISTS labels_filter JSONB""",
    f"""ALTER TABLE {SCHEMA}.annotation_tasks
        ADD COLUMN IF NOT EXISTS crop_from_task_id INTEGER""",
    f"""ALTER TABLE {SCHEMA}.annotation_tasks
        ADD COLUMN IF NOT EXISTS crop_params JSONB""",
    # --- training_runs ---
    f"""CREATE TABLE IF NOT EXISTS {SCHEMA}.training_runs (
        id SERIAL PRIMARY KEY,
        run_name VARCHAR(200) NOT NULL UNIQUE,
        generation INTEGER NOT NULL DEFAULT 1,
        parent_run_id INTEGER,
        model_base VARCHAR(500) NOT NULL,
        model_output_path VARCHAR(500),
        dataset_path VARCHAR(500) NOT NULL,
        dataset_hash VARCHAR(64),
        label_map JSONB NOT NULL,
        bone_type VARCHAR(50) NOT NULL,
        epochs INTEGER NOT NULL,
        imgsz INTEGER NOT NULL DEFAULT 1408,
        batch_size INTEGER NOT NULL DEFAULT 4,
        map50 FLOAT, map50_95 FLOAT,
        precision_score FLOAT, recall_score FLOAT,
        total_images INTEGER,
        status VARCHAR(20) DEFAULT 'pending',
        started_at TIMESTAMPTZ, completed_at TIMESTAMPTZ,
        created_at TIMESTAMPTZ DEFAULT NOW()
    )""",
    # --- Traceability ---
    f"""ALTER TABLE {SCHEMA}.frame_annotations
        ADD COLUMN IF NOT EXISTS task_id INTEGER""",
    f"""ALTER TABLE {SCHEMA}.training_runs
        ADD COLUMN IF NOT EXISTS task_ids INTEGER[]""",
    f"""ALTER TABLE {SCHEMA}.training_runs
        ADD COLUMN IF NOT EXISTS pipeline_preset VARCHAR(100)""",
    f"""CREATE TABLE IF NOT EXISTS {SCHEMA}.cvat_projects (
        bone_type TEXT PRIMARY KEY,
        cvat_project_id INTEGER NOT NULL,
        created_at TIMESTAMPTZ DEFAULT NOW()
    )""",
    # --- BoneSeg integration ---
    f"""ALTER TABLE {SCHEMA}.frame_annotations
        ADD COLUMN IF NOT EXISTS quality_tier VARCHAR(10) DEFAULT 'silver'""",
    f"""UPDATE {SCHEMA}.frame_annotations
        SET quality_tier = 'gold'
        WHERE source = 'manual' AND validated_by IS NOT NULL""",
    f"""UPDATE {SCHEMA}.frame_annotations
        SET quality_tier = 'silver'
        WHERE source = 'corrected_ml' AND validated_by IS NOT NULL""",
    f"""UPDATE {SCHEMA}.frame_annotations
        SET quality_tier = 'pseudo'
        WHERE source = 'ml' AND validated_by IS NULL""",
    f"""CREATE TABLE IF NOT EXISTS {SCHEMA}.test_sets (
        id SERIAL PRIMARY KEY,
        bone_type VARCHAR(50) NOT NULL,
        acquisition_id VARCHAR(100) NOT NULL,
        added_at TIMESTAMP DEFAULT NOW(),
        UNIQUE(bone_type, acquisition_id)
    )""",
    f"""CREATE TABLE IF NOT EXISTS {SCHEMA}.bonestore_catalog (
        id SERIAL PRIMARY KEY,
        acquisition_id VARCHAR(100) NOT NULL UNIQUE,
        bone_type VARCHAR(50),
        category VARCHAR(100),
        frame_count INT DEFAULT 0,
        source_path VARCHAR(500),
        first_seen TIMESTAMP DEFAULT NOW(),
        ml_status VARCHAR(20) DEFAULT 'new',
        uncertainty_score FLOAT,
        uncertainty_model VARCHAR(200),
        scored_at TIMESTAMP,
        annotation_tier VARCHAR(10),
        in_test_set BOOLEAN DEFAULT FALSE,
        last_trained_gen INT,
        notes VARCHAR(500)
    )""",
    f"""CREATE INDEX IF NOT EXISTS idx_catalog_status
        ON {SCHEMA}.bonestore_catalog(ml_status)""",
    f"""CREATE INDEX IF NOT EXISTS idx_catalog_bone
        ON {SCHEMA}.bonestore_catalog(bone_type)""",
    f"""CREATE INDEX IF NOT EXISTS idx_catalog_score
        ON {SCHEMA}.bonestore_catalog(uncertainty_score DESC)""",
    f"""CREATE TABLE IF NOT EXISTS {SCHEMA}.boneseg_training_runs (
        id SERIAL PRIMARY KEY,
        run_name VARCHAR(200) NOT NULL,
        bone_type VARCHAR(50) NOT NULL,
        generation INT DEFAULT 1,
        parent_run_id INT REFERENCES {SCHEMA}.boneseg_training_runs(id),
        model_backend VARCHAR(50) DEFAULT 'smp_unet',
        bone_classes JSONB NOT NULL,
        tiers_used JSONB NOT NULL,
        train_count INT, val_count INT, test_count INT,
        epochs INT, best_dice FLOAT,
        per_class_dice JSONB,
        test_dice FLOAT,
        model_output_path VARCHAR(500),
        status VARCHAR(20) DEFAULT 'running',
        started_at TIMESTAMP DEFAULT NOW(),
        completed_at TIMESTAMP
    )""",
    f"""CREATE TABLE IF NOT EXISTS {SCHEMA}.learning_decisions (
        id SERIAL PRIMARY KEY,
        decided_at TIMESTAMPTZ DEFAULT NOW(),
        action VARCHAR(50) NOT NULL,
        bone_type VARCHAR(50),
        generation INT,
        gold_count INT,
        silver_count INT,
        trigger_source VARCHAR(50) DEFAULT 'system',
        payload JSONB,
        notes TEXT
    )""",
    f"""CREATE INDEX IF NOT EXISTS idx_learning_decisions_at
        ON {SCHEMA}.learning_decisions(decided_at DESC)""",
]
