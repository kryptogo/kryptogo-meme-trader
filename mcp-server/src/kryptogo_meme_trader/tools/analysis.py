from mcp.server.fastmcp import Context
from kryptogo_meme_trader.app import mcp, AppContext


def _get_ctx(ctx: Context) -> AppContext:
    return ctx.session.server.lifespan_context


@mcp.tool()
async def get_token_overview(ctx: Context, token_address: str, chain_id: int = 501) -> dict:
    """Get token metadata and market data (price, market cap, holders, liquidity, volume, risk level).

    Args:
        token_address: Token contract address (mint for Solana, 0x for EVM)
        chain_id: Chain ID — 501 (Solana), 56 (BSC), 8453 (Base), 143 (Monad)
    """
    app = _get_ctx(ctx)
    return await app.api.get("/token-overview", params={"address": token_address, "chain_id": chain_id})


@mcp.tool()
async def analyze_token(ctx: Context, token_address: str, chain_id: int = 501) -> dict:
    """Full cluster analysis for a token — groups related wallets, shows insider holdings, market maker positions, and top holders.

    Args:
        token_address: Token contract address
        chain_id: Chain ID — 501 (Solana), 56 (BSC), 8453 (Base), 143 (Monad)
    """
    app = _get_ctx(ctx)
    return await app.api.get(f"/analyze/{token_address}", params={"chain_id": chain_id})


@mcp.tool()
async def get_cluster_trends(ctx: Context, token_address: str, chain_id: int = 501, include_top_holders: bool = True) -> dict:
    """Get cluster holding ratio and change trends across 15m/1h/4h/1d/7d periods. Positive change = accumulating, negative = distributing.

    Args:
        token_address: Token contract address
        chain_id: Chain ID
        include_top_holders: Also return top holder ratio trends
    """
    app = _get_ctx(ctx)
    return await app.api.get(
        f"/analyze-cluster-change/{token_address}",
        params={"chain_id": chain_id, "include_top_holders": str(include_top_holders).lower()},
    )


@mcp.tool()
async def get_balance_history(ctx: Context, token_address: str, wallets: list[str], after: int, bar: str = "1H", limit: int = 100, chain_id: int = 501) -> dict:
    """Time-series balance data for specific wallets on a token.

    Args:
        token_address: Token contract address
        wallets: List of wallet addresses to track
        after: Unix timestamp to start from
        bar: Interval — 1m, 5m, 15m, 1H, 4H, 1D (tier restrictions apply)
        limit: Number of data points (1-1000)
        chain_id: Chain ID
    """
    app = _get_ctx(ctx)
    return await app.api.post("/balance-history", json={
        "token": token_address, "wallets": wallets, "after": after,
        "bar": bar, "limit": limit, "chain_id": chain_id,
    })


@mcp.tool()
async def get_balance_increase(ctx: Context, token_address: str, from_ts: int, to_ts: int, chain_id: int = 501) -> dict:
    """Find wallets that accumulated the most tokens in a time range. Useful for detecting pre-pump accumulation.

    Args:
        token_address: Token contract address
        from_ts: Unix timestamp range start
        to_ts: Unix timestamp range end
        chain_id: Chain ID
    """
    app = _get_ctx(ctx)
    return await app.api.get(
        f"/balance-increase/{token_address}",
        params={"from": from_ts, "to": to_ts, "chain_id": chain_id},
    )


@mcp.tool()
async def get_top_holders_snapshot(ctx: Context, token_address: str, timestamp: int, chain_id: int = 501) -> dict:
    """Point-in-time top holder snapshot (up to 1000 holders). Compare before/after events.

    Args:
        token_address: Token contract address
        timestamp: Unix timestamp for the snapshot
        chain_id: Chain ID
    """
    app = _get_ctx(ctx)
    return await app.api.get(
        f"/top-holders-snapshot/{token_address}",
        params={"timestamp": timestamp, "chain_id": chain_id},
    )


@mcp.tool()
async def get_historical_top_holders(ctx: Context, token_address: str, chain_id: int = 501) -> dict:
    """Addresses that held the most at ANY point in history (historical max balance vs current).

    Args:
        token_address: Token contract address
        chain_id: Chain ID
    """
    app = _get_ctx(ctx)
    return await app.api.get(f"/historical-top-holders/{token_address}", params={"chain_id": chain_id})


@mcp.tool()
async def get_fresh_addresses(ctx: Context, token_address: str) -> dict:
    """New wallet addresses holding a token (Solana only).

    Args:
        token_address: Token mint address
    """
    app = _get_ctx(ctx)
    return await app.api.get(f"/fresh-addresses/{token_address}")


@mcp.tool()
async def get_dca_limit_orders(ctx: Context, token_address: str) -> dict:
    """Detect DCA (dollar-cost averaging) and limit order usage by holders. Large DCA positions may indicate stealth accumulation. Solana only.

    Args:
        token_address: Token mint address
    """
    app = _get_ctx(ctx)
    return await app.api.get(f"/analyze-dca-limit-orders/{token_address}")


@mcp.tool()
async def get_price_chart(ctx: Context, token_address: str, after: int, bar: str = "1H", limit: int = 100) -> dict:
    """OHLCV price candlestick data. Returns arrays of [timestamp, open, high, low, close, volume, volumeUsd, confirm].

    Args:
        token_address: Token contract address
        after: Unix timestamp to start from
        bar: Interval — 1m, 5m, 15m, 1H, 4H, 1D
        limit: Number of candles (1-1000)
    """
    app = _get_ctx(ctx)
    return await app.api.get("/price-chart", params={
        "token": token_address, "after": after, "bar": bar, "limit": limit,
    })


@mcp.tool()
async def get_batch_prices(ctx: Context, token_mints: list[str]) -> dict:
    """Batch price lookup for multiple tokens. Returns prices in USD.

    Args:
        token_mints: List of token contract addresses
    """
    app = _get_ctx(ctx)
    return await app.api.post("/batch-token-prices", json={"token_mints": token_mints})


@mcp.tool()
async def get_cluster_connections(ctx: Context, token_address: str, wallets: list[str]) -> dict:
    """Get fund flow connections between wallets within a cluster — reveals WHY wallets were grouped together.

    Args:
        token_address: Token contract address
        wallets: List of wallet addresses to check connections for
    """
    app = _get_ctx(ctx)
    return await app.api.post("/cluster-wallet-connections", json={
        "token_mint": token_address, "wallets": wallets,
    })


@mcp.tool()
async def get_wallet_assets(ctx: Context, wallet_address: str, chain_id: int = 501) -> dict:
    """Get a wallet's complete token holdings with balances and USD values.

    Args:
        wallet_address: Wallet address to inspect
        chain_id: Chain ID
    """
    app = _get_ctx(ctx)
    return await app.api.get("/wallet-assets", params={"address": wallet_address, "chain_id": chain_id})
