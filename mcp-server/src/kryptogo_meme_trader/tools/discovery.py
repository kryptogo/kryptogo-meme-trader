from mcp.server.fastmcp import Context
from kryptogo_meme_trader.app import mcp, AppContext


def _get_ctx(ctx: Context) -> AppContext:
    return ctx.session.server.lifespan_context


@mcp.tool()
async def get_trending_tokens(
    ctx: Context,
    chain_id: str = "501",
    sort_by: int = 5,
    period: int = 2,
    page_size: int = 20,
    page: int = 1,
    market_cap_min: int | None = None,
    market_cap_max: int | None = None,
    holders_min: int | None = None,
    holders_max: int | None = None,
    liquidity_min: int | None = None,
    liquidity_max: int | None = None,
    volume_min: int | None = None,
    volume_max: int | None = None,
    token_age_min: int | None = None,
    token_age_max: int | None = None,
    token_age_type: int | None = None,
) -> dict:
    """Scan trending tokens by volume, market cap, holders, etc. Same data as KryptoGO xyz discovery page.

    Args:
        chain_id: Chain filter — "501" (Solana), "56" (BSC), "8453" (Base), "143" (Monad), or comma-separated
        sort_by: Sort field — 1=market cap, 2=holders, 3=liquidity, 4=tx count, 5=volume, 6=price change
        period: Time window — 1=5min, 2=1h, 3=4h, 4=24h
        page_size: Results per page (max 50, free tier limited to 10)
        page: Page number
        market_cap_min: Min market cap USD filter
        market_cap_max: Max market cap USD filter
        holders_min: Min holder count filter
        holders_max: Max holder count filter
        liquidity_min: Min liquidity USD filter
        liquidity_max: Max liquidity USD filter
        volume_min: Min volume USD filter
        volume_max: Max volume USD filter
        token_age_min: Min token age value
        token_age_max: Max token age value
        token_age_type: Age unit — 1=min, 2=hour, 3=day, 4=month, 5=year
    """
    app = _get_ctx(ctx)
    params: dict = {
        "chain_id": chain_id, "sort_by": sort_by, "period": period,
        "page_size": page_size, "page": page,
    }
    for key, val in [
        ("marketCapMin", market_cap_min), ("marketCapMax", market_cap_max),
        ("holdersMin", holders_min), ("holdersMax", holders_max),
        ("liquidityMin", liquidity_min), ("liquidityMax", liquidity_max),
        ("volumeMin", volume_min), ("volumeMax", volume_max),
        ("tokenAgeMin", token_age_min), ("tokenAgeMax", token_age_max),
        ("tokenAgeType", token_age_type),
    ]:
        if val is not None:
            params[key] = val
    return await app.api.get("/agent/trending-tokens", params=params)


@mcp.tool()
async def get_signal_dashboard(ctx: Context) -> dict:
    """Network-wide accumulation signals (most recent ~100). Shows tokens where insiders are accumulating. Requires Pro or Alpha tier.

    Returns signals with pattern type (first_stage = early/rapid, second_stage = stable/confirmed),
    price at signal time, current price, max price after signal, and cluster ratio changes.
    """
    app = _get_ctx(ctx)
    return await app.api.get("/signal-dashboard")


@mcp.tool()
async def get_signal_history(ctx: Context, token_address: str) -> dict:
    """Historical accumulation signals for a specific token. Useful for backtesting signal quality.

    Args:
        token_address: Token contract address
    """
    app = _get_ctx(ctx)
    return await app.api.get(f"/signal-history/{token_address}")
