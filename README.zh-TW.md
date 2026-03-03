# KryptoGO Meme Trader

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

**迷因幣的上帝之眼** — 全網首家全維度鏈上輔助交易工具。

聰明錢追蹤 · 莊家分析 · 巨鯨監控 · 訊號預警

## 為什麼選擇 KryptoGO

| 能力 | 說明 | 工具 |
|---|---|---|
| **獨家集群偵測** | 精準偵測所有持倉地址中的莊家集群，主力資金是在吸籌還是出貨，一目了然 | `analyze_token` |
| **集群持倉趨勢** | 價格橫盤 + 集群持倉上升 = 吸籌（看漲）。價格上漲 + 集群持倉下降 = 出貨（看跌） | `get_cluster_trends` |
| **隱藏持倉還原** | 精準還原 Jupiter 限價單、DCA 分時買入等隱藏持倉——其他工具顯示已清倉，我們能看到莊家真實籌碼仍在手上 | `get_dca_limit_orders` |
| **全網吸籌信號** | 一段吸籌捕捉新幣快速吸籌、二段吸籌捕捉成熟幣再次吸籌階段，精準掌握主力動向 | `get_signal_dashboard` |
| **多維度地址標籤** | 涵蓋聰明錢、藍籌高盈利、巨鯨、DEV、狙擊手、捆綁交易等，標籤數量遠超 Nansen | `get_token_wallet_labels` |

### 看懂主力操盤

透過集群持倉變化，識別莊家操盤三大階段：

| 階段 | 價格走勢 | 集群持倉 | 訊號 |
|---|---|---|---|
| **吸籌** | 橫盤整理 | 持續上升 | 看漲——主力悄悄收集籌碼 |
| **拉盤** | 快速拉升 | 維持高位 | 持有——主力尚未出手 |
| **出貨** | 仍在高位 | 開始下降 | 離場——主力正在派發給追高散戶 |

> *人也許會說謊，但鏈上數據不會。*

## 前置需求

- 從 [kryptogo.xyz/account](https://kryptogo.xyz/account) 取得 API 金鑰
- Python 3.10+

## Skill

### OpenClaw

```bash
npx clawhub install kryptogo-meme-trader
```

### Claude Code

```bash
npx degit kryptogo/kryptogo-meme-trader/skill ~/.claude/skills/kryptogo-meme-trader
```

安裝後請重啟 Claude Code 以啟用。完整文件請參閱 [skill/SKILL.md](./skill/SKILL.md)。

## MCP 伺服器

### Claude Code 快速開始

```bash
claude mcp add kryptogo-meme-trader -e KRYPTOGO_API_KEY=your_key -- uvx kryptogo-meme-trader
```

### 啟用交易功能

```bash
claude mcp add kryptogo-meme-trader \
  -e KRYPTOGO_API_KEY=your_key \
  -e SOLANA_PRIVATE_KEY=your_base58_key \
  -e SOLANA_WALLET_ADDRESS=your_wallet \
  -- uvx kryptogo-meme-trader
```

### Claude Desktop / Cursor / Windsurf

```json
{
  "mcpServers": {
    "kryptogo-meme-trader": {
      "command": "uvx",
      "args": ["kryptogo-meme-trader"],
      "env": {
        "KRYPTOGO_API_KEY": "your_key"
      }
    }
  }
}
```

## 文件

| | English | 繁體中文 | 简体中文 |
|---|---|---|---|
| 產品指南 | [User Guide](https://kryptogo.notion.site/Product-Guide-EN-26c3499de8a28179aafacb68304458ea) | [使用手冊](https://kryptogo.notion.site/kryptogo-xyz-usage-guide) | [使用手册](https://kryptogo.notion.site/kryptogo-xyz-productguide-zhcn) |
| 白皮書 | [PDF](https://wallet-static.kryptogo.com/public/whitepaper/kryptogo-xyz-whitepaper-v1.0.pdf) | [白皮書](https://kryptogo.xyz/whitepaper) | [白皮书](https://kryptogo.xyz/whitepaper) |

## 環境變數

| 變數 | 必填 | 說明 |
|------|------|------|
| `KRYPTOGO_API_KEY` | 是 | 從 kryptogo.xyz 取得的 API 金鑰 |
| `SOLANA_PRIVATE_KEY` | 否 | 用於交易的 Base58 私鑰 |
| `SOLANA_WALLET_ADDRESS` | 否 | 用於投資組合/交易的錢包地址 |

## 可用工具 (22)

### 分析 (13)

| 工具 | 說明 |
|------|------|
| `get_token_overview` | 取得代幣綜合概覽，包含價格、市值及元資料 |
| `analyze_token` | 集群分析 — 將關聯錢包分組以揭示內部持倉（免費版僅顯示前 2 個集群） |
| `get_cluster_trends` | 分析聰明錢集群趨勢與動向 |
| `get_balance_history` | 追蹤錢包的歷史餘額變化 |
| `get_balance_increase` | 識別餘額大幅增加的錢包 |
| `get_top_holders_snapshot` | 取得代幣前幾大持有者的當前快照 |
| `get_historical_top_holders` | 查看歷史前幾大持有者資料的時間變化 |
| `get_fresh_addresses` | 偵測正在累積代幣的新建錢包 |
| `get_dca_limit_orders` | 查詢代幣的定投與限價單活動 |
| `get_price_chart` | 取得 OHLCV 價格圖表資料 |
| `get_batch_prices` | 單次呼叫取得多個代幣價格 |
| `get_cluster_connections` | 繪製集群中錢包之間的連結關係 |
| `get_wallet_assets` | 列出錢包的所有代幣持有 |

### 發現 (3)

| 工具 | 說明 |
|------|------|
| `get_trending_tokens` | 取得跨鏈當前熱門代幣 |
| `get_signal_dashboard` | 全網吸籌訊號 — 內部人正在買入的代幣（僅限 Pro/Alpha） |
| `get_signal_history` | 取得代幣過去發送的訊號 |

### 投資組合 (2)

| 工具 | 說明 |
|------|------|
| `get_account_info` | 取得帳戶資訊，包含 API 使用量與方案等級 |
| `get_portfolio` | 查看錢包投資組合及損益追蹤 |

### 交易 (1)

| 工具 | 說明 |
|------|------|
| `swap_tokens` | 在 Solana 上執行代幣交換 |

### 標籤與風險 (3)

| 工具 | 說明 |
|------|------|
| `get_wallet_labels` | 取得錢包地址的標籤與標記 |
| `get_token_wallet_labels` | 取得與代幣相關的已標記錢包 |
| `check_rug_risk` | 評估代幣的 Rug Pull 風險 |

## 支援鏈

| 區塊鏈 | chain_id | 交易 |
|---------|----------|------|
| Solana | 501 | 支援 |
| BSC | 56 | 僅分析 |
| Base | 8453 | 僅分析 |
| Monad | 143 | 僅分析 |

## 方案等級

| 等級 | 每日 API 呼叫數 | 交易手續費 | 訊號 |
|------|-----------------|------------|------|
| Free | 100 | 1% | 無 |
| Pro | 1,000 | 0.5% | 有 |
| Alpha | 5,000 | 0% | 有 |

## 安全性

所有交易簽署皆在您的本機上執行。您的私鑰絕不會傳送至 KryptoGO 伺服器或任何第三方。MCP 伺服器在本地建構交易，僅將已簽署的交易提交至 Solana RPC 端點。

## 授權條款

MIT
