import sys

from kryptogo_meme_trader.app import mcp

# Import tool modules to trigger @mcp.tool() registration
import kryptogo_meme_trader.tools  # noqa: F401


def main():
    if sys.platform == "win32":
        import asyncio
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    mcp.run()


if __name__ == "__main__":
    main()
