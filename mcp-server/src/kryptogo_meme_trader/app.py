from dataclasses import dataclass
from contextlib import asynccontextmanager
from mcp.server.fastmcp import FastMCP
from kryptogo_meme_trader.api_client import KryptoGoClient, RugCheckClient


@dataclass
class AppContext:
    api: KryptoGoClient
    rugcheck: RugCheckClient


@asynccontextmanager
async def app_lifespan(server: FastMCP):
    api = KryptoGoClient()
    rugcheck = RugCheckClient()
    try:
        yield AppContext(api=api, rugcheck=rugcheck)
    finally:
        await api.close()
        await rugcheck.close()


mcp = FastMCP(
    "kryptogo-meme-trader",
    lifespan=app_lifespan,
)
