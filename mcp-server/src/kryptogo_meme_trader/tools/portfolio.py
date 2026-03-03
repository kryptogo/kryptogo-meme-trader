from mcp.server.fastmcp import Context
from kryptogo_meme_trader.app import mcp, AppContext
from kryptogo_meme_trader.config import SOLANA_WALLET_ADDRESS


def _get_ctx(ctx: Context) -> AppContext:
    return ctx.session.server.lifespan_context


@mcp.tool()
async def get_account_info(ctx: Context) -> dict:
    """Check your KryptoGO account subscription tier and API usage quota. This call does not count toward your daily limit.

    Returns tier (free/pro/alpha), daily_limit, daily_calls_used, daily_calls_remaining.
    """
    app = _get_ctx(ctx)
    return await app.api.get("/agent/account")


@mcp.tool()
async def get_portfolio(ctx: Context, wallet_address: str = "") -> dict:
    """Get wallet portfolio — SOL balance, token holdings with USD values, and per-token PnL (realized, unrealized, total).

    Args:
        wallet_address: Wallet to query. Defaults to the configured SOLANA_WALLET_ADDRESS if omitted.
    """
    app = _get_ctx(ctx)
    addr = wallet_address or SOLANA_WALLET_ADDRESS
    params = {}
    if addr:
        params["wallet_address"] = addr
    return await app.api.get("/agent/portfolio", params=params)
