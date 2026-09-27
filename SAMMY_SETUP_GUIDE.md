# CHIBA Shopify 協同開發指南（Sammy 專屬 5 分鐘快速上手）

歡迎加入 CHIBA Shopify 電商主題開發！為了確保你與 Archie 在協同開發時**零衝突、代碼即時雙向同步**，並符合官方 0 失誤品質門檻，請依照以下步驟完成本機設定。

---

## 快速摘要 (Quick TL;DR)
* **遠端倉庫**：https://github.com/archielin0725/Chiba-Shopify.git
* **本機推薦路徑**：/Users/sammywang/Chiba-Shopify
* **主要分支**：main
* **協作金律**：
  1. 開工前先拉取：git pull --rebase origin main
  2. 提交前必過門檻：Shopify CLI Theme Check 0 Errors
  3. 完工後自動推送：git add . && git commit -m "..." && git push origin main

---

## 第一步：接受 GitHub 協作者邀請
1. 前往你的信箱（或登入 GitHub 帳號 sammywanwan）。
2. 開啟 Archie 發送的邀請信，點擊 「Accept invitation」 加入倉庫。
3. 倉庫網址：https://github.com/archielin0725/Chiba-Shopify

---

## 第二步：本機克隆倉庫 (Clone)
打開 Mac 終端機（Terminal），執行：
```bash
cd /Users/sammywang
git clone https://github.com/archielin0725/Chiba-Shopify.git
cd Chiba-Shopify
```

---

## 第三步：安裝官方檢查工具與自動防護網 (Quality Gate Setup)
CHIBA 專案嚴格遵守 Shopify 官方零失誤門檻，提交前必須通過 @shopify/cli theme check。

### 1. 測試 Shopify CLI 是否可用：
```bash
npx -y @shopify/cli theme check --path theme --fail-level error --no-color
```
*(第一次執行時 npx 會自動下載，看到 0 errors 即表示環境完全正常)*

### 2. 啟用本地 Git 防護攔截鉤子 (Pre-commit Hook)：
在專案中執行以下指令，配置自動攔截機制（若 Theme Check 未過則會自動阻止 commit，防止將錯誤代碼推上線）：
```bash
cat << 'EOF' > .git/hooks/pre-commit
#!/bin/bash
echo '🛡️ 執行本地 Shopify CLI Theme Check...'
npx -y @shopify/cli theme check --path theme --fail-level error --no-color
if [ $? -ne 0 ]; then
  echo '❌ Theme Check 未通過，已自動攔截提交！請修復錯誤後重試。'
  exit 1
fi
echo '✅ Theme Check 通過，允許提交。'
EOF

chmod +x .git/hooks/pre-commit
```

---

## 第四步：標準日常協作流程 (Daily Workflow)

無論是你手動編寫代碼，或是使用 AI 工具（Antigravity, Cursor, Claude, Copilot）協助，請遵循標準 3 步驟：

### 步驟 1：開工前同步最新進度
每次開始修改前，請務必先拉取 Archie 的最新變更：
```bash
git pull --rebase origin main
```

### 步驟 2：修改主題檔案
主題核心檔案位於 theme/ 目錄：
* theme/templates/：頁面 JSON 模板（index, product, collection, cart 等）
* theme/sections/：區塊佈局（header-group 等）
* theme/snippets/：Liquid 元件（選單、導覽、麵包屑、商品卡等）
* theme/assets/：樣式與腳本（base.css 等）

### 步驟 3：提交與自動推送 (Mode 1 Auto-Sync)
修改驗證完成後，直接推送回 GitHub：
```bash
git add .
git commit -m 'feat(功能名稱): 清楚描述本次修改內容'
git push origin main
```
*推送成功後，Archie 的本機與線上系統就能立即取得你的最新代碼！*

---

## 第五步：重要開發禁忌與設計規範 (Permanent Guidelines)
為確保全站品質，請牢記以下專案規範：
1. **選單字級層級**：
   * 頂級/父分類（自行車系列、健身系列）為粗體黑字（font-weight: 700, 1.15rem），帶細底線。
   * 子分類連結為自然大小寫、深灰色（font-weight: 400, 0.95rem, #4b5563），嚴禁全域暴力轉大寫（避免破壞 BioXCell 品牌專利大小寫）。
2. **手機版字級與觸控底線**：
   * 全站所有手機可見文字嚴禁低於 14px。
   * 所有按鈕與連結點擊熱區高度嚴禁低於 32px（推薦 44px）。
3. **禁止在 Section Group JSON 寫 custom_css**：
   * sections/header-group.json 等檔案嚴禁手動塞入多行 CSS 陣列，否則會導致 Shopify 核心解析器崩潰而丟失整組 Header。樣式請寫入 theme/assets/base.css。
4. **商品細節頁（PDP）圖片零裁切**：
   * templates/product.json 中的 media-gallery aspect_ratio 必須為 adapt，確保手套直向照片 100% 完整展示，不被強制切除指尖與手腕。

---

若在開發或同步過程中有任何問題，隨時與 Archie 聯繫！祝協同開發順利！


---

## 第六步：雙帳號與本機磁碟一鍵全自動同步腳本 (Master Sync Script)

當 Archie 在官方倉庫（`archielin0725`）進行任何更新發布後，你只需在你的 Mac 電腦執行以下標準腳本，即可**一次性完成三方同步**：
1. **官方最新代碼 (`archielin0725`)** ➔ **Sammy 本機磁碟 (`/Users/sammywang`)**
2. **Sammy 本機磁碟** ➔ **Sammy 個人 GitHub (`sammywanwan`)**

### 執行方式 (Run Once to Sync All)：
```bash
bash ~/Chiba-Shopify/scripts/sync_chiba.sh
```

### 腳本執行內容說明：
```bash
#!/usr/bin/env bash
# 1. 自動同步 Chiba-Shopify
cd ~/Chiba-Shopify
git remote set-url origin https://github.com/archielin0725/Chiba-Shopify.git
git pull --rebase origin main
git push https://github.com/sammywanwan/Chiba-Shopify.git main:main

# 2. 自動同步 Chiba-AI
cd ~/Chiba-AI
git remote set-url origin https://github.com/archielin0725/Chiba-AI.git
git pull --rebase origin main
git push https://github.com/sammywanwan/Chiba-AI.git main:main
```

### 💡 進階技巧：設定每 5 分鐘背景自動同步（完全免手動）
如果你希望本機磁碟與 GitHub 永遠自動保持最新，可以在終端機輸入 `crontab -e` 並加入此行：
```cron
*/5 * * * * bash ~/Chiba-Shopify/scripts/sync_chiba.sh >/dev/null 2>&1
```
從此只要 Archie 在 `archielin0725` 有任何修改，5 分鐘內自動推送到你的電腦硬碟與 `sammywanwan` GitHub，完全無感同步！
