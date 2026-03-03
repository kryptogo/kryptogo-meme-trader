import httpx
from kryptogo_meme_trader.config import API_BASE, API_KEY


class KryptoGoClient:
    """Async HTTP client for KryptoGO API."""

    def __init__(self):
        self._client: httpx.AsyncClient | None = None

    async def _get_client(self) -> httpx.AsyncClient:
        if self._client is None or self._client.is_closed:
            self._client = httpx.AsyncClient(
                base_url=API_BASE,
                headers={
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json",
                },
                timeout=30.0,
            )
        return self._client

    async def get(self, path: str, **kwargs) -> dict:
        client = await self._get_client()
        resp = await client.get(path, **kwargs)
        resp.raise_for_status()
        return resp.json()

    async def post(self, path: str, **kwargs) -> dict:
        client = await self._get_client()
        resp = await client.post(path, **kwargs)
        resp.raise_for_status()
        return resp.json()

    async def close(self):
        if self._client and not self._client.is_closed:
            await self._client.close()


class RugCheckClient:
    """Async HTTP client for RugCheck.xyz API (no auth)."""

    def __init__(self):
        self._client: httpx.AsyncClient | None = None

    async def _get_client(self) -> httpx.AsyncClient:
        if self._client is None or self._client.is_closed:
            self._client = httpx.AsyncClient(
                base_url="https://api.rugcheck.xyz/v1",
                timeout=5.0,
            )
        return self._client

    async def get(self, path: str, **kwargs) -> dict:
        client = await self._get_client()
        resp = await client.get(path, **kwargs)
        resp.raise_for_status()
        return resp.json()

    async def close(self):
        if self._client and not self._client.is_closed:
            await self._client.close()
