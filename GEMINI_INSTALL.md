# gstack for Gemini CLI 安裝文檔

gstack 是一套由 Garry Tan 定義的高級技能組，旨在將 **Google Gemini CLI** 轉化為一個具備 CEO、架構師與 QA 工程師能力的虛擬開發團隊。

---

## 1. 前置需求

在安裝之前，請確保您的系統已安裝以下工具：

*   **Google Gemini CLI**: 確保已正確安裝並登入。
*   **Bun**: gstack 的瀏覽器測試工具 (`browse`) 需要 Bun 運行環境。
    *   安裝指令：`curl -fsSL https://bun.sh/install | bash`
*   **Git**: 用於版本控制與代碼追蹤。

---

## 2. 安裝步驟

### 步驟 A：建立技能目錄
Gemini CLI 預設會從 `~/.gemini/skills` 讀取自定義技能。

```bash
# 建立目錄路徑
mkdir -p ~/.gemini/skills/gstack
```

### 步驟 B：將轉換後的檔案移至目標位置
如果您已經在本地轉換好檔案，請將它們複製到上述目錄；或者直接在該目錄下進行操作：

```bash
# 假設您目前的目錄是轉換後的 gstack_port
cp -r * ~/.gemini/skills/gstack/
```

### 步驟 C：執行 Setup 腳本
gstack 需要編譯其內部的 browse 二進位檔案並配置環境。

```bash
cd ~/.gemini/skills/gstack
chmod +x setup
./setup
```

> **注意 (Windows 用戶)**: 如果您使用 Git Bash 或 WSL，請確保在 Unix 模擬環境下執行。如果是原生 Windows 環境，請確保 `bun` 已加入環境變數。

---

## 3. 配置 Gemini CLI

為了讓 Gemini CLI 識別這些技能，您可能需要確保路徑正確。Gemini CLI 會自動掃描 `~/.gemini/skills` 下的 `SKILL.md` 檔案。

您可以使用以下指令檢查配置：

```bash
# 檢查目前載入的技能 (視您的 Gemini CLI 版本而定)
gemini skills list
```

---

## 4. 如何使用

安裝完成後，您可以在 Gemini CLI 會話中直接透過描述或指令調用以下功能：

| 功能指令 | 角色 / 用途 |
| :--- | :--- |
| `/plan-ceo-review` | **CEO 模式**：審查產品策略、挑戰產品願景、擴張或精簡範疇。 |
| `/plan-eng-review` | **工程師模式**：分析系統架構、繪製數據流圖、檢查錯誤處理。 |
| `/qa` | **QA 模式**：啟動無頭瀏覽器測試 UI、發現 Bug 並自動修復。 |
| `/review` | **代碼審查**：以嚴苛的 Staff Engineer 角度進行安全性與邏輯審查。 |
| `/investigate` | **深度調查**：追蹤複雜 Bug 的根本原因。 |
| `/ship` | **發佈模式**：準備 PR、執行最後測試、自動化發佈流程。 |

---

## 5. 重要變更說明 (Gemini CLI 版)

與原始 `garrytan/gstack` (Claude Code 版) 的不同點：

1.  **路徑變更**：所有設定與二進位檔案現在位於 `~/.gemini/skills/gstack`。
2.  **工具適配**：原本的 `Bash`, `Read`, `Edit` 指令已適配為 Gemini CLI 的 `run_shell_command`, `read_file`, `replace`。
3.  **長文本優化**：技能指令已針對 Gemini 的 1M+ Token Context 進行調整，Agent 會傾向於讀取更多專案脈絡（如 `ARCHITECTURE.md`）來做出決策。

---

## 故障排除

*   **瀏覽器無法啟動**：請確認 `~/.gemini/skills/gstack/browse/dist/browse` 是否具備執行權限。
*   **找不到技能**：請確認 `SKILL.md` 位於 `~/.gemini/skills/gstack/` 的第一層目錄中。
*   **路徑衝突**：如果您同時安裝了 Claude Code，請注意兩者現在使用獨立的配置路徑，互不干擾。
