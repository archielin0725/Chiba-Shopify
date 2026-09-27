#!/bin/bash
# ==============================================================================
# CHIBA Shopify - 全方位一鍵雙向同步腳本 (All-in-One Data Sync)
# 作用：拉取最新資料、同步推送至 archielin0725 與 sammywanwan、確保三方 100% 一致
# ==============================================================================

set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
cd "$DIR"

echo "================================================================="
echo "🔄 開始執行全資料同步 (Syncing Local + Archie + Sammy)..."
echo "================================================================="

# 1. 確保遠端設定
if ! git remote | grep -q "^origin$"; then
  git remote add origin https://github.com/archielin0725/Chiba-Shopify.git
fi

if ! git remote | grep -q "^sammy$"; then
  git remote add sammy https://github.com/sammywanwan/Chiba-Shopify.git
fi

# 2. 如果本地有修改且有帶訊息，自動 commit
COMMIT_MSG="$1"
if [ -n "$(git status --porcelain)" ]; then
  if [ -z "$COMMIT_MSG" ]; then
    COMMIT_MSG="update: sync latest changes"
  fi
  echo "📦 正在暫存並提交本地修改: $COMMIT_MSG"
  git add .
  git commit -m "$COMMIT_MSG"
fi

# 3. 先從主倉庫 (archielin0725) 拉取最新更新
echo ""
echo "📥 [1/3] 從 archielin0725 (origin) 拉取最新進度..."
git pull --rebase origin main

# 4. 推送到 sammywanwan (將落後的 sammywanwan 追齊)
echo ""
echo "📤 [2/3] 同步推送至 sammywanwan (sammy)..."
git push sammy main

# 5. 推送到 archielin0725 (若本地有新 commit)
echo ""
echo "📤 [3/3] 同步推送至 archielin0725 (origin)..."
git push origin main

# 6. 執行三方對照檢查
echo ""
"$DIR/sync_check.sh"
