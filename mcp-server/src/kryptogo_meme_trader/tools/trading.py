import base64
from decimal import Decimal, getcontext
from mcp.server.fastmcp import Context
from kryptogo_meme_trader.app import mcp, AppContext
from kryptogo_meme_trader.config import SOLANA_WALLET_ADDRESS, SOLANA_PRIVATE_KEY, SOL_MINT

getcontext().prec = 28


def _get_ctx(ctx: Context) -> AppContext:
    return ctx.request_context.lifespan_context


@mcp.tool()
async def swap_tokens(
    ctx: Context,
    token_address: str,
    amount: str,
    sell: bool = False,
    slippage_bps: int = 500,
    max_price_impact: float = 10.0,
) -> dict:
    """Buy or sell tokens on Solana via DEX aggregator. Transaction is signed locally — private key never leaves your machine.

    Requires SOLANA_PRIVATE_KEY and SOLANA_WALLET_ADDRESS environment variables.

    Args:
        token_address: Token mint address to buy or sell
        amount: Amount in SOL (for buy) or token units (for sell). String to preserve precision.
        sell: If True, sell tokens back to SOL. Default is buy.
        slippage_bps: Slippage tolerance in basis points (default 500 = 5%)
        max_price_impact: Max price impact percentage before aborting (default 10%)
    """
    if not SOLANA_PRIVATE_KEY or not SOLANA_WALLET_ADDRESS:
        return {"error": "Trading requires SOLANA_PRIVATE_KEY and SOLANA_WALLET_ADDRESS environment variables."}

    app = _get_ctx(ctx)
    amount_dec = Decimal(amount)

    # Get token info for decimals
    token_info = {}
    try:
        token_info = await app.api.get("/token-overview", params={"address": token_address})
    except Exception:
        pass

    decimals = token_info.get("decimals")
    token_symbol = token_info.get("symbol", "UNKNOWN")

    if sell:
        if decimals is None:
            return {"error": "Cannot determine token decimals. Refusing to sell with unknown precision."}
        input_mint = token_address
        output_mint = SOL_MINT
        amount_raw = int(amount_dec * (Decimal(10) ** decimals))
    else:
        input_mint = SOL_MINT
        output_mint = token_address
        amount_raw = int(amount_dec * Decimal(1_000_000_000))

    # Step 1: Build unsigned transaction
    swap_data = await app.api.post("/agent/swap", json={
        "input_mint": input_mint,
        "output_mint": output_mint,
        "amount": amount_raw,
        "slippage_bps": slippage_bps,
        "wallet_address": SOLANA_WALLET_ADDRESS,
    })

    fee_payer = swap_data.get("fee_payer")
    price_impact = float(swap_data.get("quote", {}).get("price_impact_pct", 0))

    if fee_payer and fee_payer != SOLANA_WALLET_ADDRESS:
        return {"error": f"Fee payer mismatch. Expected {SOLANA_WALLET_ADDRESS}, got {fee_payer}"}

    if abs(price_impact) > max_price_impact:
        return {"error": f"Price impact {price_impact}% exceeds max {max_price_impact}%"}

    # Step 2: Sign locally
    try:
        from solders.keypair import Keypair
        from solders.transaction import VersionedTransaction
    except ImportError:
        return {"error": "solders package not installed. Install with: pip install 'kryptogo-meme-trader[trading]'"}

    tx_bytes = base64.b64decode(swap_data["transaction"])
    tx = VersionedTransaction.from_bytes(tx_bytes)
    keypair = Keypair.from_base58_string(SOLANA_PRIVATE_KEY)
    signed_tx = VersionedTransaction(tx.message, [keypair])
    signed_tx_b64 = base64.b64encode(bytes(signed_tx)).decode()

    # Step 3: Submit
    result = await app.api.post("/agent/submit", json={"signed_transaction": signed_tx_b64})

    tx_hash = result.get("tx_hash", result.get("signature", ""))
    action = "SELL" if sell else "BUY"
    return {
        "action": action,
        "token": token_symbol,
        "token_address": token_address,
        "amount": amount,
        "tx_hash": tx_hash,
        "status": result.get("status", "submitted"),
        "explorer_url": f"https://solscan.io/tx/{tx_hash}",
        "price_impact": price_impact,
        "quote": swap_data.get("quote"),
    }
