# KryptoGO Meme Trader

[繁體中文](README.zh-TW.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

AI-powered meme coin trading agent for Solana with multi-chain on-chain analysis.

## MCP Server

### Claude Code Quick Start

```bash
claude mcp add kryptogo-meme-trader -e KRYPTOGO_API_KEY=your_key -- uvx kryptogo-meme-trader
```

### With Trading

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

See [skill/SKILL.md](./skill/SKILL.md) for full documentation.

## Prerequisites

- API key from [kryptogo.xyz/account](https://kryptogo.xyz/account)
- Python 3.10+

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `KRYPTOGO_API_KEY` | Yes | API key from kryptogo.xyz |
| `SOLANA_PRIVATE_KEY` | No | Base58 private key for trading |
| `SOLANA_WALLET_ADDRESS` | No | Wallet address for portfolio/trading |

## Available Tools (22)

### Analysis (13)

| Tool | Description |
|------|-------------|
| `get_token_overview` | Get comprehensive token overview including price, market cap, and metadata |
| `analyze_token` | Cluster analysis — groups related wallets to reveal insider holdings (free tier: first 2 clusters only) |
| `get_cluster_trends` | Analyze smart money cluster trends and movements |
| `get_balance_history` | Track historical balance changes for a wallet |
| `get_balance_increase` | Identify wallets with significant balance increases |
| `get_top_holders_snapshot` | Get current snapshot of top token holders |
| `get_historical_top_holders` | View historical top holder data over time |
| `get_fresh_addresses` | Detect newly created wallets accumulating tokens |
| `get_dca_limit_orders` | Find DCA and limit order activity for a token |
| `get_price_chart` | Retrieve OHLCV price chart data |
| `get_batch_prices` | Get prices for multiple tokens in a single call |
| `get_cluster_connections` | Map connections between wallets in a cluster |
| `get_wallet_assets` | List all token holdings for a wallet |

### Discovery (3)

| Tool | Description |
|------|-------------|
| `get_trending_tokens` | Get currently trending tokens across chains |
| `get_signal_dashboard` | Network-wide accumulation signals — tokens where insiders are buying (Pro/Alpha only) |
| `get_signal_history` | Browse historical trading signals |

### Portfolio (2)

| Tool | Description |
|------|-------------|
| `get_account_info` | Get account info including API usage and tier |
| `get_portfolio` | View wallet portfolio with P&L tracking |

### Trading (1)

| Tool | Description |
|------|-------------|
| `swap_tokens` | Execute token swaps on Solana |

### Labels & Risk (3)

| Tool | Description |
|------|-------------|
| `get_wallet_labels` | Get labels and tags for a wallet address |
| `get_token_wallet_labels` | Get labeled wallets associated with a token |
| `check_rug_risk` | Assess rug pull risk for a token |

## Supported Chains

| Chain | chain_id | Trading |
|-------|----------|---------|
| Solana | 501 | Yes |
| BSC | 56 | Analysis only |
| Base | 8453 | Analysis only |
| Monad | 143 | Analysis only |

## Tiers

| Tier | API Calls/Day | Trading Fee | Signals |
|------|--------------|-------------|---------|
| Free | 100 | 1% | No |
| Pro | 1,000 | 0.5% | Yes |
| Alpha | 5,000 | 0% | Yes |

## Security

All transaction signing is performed locally on your machine. Your private key is never sent to KryptoGO servers or any third party. The MCP server constructs transactions locally and only submits signed transactions to the Solana RPC endpoint.

## License

MIT
