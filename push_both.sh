#!/bin/bash
# ==============================================================================
# CHIBA Shopify - 雙向同步推送腳本 (Push to Both GitHub Accounts)
# 自動同步推送至 archielin0725 與 sammywanwan 兩大倉庫
# ==============================================================================

set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
cd "$DIR"

echo "================================================================="
echo "🚀 準備同步推送代碼至 archielin0725 與 sammywanwan..."
echo "================================================================="

# 1. 檢查遠端設定
if ! git remote | grep -q "^origin$"; then
  git remote add origin https://github.com/archielin0725/Chiba-Shopify.git
fi

if ! git remote | grep -q "^sammy$"; then
  git remote add sammy https://github.com/sammywanwan/Chiba-Shopify.git
fi

# 2. 如果有變更且傳入了 commit 訊息，則自動 commit
COMMIT_MSG="$1"
if [ -n "$(git status --porcelain)" ]; then
  if [ -z "$COMMIT_MSG" ]; then
    echo "⚠️ 偵測到本地有未提交的檔案修改，但未提供 Commit 訊息。"
    echo "使用方式範例："
    echo "  ./push_both.sh \"feat: 修改導覽列與商品頁樣式\""
    echo ""
    read -p "請輸入 Commit 訊息（直接按 Enter 取消）: " USER_INPUT_MSG
    if [ -z "$USER_INPUT_MSG" ]; then
      echo "❌ 已取消操作。"
      exit 1
    fi
    COMMIT_MSG="$USER_INPUT_MSG"
  fi
  echo "📦 正在暫存並提交變更: $COMMIT_MSG"
  git add .
  git commit -m "$COMMIT_MSG"
else
  echo "ℹ️ 工作區乾淨，準備推送最新 Commit..."
fi

# 3. 推送至 Archie (origin)
echo ""
echo "📤 [1/2] 正在推送至 archielin0725 (origin main)..."
git push origin main

# 4. 推送至 Sammy (sammy)
echo ""
echo "📤 [2/2] 正在推送至 sammywanwan (sammy main)..."
git push sammy main

# 5. 再次檢驗三方一致性
echo ""
"$DIR/sync_check.sh"
