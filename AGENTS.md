# CHIBA Permanent Working Standard

## Priority (in order)
1. CORRECTNESS
2. SECURITY
3. COMPLETION
4. SIMPLICITY
5. AUTOMATION
6. GREEN OPTIMIZATION

## Permanent Rules
- Finish the CURRENT phase before building future-phase infrastructure.
- Prefer the shortest safe path.
- Prefer prevention at the data boundary over post-build cleanup.
- Detect the actual technology stack before applying framework-specific settings.
- Do not invent a new framework if existing architecture is sufficient.
- Reuse validated existing work.
- Never restart from zero without evidence that prior work is invalid.
- Use deterministic scripts before Astra/AI reasoning.
- Use the smallest safe rebuild/test scope.
- Full regression only when release risk requires it.
- Do not interrupt the user for routine technical issues.
- Never expose confidential/internal data publicly.
- Never modify `~/Documents/Chiba`.
- Do not claim unsupported performance, carbon, credit, or energy savings.

## Recovery Instructions

Before substantial work, read `Output/CHIBA_TASK_CHECKPOINT.md` FIRST, then `CHIBA_CHECKPOINT_POLICY.md`.

After a usage-limit interruption or app restart, resume from the first incomplete phase recorded there. Do not repeat completed work unless regression evidence requires it.

Update `Output/CHIBA_TASK_CHECKPOINT.md` after every major phase, after regression testing, before risky changes, and before an expected usage-limit stop. Include completed, pending, last known good build, blockers, next action, and timestamp. Never mark an acceptance gate complete without evidence.

## Prior Incomplete Work Rule

Before executing ANY new CHIBA prompt, first determine whether the previous active task was fully completed by reading:
- `Output/CHIBA_TASK_CHECKPOINT.md`
- `Output/CHIBA_ACTIVE_CONTEXT.json` (if present)

If previous task is NOT complete: resume from checkpoint, complete or reach valid stop, verify, save checkpoint, THEN execute new request. A usage-limit stop, crash, or app restart is NOT completion.

## Source & Safety

- `/Users/archie/Documents/Chiba` is strictly read-only. Never modify, overwrite, rename, move, or delete anything under it.
- Do not publish externally, change DNS, sign up for paid services, or deploy to production without explicit human approval.
- Generated files belong inside `~/Chiba-AI`.
- Public website may use ONLY 台灣零售價 (approved Taiwan retail price). Never expose 經銷商價 (dealer price) publicly.

## Phase Roadmap
- **Phase 1**: Catalogue Completeness / Canonical Product Universe
- **Phase 1.5**: Catalogue Release Candidate
- **Phase 2**: Production Readiness (NOT started until Catalogue RC passes)
- **Phase 3**: Green Automation
- **Phase 4**: E-Commerce / Payment
- **Phase 5**: Growth / Optimization

Current execution scope: **Phase 2 Production Readiness**, explicitly authorized by attachment `550b6761-acbb-44cb-8db6-0cd7a1d0c566`. Phase1+1.5 is frozen PASS; do not restart it. No production/DNS cutover or Phase3 authorization.

## Catalogue conservation and durable state
- Catalogue plus approved Taiwan price-list SKU union is the universe, not the historical master count.
- Account for every SKU as preview-published, explicitly excluded with evidence, or human decision required. No silent omissions.
- Eligible SKU sets must equal public DTO, built JSON, product routes and collection-card SKU sets for each category/locale.
- Keep confidential fields out through an explicit public DTO allowlist before rendering; audit artifacts stay outside the served root.
- Checkpoint, active context, gate/release and coverage state must use same-directory temporary files, flush/fsync and atomic replacement. Use `scripts/chiba_atomic_state.py`; test failure preservation without damaging real state.
- Checkpoint is read FIRST, followed by policy and this file. Latest dated recovery entry takes precedence over historical entries. Record previous-task valid stop before switching missions.

## Repository Synchronization Standard (Chiba-Shopify & Chiba-AI)
- **模式 1：與 AI 協作時「自動推送」（永久標準規範）**
  - **運作方式**：未來只要使用者指示更新相關檔案（Shopify 主題、官方網站、MOMO 腳本等）：
  - **行為**：AI 在修改完本地檔案並驗證無誤後，必須自動在任務結尾執行 `git add . && git commit -m "<清楚描述修改內容>" && git push origin main`，一次性同步到 GitHub，完全不需要使用者手動輸入任何 Git 指令。
- **多開發者協同防護規範（Multi-Developer Pre-Fetch Standard）**：
  - 因目前有外部協作者（`sammywanwan`，本機路徑 `/Users/sammywang/Chiba-Shopify` 與 `/Users/sammywang/Chiba-AI`）共同開發：
  - **行為**：未來在開始任何相關任務前，AI **必須首先執行** `git pull --rebase origin main`，確保本機永遠基於遠端及協作者的最新提交開發，徹底杜絕覆蓋他人成果或版本脫鉤。

## File Versioning & Timestamp Naming Standard（永久檔案命名標準）
- **時間戳命名規範**：未來只要為使用者產出、打包任何交付檔案（包括但不限於：Shopify 主題 ZIP、商品 CSV、備份包等）：
  - 檔名必須自動附加時間戳（格式：`YYYYMMDD-HHMM`），例如：
    - `CHIBA-Shopify-theme-20260927-0238.zip`
    - `products_alt_text_fixed-20260927-0238.csv`
  - 同時在 Downloads 與專案目錄中產生，方便使用者在下載資料夾與瀏覽器選檔時一目了然、避免版本混淆。

## Shopify Quality Gate & Zero-Failure Standard (Shopify 零失誤驗收門檻規範)
- **四層防護網機制（必須 100% 遵守，絕不妥協）**：
  1. **第一層：官方編譯器強制門檻（Compiler Hard Gate）**
     - 任何涉及 Liquid、JSON、Section、Snippet、CSS、JS 的修改，在產出交付 ZIP 或執行 Git 提交前，**必須強制執行**：
       `npx -y @shopify/cli theme check --path theme --fail-level error --no-color`
     - **檢查結果必須為 0 Errors**。只要有 1 個 Error，嚴禁打包交付、嚴禁提交至 GitHub main。
  2. **第二層：核心頁面四角防線與禁忌語法清單（Core Pages Integrity & Forbidden Patterns）**
     - 四大核心模板（`templates/index.json` 首頁、`templates/product.json` 商品頁、`templates/collection.json` 分類頁、`templates/cart.json` 購物車）必須保持結構完整，嚴禁殘留不存在的 Section 引用（Orphan references）。
     - **選單導覽文字排版規範（Menu Typography Hierarchy Standard）**：
       * 頂層/父級大分類（`自行車系列`、`健身系列`）必須為粗體標題（`font-weight: 700`，深色 `#111`，字級 `1.15rem`），具備明確底線或區隔。
       * 子分類連結（`BioXCell 減壓系列`、`Comfort 舒適系列`、`重訓手套` 等）嚴禁被全域 `uppercase` 強制轉為大寫尖叫體（嚴禁 `type_case_primary_link: uppercase` 與 `menu_font_style: inverse_large` 反向倒置層級）。子分類必須保持自然大小寫與次級灰色（`#4b5563`，`0.95rem`）。
     - **商品列表頁首屏極簡與版位規範（Collection Page Above-The-Fold Standard）**：
       * `/collections/all` 與商品列表頁嚴禁渲染孤立、高達 100px+ 且帶 48px+ 上下留白的巨大機械翻譯「商品」標題。
       * 列表頁面頂部以麵包屑（如「首頁 / 全部商品」）提供清晰層級，下方直接緊接「篩選工具列」與「商品網格」，極大化首屏商品可視率（Above-The-Fold）。
       * 必須在主集合區塊內注入 `<h1 class="visually-hidden">` 保留無障礙與 SEO 標題權重，兼顧視覺極簡與搜尋引擎最佳化。
     - **JSON Section Group 嚴禁手動自訂 custom_css（Section Group JSON Integrity Standard）**：
       * `sections/header-group.json` 等 Section Group 檔案中，`custom_css` 屬於 Shopify 後台 Theme Editor 平台專用託管欄位。嚴禁在 JSON 中手動塞入多行 CSS 陣列或 `:hover` 規則，否則 Shopify 核心解析器會直接拒絕載入並默默丟棄整個 Section Group（導致全站 Header/Logo/選單整組蒸發）。
       * 任何元件樣式客製化必須寫入標準 Liquid 模板中的 `<style>` 標籤或 `assets/base.css`。
     - **商品卡片圖片容器與 Slideshow 原生結構保護規範（Product Card Slideshow Structural Integrity）**：
       * Horizon 主題中，多圖商品仰賴 `<slideshow-component>` 與 `<slideshow-slides>` CSS scroll-snap 原生體系。
       * 嚴禁在全域 CSS 中對 `.card-gallery` 或 `.product-media-container--image` 暴力強制 `display: flex !important`、`aspect-ratio: 1/1 !important` 或 `width: auto !important`，此舉會破壞 Slideshow 計算寬高，導致多圖手套與腰帶之圖片完全坍塌隱形。1:1 比例必須由 Horizon 原生 `--gallery-aspect-ratio: 1`（模板區塊設定 `"image_ratio": "square"`）自然渲染。
     - **首頁集合推薦標題純淨規範（Homepage Collection Title Cleanliness Standard）**：
       * 首頁推薦商品標題嚴禁使用 `{{ closest.collection.title }}熱門推薦商品`（當 collection 為 `all` 時會渲染出荒謬的「商品熱門推薦商品」）。
       * 必須硬編碼為純淨大器的「熱門推薦商品」或經由語意化前綴。
     - **商品詳情頁照片完整呈現與零裁切規範（Product Detail Page Media Full Display Standard）**：
       * 在 `templates/product.json` 中，商品主圖展示區塊（`media-gallery`）的 `aspect_ratio` 必須設定為 `"adapt"`（嚴禁設定為固定數值 `"1"`）。若設為 `"1"`，Horizon 核心會觸發 `unless aspect_ratio == 'adapt'` 判定，強行注入 `.media-fit-cover` 與 `object-fit: cover`，導致手套等直向縱長商品在 1:1 正方形容器中被強制放大拉滿，指尖與手腕部分遭到暴力裁切。
       * `constrain_to_viewport` 必須為 `true`，`media_fit` 必須為 `"contain"`，確保整幅手套完整納入螢幕可視區。
       * `snippets/slideshow-slide.liquid` 嚴禁在 HTML 標籤上殘留兩個重疊的 `style="..."` 屬性（避免瀏覽器 HTML 解析器直接丟棄後者而遺失 `--media-preview-ratio` 等關鍵變數）。
       * 在 `snippets/product-media-gallery-content.liquid` 樣式層必須配置兜底防護：`media-gallery .product-media-container img, media-gallery .product-media__image { object-fit: contain !important; object-position: center center; }`，從根源保證商品全圖 100% 完整無損展示。
     - **商品列表頁工具列與排序條件規範（Collection Toolbar & Sorting Criteria Standard）**：
       * **抽屜篩選按鈕架構（Option C）**：商品列表頁工具列嚴禁在頂部平鋪展開零散的「供貨情況」、「價格」等下拉選單。必須採用單一「篩選條件」按鈕（點擊從側欄滑出原生抽屜 `#filters-drawer`），工具列左側放置「篩選條件按鈕」與「共 X 件商品」，右側放置「排序選單」與「網格檢視切換」，實現俐落的兩端平衡對齊。
       * **排序選項精簡至 5 大實用條件**：嚴禁向顧客展示機械式的「依字母順序 (A 到 Z)」、「依字母順序 (Z 到 A)」、「日期 (從舊到新)」，以及同義重複的「最相關/精選」。必須精簡為 5 大高意圖選項：`精選推薦`、`熱門暢銷`、`價格：由低至高`、`價格：由高至低`、`最新上架`。
       * **品項文字在地化規範**：全站禁止使用生硬的機器翻譯「X 個品項」，必須標準化為繁體中文電商習慣的「共 X 件商品」與「查看 X 件商品」。
       * **供貨情況過濾防線**：在品牌型錄全店現貨情況下，篩選抽屜內必須排除 `filter.v.availability`（供貨情況），避免殘留只有單一「有存貨」的冗餘核取方塊。
     - **手機版排版與觸控最低門檻規範（Mobile Typography & Touch Target Minimum Standard）**：
       * 全站所有可見文字在手機視窗（≤ 749px）下嚴禁低於 **14px**（0.875rem）。低於此門檻的常見違規源頭：breadcrumbs（0.8rem → 12.8px）、商品卡價格使用 h6 preset（12px）、售價前綴 `.price-prefix`（0.85em of h6 = 10.2px）。
       * 所有可點擊元素（連結、按鈕、下拉選項）在手機視窗下嚴禁低於 **32px** 觸控高度（推薦 44px）。麵包屑連結、篩選條件選項、排序下拉選項為常見違規區。
       * 修正方式必須透過 `@media screen and (max-width: 749px)` CSS override，嚴禁直接修改桌面版基礎樣式。
       * 使用 `font-size: max(0.875rem, var(--font-size, 0.875rem))` 模式確保 CSS 變數不會壓低到門檻以下。
     - **模板 JSON 硬編碼英文字串完整在地化規範（Template JSON Hardcoded String Localization Standard）**：
       * 所有 `templates/*.json` 中的 `"text"`、`"label"`、`"heading"` 等可見字串欄位嚴禁殘留英文（如 "You may also like"、"View all"、"Featured collection"）。
       * 必須在每次修改 JSON 模板後，執行 `grep -rn 'You may also like\|View all\|Featured\|Add to cart\|See more' theme/templates/` 驗證零英文殘留。
       * 標準翻譯對照："You may also like" → "你可能也會喜歡"、"View all" → "查看全部"。
     - **Shopify 商品多變體 CSV 匯入規範與唯一真實資料來源 (Shopify Product CSV Single Source of Truth Standard)**：
       * **唯一合法真實資料來源 (Single Source of Truth)**：全站商品 CSV 的唯一標準基底檔為：
         `/Users/archie/Chiba-AI/data/canonical_shopify_products_master.csv`
         （此檔案具備 43 欄完整官方結構、94 款商品、1,271 列規格、0 重複變體、100% 繁中優化與 UTF-8 BOM 編碼；最新通過驗證基準版本為 `CHIBA_Shopify_Full_Products_Fixed_20260928-2027.csv`，含 0 醫學/0 專利法規避險與 40425 正反面圖庫校正與 0 類別警告清零）。
       * **嚴禁從零重新合成（Forbidden to Synthesize from Scratch）**：未來任何商品文字、標題、描述、圖片、SEO 或價格更新，**嚴禁**使用自製腳本從零拼裝或推導變體名稱（避免字典對照碰撞與 Fallback 錯誤）。**必須一律以該主檔為基底**，載入後僅修改目標欄位並另存新時間戳檔案。
       * **四大匯出硬門檻檢驗（Mandatory Assertion Gates Before Delivery）**：
         1. **結構門檻**：必須維持 43 欄標準結構，嚴禁只傳送 `Handle`、`Title`、`Body (HTML)`（否則觸發「`• 更新子類時，必須提供商品選項的輸入資料。`」報錯）。
         2. **唯一性門檻**：產出前必須執行 `python3 scripts/verify_shopify_csv_gate.py <file>` 驗證，同一個 Handle 內的 `(Option1 Value, Option2 Value)` 組合必須 100% 唯一，重複次數必須為 0（否則觸發「`子類「XXX / YYY」已存在。請至少變更一個選項值。`」報錯）。
         3. **編碼門檻**：輸出時強制指定 `encoding='utf-8-sig'`（UTF-8 with BOM），確保 Excel 與 Shopify 後台解析中文 100% 零亂碼。
         4. **類別門檻**：`Product Category` 嚴禁包含無效分類字串（如「單車手套」），預設留白由 Shopify 自動歸類，確保匯入 0 Warnings。
       * **雙目錄時間戳交付**：產出之 CSV 必須同步存於 `Downloads/` 與 `Output/`，檔名格式：`CHIBA_Shopify_Full_Products_Fixed_YYYYMMDD-HHMM.csv`。
     - **官方網站 (www.chibataiwan.com) 與 Shopify 商城 (shop.chibataiwan.com) 雙平台聯動標準 (Dual-Platform Alignment Standard)**：
       * **三位一體鍵值對齊 (Tri-Key Consistency)**：商品 `Handle`（如 `chiba-40186-fitness`）、規格 `Variant SKU`（如 `40186-BLACKGOLD-S/M`）與建議售價 `Price`（如 `NT$ 1,280`），在官網靜態 DTO/JSON、Shopify CSV 主檔與導購對照表（`shopify-variant-map.json`）中必須 100% 絕對一致。
       * **官網跳轉預選子類 (Variant Deep-Link Handover)**：官網商品頁選定顏色與尺寸點擊「前往購買」時，帶入的 URL 參數 `?variant={variant_id}` 必須與 Shopify 後台子類 ID 絕對對齊，實現即時預選規格與一鍵加入購物車。
       * **全站嚴格單一零售價防線 (RRP Brand Protection)**：全站（官網、Shopify、匯出 DTO、JSON）僅允許渲染台灣官方建議零售價（建議售價 / RRP），禁止出現小數點 `.00`。嚴禁在任何公開檔案或 CSV `Cost per item` 洩漏原廠經銷商批發價（Dealer Price）。
       * **標準商品標題公式**：統一採用 `CHIBA [英文型號/系列] [繁體中文品名]`（例如：`CHIBA Motivation Grippad 激勵防滑握力護墊`）。
       * **結構化 HTML 描述規範**：統一採用 `<div class="chiba-product-description">`，依序包含產品核心特點條列、系列材質、標準洗滌保養（`30°C 水洗或柔洗，平放陰乾，切勿烘乾`）、德國百年研發承諾，以及官方授權正品免運保證。
       * **掌圍指南品類邊界**：掌圍尺寸測量表（XS–XXL / 16.5–29cm）僅限手套品類（58款）注入；車衣、袖套、腰帶、深蹲纏繞護膝等 36 款非手套商品嚴禁殘留任何掌圍指南文字。
     - **Liquid 禁忌清單**：
       * 嚴禁對 Array / Drop 集合物件調用字串專用 Filter（如 `| slice:`）。
       * 嚴禁將 `TemplateDrop` 當作純字串直接比對（嚴禁 `template == 'index'`，必須使用 `template.name == '...'`）。
       * 嚴禁未經 Schema 定義建立超過 2 層以上的深度自訂巢狀 Block。
  3. **第三層：Git Pre-Commit Hook 物理攔截**
     - 在 `/Users/archie/Chiba-Shopify/.git/hooks/pre-commit` 中配置自動檢驗，若 Theme Check 未通過，Git 底層直接拒絕 Commit。
  4. **第四層：發布 ZIP 二次校驗規範**
     - 產出 ZIP 後，必須自動解壓縮驗證：
       * 根目錄直接為主題子目錄（`assets/`, `config/`, `layout/`, `locales/`, `sections/`, `snippets/`, `templates/`），嚴禁外層多包一層資料夾。
       * 核心模板必須存在且非空，並在 `Downloads/` 與專案目錄同步產生帶時間戳檔案（格式：`CHIBA-Shopify-theme-YYYYMMDD-HHMM.zip`）。

## MOMO E-Commerce Upload Package Standard (MOMO 零失誤驗收門檻規範)
- **六大防線（必須 100% 遵守，絕不妥協）**：
  1. **價格 100% 對齊官方零售價**：所有商品必須完全對齊台灣建議售價（RRP），嚴禁洩漏或混入經銷商價（Dealer Price）。
  2. **手套 vs 非手套掌圍對照表分離**：僅手套品類（58款）注入掌圍測量表；非手套商品（35款車衣、袖套、鞋套等）嚴禁殘留任何掌圍指南文字。
  3. **欄位合規與長度檢驗**：
     - Col03 分類碼統一 `3201000001`，Col31 倉庫代碼統一 `000001`。
     - Col33（商品名稱）、Col34（規格名稱）嚴格限制字元長度，零超標截斷。
     - Col04、Col12、Col27、Col37 嚴格留白，符合 MOMO 官方匯入標準。
  4. **實體檔案格式嚴格驗證**：Excel 必須為標準 BIFF8 (`.xls`) 實體二進位格式，嚴禁拿 CSV 或 XLSX 假冒副檔名。
  5. **圖檔 ZIP 扁平化結構**：ZIP 內部必須為純扁平結構（單層放圖），嚴禁包內子目錄、嚴禁包含 `.DS_Store` 或 `__MACOSX`。
  6. **產出前強制執行確定性檢驗腳本**：必須執行 `python3 scripts/momo_products_pipeline.py` 通過所有 Assert 檢查，並在 `Downloads/` 與 `Output/` 同步產生帶時間戳交付包。

## Continuous Self-Correction & Autonomous Learning Protocol (全自動自省沉澱與規則自更新協議)
- **自治學習原則（無需使用者提醒，犯錯時自動執行 /learn）**：
  - 未來只要在任何任務（Shopify、MOMO、官網、型錄等）中遇到使用者指正、執行異常、或重大除錯：
    1. **即時追溯根本原因**：禁止僅修補表面症狀，必須追溯到工具鏈、架構或型別本質。
    2. **建立自動化防護腳本**：優先編寫確定性驗證腳本（如 Theme Check、Git Hook、Python Assert 管道），不靠 AI 自由心證。
    3. **自動更新 `AGENTS.md`（永久規則層）**：在任務回覆前，**AI 必須自動將本次教訓與防護門檻沉澱為永久條款，直接寫入 `AGENTS.md`**，絕不等待使用者要求。
    4. **自動更新 `SKILL.md`（操作手冊層）**：AI 必須同步將更新的操作流程與防錯禁忌寫入 `.agents/skills/<skill_name>/SKILL.md`（如 `shopify-theme-guardian` 或 `momo-package-builder`）。
    5. **透明回報已更新的 MD**：在每次解決問題的結尾，AI 必須向使用者主動列出本次已自動更新的規則檔與技能檔路徑。
    6. **跨任務與重啟繼承**：新規則一旦寫入，立即永久生效於此工作區，所有未來的 AI 對話與任務皆無條件遵循。
- **基準版本主動閉環機制 (Proactive Baseline Artifact & MD Auto-Binding)**：
  - 未來只要產出任何新的里程碑標準檔（包括但不限於：商品 CSV 主檔、主題 ZIP 發布包、MOMO 上架包）：
  - **AI 必須在交付該任務的當下，自動將新檔名、時間戳與校驗狀態沉澱至 `AGENTS.md`、`SKILL.md` 與 `CHIBA_TASK_CHECKPOINT.md`，並在回覆中以專屬區塊主動展示「已完成 MD 自動更新」**。
  - 嚴禁等待使用者開口詢問或提醒更新 MD。若使用者需要提醒 AI 更新 MD，即判定為流程缺陷並觸發本條款自我修正。




## Multi-Developer Dual-Account & Local Disk Sync Standard (雙帳號與本機磁碟同步標準規範)
- **單一真實資料來源 (Single Source of Truth)**：`archielin0725` 官方遠端倉庫為唯一主幹（Upstream）。
- **同步管線（Sync Pipeline）**：
  `archielin0725 (GitHub 主幹)` ➔ `Sammy 本地磁碟 (/Users/sammywang/)` ➔ `sammywanwan (Sammy 個人 GitHub)`
- **標準同步腳本（Deterministic Sync Script: `scripts/sync_chiba.sh`）**：
  在 Sammy 本機執行時，腳本自動拉取 `archielin0725` 最新提交至本機磁碟，並自動推送至 Sammy 個人 GitHub，實現三方（Archie 官方、Sammy 本機、Sammy GitHub）100% 同步。

## Rule Governance & Health Checkpoint Standard (MD 規則治理與健康檢查標準)
- **三層分立架構（Three-Tier Architecture）**：
  1. **憲法層（`AGENTS.md`）**：僅保留不可撼動之全域核心紅線（資料來源、價格保護、編譯門檻、同步規範）。嚴格控制在 **250 行 / 30KB** 以內，避免模型「迷失在中間（Lost in the Middle）」。
  2. **手冊層（`.agents/skills/<name>/SKILL.md`）**：模組細節（Liquid 語法、MOMO 欄位代碼、CSV 對照邏輯）拆分至專屬技能庫，由 AI 依任務按需載入。
  3. **動態進度層（`Output/CHIBA_TASK_CHECKPOINT.md`）**：記錄任務歷程、除錯紀錄與時間戳交付檔案，嚴禁混入憲法層。
- **跨 AI 工具單一橋接（Universal AI Rule Bridge）**：
  - `CLAUDE.md` 與 `.cursorrules` 必須以 Symlink 永遠指向 `AGENTS.md`，杜絕跨工具規格漂移。
  - Web AI 工具（Claude Projects、ChatGPT Custom GPTs）直接將 `AGENTS.md` 設為專案知識庫與指示基準。
- **定期健康審查防線（Deterministic MD Health Gate）**：
  - 必須定期執行 `python3 scripts/audit_md_health.py`。
  - 自動檢驗：行數上限（≤ 250 行）、大小上限（≤ 30KB）、Symlink 有效性、機密防護（零批發價與金鑰洩漏）、跨倉庫（`Chiba-AI` 與 `Chiba-Shopify`）100% 同步性。
