# CHIBA Taiwan — Shopify Theme & Product Data Archive

此倉庫為德國 CHIBA 台灣官方 Shopify 專案之完整程式碼、佈景主題與商品主檔資料庫。

## 倉庫資訊
- **GitHub 倉庫**：[https://github.com/archielin0725/Chiba-Shopify](https://github.com/archielin0725/Chiba-Shopify)
- **本地工作目錄**：`/Users/archie/Chiba-Shopify`
- **主要分支**：`main`
- **安全屬性**：Private（私人倉庫，確保內部數據與自訂主題資產安全）

## 目錄架構
- `theme/`：Shopify 官方優化版 Horizon 佈景主題完整源碼（Liquid 模板、Sections、Blocks、Snippets、Locales 等）
- `CHIBA-Shopify-theme.zip`：官方主題上線發布壓縮包
- `chiba-horizon-theme-optimized.zip`：效能優化版主題發布壓縮包
- `data/`：
  - `products_all_shopify_import.csv`：Shopify 全館商品主檔匯入檔（含專屬特色與完整 HTML 介紹文案）
  - `products_export_1.csv`：基礎匯出資料備份
  - `products_supplementary_3030424_3400018.csv`：補充商品規格清單
  - `Pure_Race_II_Photos/`：Pure Race II 高解析度商品圖庫
  - `Retro_Black_Brown_Photos/`：Retro 系列高解析度商品圖庫

## 同步與版本控制規範

### 模式 1：與 AI 協作時「自動推送」（永久標準規範）
- **運作方式**：未來只要使用者指示更新 Shopify 相關檔案（例如：「修改某個 Liquid 模板」、「更新樣式設定」或「新增/更新商品 CSV」）。
- **行為**：AI 在修改完本地檔案（`/Users/archie/Chiba-Shopify`）並驗證無誤後，會自動在任務結尾執行：
  ```bash
  git add . && git commit -m "<清楚描述修改內容>" && git push origin main
  ```
  一次性同步到 GitHub，完全不需要使用者手動輸入任何 Git 指令。

## 歷史版本還原（Rollback）
若需要還原到先前的任何歷史版本：
- 方式一：直接在對話中告知 AI：「幫我還原到上一版本」或「還原到指定日期的狀態」。
- 方式二：手動執行 `git restore .`（放棄未提交修改）或 `git revert HEAD && git push`（安全回退上一版）。
