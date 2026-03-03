from mcp.server.fastmcp import Context
from kryptogo_meme_trader.app import mcp, AppContext


def _get_ctx(ctx: Context) -> AppContext:
    return ctx.request_context.lifespan_context


@mcp.tool()
async def get_wallet_labels(ctx: Context, token_address: str, wallets: list[str]) -> dict:
    """Get behavior labels for wallets — smart_money (realized profit >$100K), whale, high_frequency, blue_chip_profit. Only labeled wallets are returned.

    Args:
        token_address: Token contract address for context
        wallets: List of wallet addresses to label
    """
    app = _get_ctx(ctx)
    return await app.api.post("/wallet-labels", json={"token_mint": token_address, "wallets": wallets})


@mcp.tool()
async def get_token_wallet_labels(ctx: Context, token_address: str) -> dict:
    """Get token-specific labels for all relevant wallets — developer, sniper, bundle, new_wallet.

    Args:
        token_address: Token contract address
    """
    app = _get_ctx(ctx)
    return await app.api.post("/token-wallet-labels", json={"token_mint": token_address})


@mcp.tool()
async def check_rug_risk(ctx: Context, token_address: str) -> dict:
    """Check token for rug pull risks via RugCheck.xyz. Returns risk score and danger signals (mint authority, freeze authority, LP unlocked, low liquidity). Solana only.

    Args:
        token_address: Token mint address (Solana)
    """
    app = _get_ctx(ctx)
    try:
        data = await app.rugcheck.get(f"/tokens/{token_address}/report/summary")
    except Exception as e:
        return {"safe": True, "reason": "API_UNAVAILABLE", "error": str(e)}

    score = data.get("score", 0)
    if score > 5000:
        return {"safe": False, "reason": f"High Risk Score: {score}", "score": score, "raw": data}

    risks = data.get("risks", [])
    danger_signals = []
    for r in risks:
        if r.get("level") == "danger":
            name = r.get("name", "")
            if "Mint Authority" in name:
                danger_signals.append("Mint Authority Enabled")
            elif "Freeze Authority" in name:
                danger_signals.append("Freeze Authority Enabled")
            elif "LP Unlocked" in name:
                danger_signals.append("LP Not Locked/Burned")
            elif "Low Liquidity" in name:
                danger_signals.append("Low Liquidity")

    if danger_signals:
        return {"safe": False, "reason": f"Rug Risks: {', '.join(danger_signals)}", "score": score, "raw": data}

    return {"safe": True, "reason": "Safe", "score": score, "raw": data}
