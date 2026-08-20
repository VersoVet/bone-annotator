#!/bin/bash
# Deploy SAM (Segment Anything Model) to CVAT/Nuclio
# Reads config from config/sources.yaml and deploys the configured model variant
#
# Usage: ./scripts/deploy_sam.sh
# Change model in config/sources.yaml → sam.model_type then re-run this script

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
CONFIG="$PROJECT_DIR/config/sources.yaml"

if [ ! -f "$CONFIG" ]; then
    echo "ERROR: $CONFIG not found"
    exit 1
fi

# Read SAM config from sources.yaml
MODEL_TYPE=$(python3 -c "import yaml; print(yaml.safe_load(open('$CONFIG')).get('sam',{}).get('model_type','vit_b'))")
CHECKPOINT=$(python3 -c "import yaml; print(yaml.safe_load(open('$CONFIG')).get('sam',{}).get('checkpoint','sam_vit_b_01ec64.pth'))")
CHECKPOINT_URL=$(python3 -c "import yaml; print(yaml.safe_load(open('$CONFIG')).get('sam',{}).get('checkpoint_url','https://dl.fbaipublicfiles.com/segment_anything/sam_vit_b_01ec64.pth'))")
CVAT_HOST=$(python3 -c "import yaml; print(yaml.safe_load(open('$CONFIG')).get('sam',{}).get('cvat_host','10.0.0.59'))")
CVAT_PATH=$(python3 -c "import yaml; print(yaml.safe_load(open('$CONFIG')).get('sam',{}).get('cvat_path','/opt/onyx/cvat'))")

echo "=== SAM Deployment ==="
echo "Model type:     $MODEL_TYPE"
echo "Checkpoint:     $CHECKPOINT"
echo "Checkpoint URL: $CHECKPOINT_URL"
echo "CVAT host:      $CVAT_HOST"
echo "CVAT path:      $CVAT_PATH"
echo ""

SAM_DIR="$CVAT_PATH/serverless/pytorch/facebookresearch/sam/nuclio"

# Update function.yaml on CVAT host
echo "[1/4] Updating function.yaml..."
ssh onyx@"$CVAT_HOST" "
cd $SAM_DIR
sed -i 's|value: vit_.*|value: $MODEL_TYPE|' function.yaml
sed -i 's|value: /opt/nuclio/sam/sam_.*|value: /opt/nuclio/sam/$CHECKPOINT|' function.yaml
sed -i 's|image: cvat.pth.facebookresearch.sam.vit_.*|image: cvat.pth.facebookresearch.sam.$MODEL_TYPE|' function.yaml
sed -i 's|curl -O https://dl.fbaipublicfiles.com/segment_anything/.*|curl -O $CHECKPOINT_URL|' function.yaml
"

# Update model_handler.py env var defaults
echo "[2/4] Updating model_handler.py defaults..."
ssh onyx@"$CVAT_HOST" "
cd $SAM_DIR
sed -i \"s|'SAM_MODEL_TYPE', '.*'|'SAM_MODEL_TYPE', '$MODEL_TYPE'|\" model_handler.py
sed -i \"s|'SAM_CHECKPOINT',|'SAM_CHECKPOINT',|\" model_handler.py
"

# Delete old function and redeploy
echo "[3/4] Removing old SAM function..."
ssh onyx@"$CVAT_HOST" "nuctl delete function pth-facebookresearch-sam-vit-h --platform local 2>/dev/null || true"

echo "[4/4] Deploying SAM $MODEL_TYPE..."
ssh onyx@"$CVAT_HOST" "cd $CVAT_PATH && ./serverless/deploy_cpu.sh serverless/pytorch/facebookresearch/sam"

echo ""
echo "=== SAM $MODEL_TYPE deployed ==="
echo "Refresh CVAT (Ctrl+F5) and use AI Tools > Segment Anything"
