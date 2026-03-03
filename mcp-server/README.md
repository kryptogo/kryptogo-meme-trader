# KryptoGO Meme Trader MCP Server

MCP server for Solana meme coin analysis and trading powered by [KryptoGO](https://kryptogo.xyz).

## Quick Start

### Claude Code

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

Add to your config file:

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
| `analyze_token` | Deep analysis of a token with holder distribution, trading activity, and risk signals |
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
| `get_signal_dashboard` | View real-time trading signals dashboard |
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
| Free | 50 | 1% | No |
| Pro | 500 | 0.5% | Yes |
| Alpha | 5,000 | 0% | Yes |

## Security

All transaction signing is performed locally on your machine. Your private key is never sent to KryptoGO servers or any third party.

## License

MIT
