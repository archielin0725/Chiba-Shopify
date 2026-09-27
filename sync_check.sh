#!/bin/bash
# ==============================================================================
# CHIBA Shopify - 狀態檢查與對齊檢驗腳本 (Sync Status Checker)
# 檢查 本機磁碟、archielin0725、sammywanwan 三方 Commit 是否完全一致
# ==============================================================================

set -e

# 切換至專案根目錄
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
cd "$DIR"

echo "================================================================="
echo "🔍 正在檢查 CHIBA 倉庫三方同步狀態 (Local / Archie / Sammy)..."
echo "================================================================="

# 確保遠端設定存在
if ! git remote | grep -q "^origin$"; then
  git remote add origin https://github.com/archielin0725/Chiba-Shopify.git
fi

if ! git remote | grep -q "^sammy$"; then
  git remote add sammy https://github.com/sammywanwan/Chiba-Shopify.git
fi

echo "📡 正在抓取遠端最新資訊 (Fetching origin & sammy)..."
git fetch origin main --quiet 2>/dev/null || echo "⚠️ 無法抓取 origin，將以快取檢驗"
git fetch sammy main --quiet 2>/dev/null || echo "⚠️ 無法抓取 sammy，將以快取檢驗"

LOCAL_COMMIT=$(git rev-parse HEAD 2>/dev/null || echo "N/A")
ARCHIE_COMMIT=$(git rev-parse origin/main 2>/dev/null || echo "N/A")
SAMMY_COMMIT=$(git rev-parse sammy/main 2>/dev/null || echo "N/A")

LOCAL_SHORT=${LOCAL_COMMIT:0:7}
ARCHIE_SHORT=${ARCHIE_COMMIT:0:7}
SAMMY_SHORT=${SAMMY_COMMIT:0:7}

echo ""
echo "📊 當前 Commit 雜湊對照表："
echo "-----------------------------------------------------------------"
printf "%-20s | %-10s | %s\n" "節點" "Commit" "最新 Commit 標題"
echo "-----------------------------------------------------------------"
printf "%-20s | %-10s | %s\n" "1. 本機磁碟 (Local)" "$LOCAL_SHORT" "$(git log -1 --pretty=format:'%s' HEAD 2>/dev/null)"
printf "%-20s | %-10s | %s\n" "2. archielin0725" "$ARCHIE_SHORT" "$(git log -1 --pretty=format:'%s' origin/main 2>/dev/null)"
printf "%-20s | %-10s | %s\n" "3. sammywanwan" "$SAMMY_SHORT" "$(git log -1 --pretty=format:'%s' sammy/main 2>/dev/null)"
echo "-----------------------------------------------------------------"

echo ""
if [ "$LOCAL_COMMIT" == "$ARCHIE_COMMIT" ] && [ "$LOCAL_COMMIT" == "$SAMMY_COMMIT" ]; then
  echo "🎉 【完全一致】本機、archielin0725 與 sammywanwan 資料 100% 同步！"
  echo "✅ 你可以安全開始進行修改。"
else
  echo "⚠️ 【尚未完全一致】"
  if [ "$LOCAL_COMMIT" != "$ARCHIE_COMMIT" ]; then
    echo "  - 本機與 archielin0725 不一致"
  fi
  if [ "$LOCAL_COMMIT" != "$SAMMY_COMMIT" ]; then
    BEHIND_COUNT=$(git rev-list --count sammy/main..HEAD 2>/dev/null || echo "?")
    echo "  - sammywanwan 落後本機/Archie $BEHIND_COUNT 個 Commit。"
    echo "    👉 請在終端機執行: git push sammy main"
    echo "       或至網頁 https://github.com/sammywanwan/Chiba-Shopify 點擊「Sync fork」"
  fi
fi

echo "================================================================="
