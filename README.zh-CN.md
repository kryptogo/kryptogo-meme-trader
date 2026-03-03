# KryptoGO Meme Trader

[English](README.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md)

**迷因币的上帝之眼** — 全网首家全维度链上辅助交易工具。

聪明钱追踪 · 庄家分析 · 巨鲸监控 · 信号预警

## 为什么选择 KryptoGO

| 能力 | 说明 | 工具 |
|---|---|---|
| **独家集群检测** | 精准检测所有持仓地址中的庄家集群，主力资金是在吸筹还是出货，一目了然 | `analyze_token` |
| **集群持仓趋势** | 价格横盘 + 集群持仓上升 = 吸筹（看涨）。价格上涨 + 集群持仓下降 = 出货（看跌） | `get_cluster_trends` |
| **隐藏持仓还原** | 精准还原 Jupiter 限价单、DCA 分时买入等隐藏持仓——其他工具显示已清仓，我们能看到庄家真实筹码仍在手上 | `get_dca_limit_orders` |
| **全网吸筹信号** | 一段吸筹捕捉新币快速吸筹、二段吸筹捕捉成熟币再次吸筹阶段，精准掌握主力动向 | `get_signal_dashboard` |
| **多维度地址标签** | 涵盖聪明钱、蓝筹高盈利、巨鲸、DEV、狙击手、捆绑交易等，标签数量远超 Nansen | `get_token_wallet_labels` |

### 看懂主力操盘

通过集群持仓变化，识别庄家操盘三大阶段：

| 阶段 | 价格走势 | 集群持仓 | 信号 |
|---|---|---|---|
| **吸筹** | 横盘整理 | 持续上升 | 看涨——主力悄悄收集筹码 |
| **拉盘** | 快速拉升 | 维持高位 | 持有——主力尚未出手 |
| **出货** | 仍在高位 | 开始下降 | 离场——主力正在派发给追高散户 |

> *人也许会说谎，但链上数据不会。*

## MCP 服务器

### Claude Code 快速开始

```bash
claude mcp add kryptogo-meme-trader -e KRYPTOGO_API_KEY=your_key -- uvx kryptogo-meme-trader
```

### 启用交易功能

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

## Claude Code Skill

```bash
npx clawhub install kryptogo-meme-trader
```

完整文档请参阅 [skill/SKILL.md](./skill/SKILL.md)。

## 文档

| | English | 繁體中文 | 简体中文 |
|---|---|---|---|
| 产品指南 | [User Guide](https://kryptogo.notion.site/Product-Guide-EN-26c3499de8a28179aafacb68304458ea) | [使用手冊](https://kryptogo.notion.site/kryptogo-xyz-usage-guide) | [使用手册](https://kryptogo.notion.site/kryptogo-xyz-productguide-zhcn) |
| 白皮书 | [PDF](https://wallet-static.kryptogo.com/public/whitepaper/kryptogo-xyz-whitepaper-v1.0.pdf) | [白皮書](https://kryptogo.xyz/whitepaper) | [白皮书](https://kryptogo.xyz/whitepaper) |

## 前置要求

- 从 [kryptogo.xyz/account](https://kryptogo.xyz/account) 获取 API 密钥
- Python 3.10+

## 环境变量

| 变量 | 必填 | 说明 |
|------|------|------|
| `KRYPTOGO_API_KEY` | 是 | 从 kryptogo.xyz 获取的 API 密钥 |
| `SOLANA_PRIVATE_KEY` | 否 | 用于交易的 Base58 私钥 |
| `SOLANA_WALLET_ADDRESS` | 否 | 用于投资组合/交易的钱包地址 |

## 可用工具 (22)

### 分析 (13)

| 工具 | 说明 |
|------|------|
| `get_token_overview` | 获取代币综合概览，包含价格、市值及元数据 |
| `analyze_token` | 集群分析 — 将关联钱包分组以揭示内部持仓（免费版仅显示前 2 个集群） |
| `get_cluster_trends` | 分析聪明钱集群趋势与动向 |
| `get_balance_history` | 追踪钱包的历史余额变化 |
| `get_balance_increase` | 识别余额大幅增加的钱包 |
| `get_top_holders_snapshot` | 获取代币前几大持有者的当前快照 |
| `get_historical_top_holders` | 查看历史前几大持有者数据的时间变化 |
| `get_fresh_addresses` | 检测正在累积代币的新建钱包 |
| `get_dca_limit_orders` | 查询代币的定投与限价单活动 |
| `get_price_chart` | 获取 OHLCV 价格图表数据 |
| `get_batch_prices` | 单次调用获取多个代币价格 |
| `get_cluster_connections` | 绘制集群中钱包之间的连接关系 |
| `get_wallet_assets` | 列出钱包的所有代币持有 |

### 发现 (3)

| 工具 | 说明 |
|------|------|
| `get_trending_tokens` | 获取跨链当前热门代币 |
| `get_signal_dashboard` | 全网累积信号 — 内部人正在买入的代币（仅限 Pro/Alpha） |
| `get_signal_history` | 浏览历史交易信号 |

### 投资组合 (2)

| 工具 | 说明 |
|------|------|
| `get_account_info` | 获取账户信息，包含 API 使用量与方案等级 |
| `get_portfolio` | 查看钱包投资组合及盈亏追踪 |

### 交易 (1)

| 工具 | 说明 |
|------|------|
| `swap_tokens` | 在 Solana 上执行代币交换 |

### 标签与风险 (3)

| 工具 | 说明 |
|------|------|
| `get_wallet_labels` | 获取钱包地址的标签与标记 |
| `get_token_wallet_labels` | 获取与代币相关的已标记钱包 |
| `check_rug_risk` | 评估代币的 Rug Pull 风险 |

## 支持链

| 区块链 | chain_id | 交易 |
|--------|----------|------|
| Solana | 501 | 支持 |
| BSC | 56 | 仅分析 |
| Base | 8453 | 仅分析 |
| Monad | 143 | 仅分析 |

## 方案等级

| 等级 | 每日 API 调用数 | 交易手续费 | 信号 |
|------|-----------------|------------|------|
| Free | 100 | 1% | 无 |
| Pro | 1,000 | 0.5% | 有 |
| Alpha | 5,000 | 0% | 有 |

## 安全性

所有交易签名均在您的本地计算机上执行。您的私钥绝不会发送至 KryptoGO 服务器或任何第三方。MCP 服务器在本地构建交易，仅将已签名的交易提交至 Solana RPC 端点。

## 许可证

MIT
