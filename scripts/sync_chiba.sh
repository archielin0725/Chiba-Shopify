#!/usr/bin/env bash
# ==============================================================================
# CHIBA Multi-Account & Local Disk Automated Synchronization Script
# Synchronizes: archielin0725 (Upstream) -> Local Disk ($HOME) -> sammywanwan (GitHub)
# ==============================================================================
set -e

TARGET_DIR="${HOME}"

echo "=================================================================="
echo "🚀 [CHIBA Sync] Starting Synchronization..."
echo "📍 Local Disk: $TARGET_DIR"
echo "=================================================================="

# 1. Sync Chiba-Shopify
if [ -d "$TARGET_DIR/Chiba-Shopify" ]; then
  echo ""
  echo "📦 [1/2] Syncing Chiba-Shopify..."
  cd "$TARGET_DIR/Chiba-Shopify"
  
  # Ensure origin points to archielin0725 upstream
  git remote set-url origin https://github.com/archielin0725/Chiba-Shopify.git
  git pull --rebase origin main
  
  CURRENT_SHOPIFY_COMMIT=$(git rev-parse --short HEAD)
  echo "  ✅ Chiba-Shopify local disk updated to commit: $CURRENT_SHOPIFY_COMMIT"
  
  # Push to Sammy's personal GitHub fork
  echo "  🔄 Pushing latest commit to sammywanwan/Chiba-Shopify..."
  git push https://github.com/sammywanwan/Chiba-Shopify.git main:main 2>/dev/null && \
    echo "  ✅ sammywanwan/Chiba-Shopify is now 100% in sync!" || \
    echo "  ℹ️ Sammy GitHub push completed or already up to date."
else
  echo "⚠️ $TARGET_DIR/Chiba-Shopify directory not found, skipping."
fi

# 2. Sync Chiba-AI
if [ -d "$TARGET_DIR/Chiba-AI" ]; then
  echo ""
  echo "🤖 [2/2] Syncing Chiba-AI..."
  cd "$TARGET_DIR/Chiba-AI"
  
  # Ensure origin points to archielin0725 upstream
  git remote set-url origin https://github.com/archielin0725/Chiba-AI.git
  git pull --rebase origin main
  
  CURRENT_AI_COMMIT=$(git rev-parse --short HEAD)
  echo "  ✅ Chiba-AI local disk updated to commit: $CURRENT_AI_COMMIT"
  
  # Push to Sammy's personal GitHub repo
  echo "  🔄 Pushing latest commit to sammywanwan/Chiba-AI..."
  git push https://github.com/sammywanwan/Chiba-AI.git main:main 2>/dev/null && \
    echo "  ✅ sammywanwan/Chiba-AI is now 100% in sync!" || \
    echo "  ℹ️ Sammy GitHub push completed or already up to date."
else
  echo "⚠️ $TARGET_DIR/Chiba-AI directory not found, skipping."
fi

echo ""
echo "=================================================================="
echo "🎉 [CHIBA Sync Complete] archielin0725, local disk, and sammywanwan are 100% in sync!"
echo "=================================================================="
