import asyncio

from valopy import Client, ValoPyNotFoundError, ValoPyPermissionError, ValoPyRateLimitError, ValoPyHTTPError


async def safe_fetch_account():
    async with Client(api_key="your-api-key") as client:
        try:
            account = await client.get_account_v1("PlayerName", "TAG")
            print(f"Found: {account.name}#{account.tag}")

        except ValoPyNotFoundError:
            print("Account not found!")

        except ValoPyPermissionError:
            print("Invalid API key or insufficient permissions")

        except ValoPyRateLimitError as e:
            print(f"Rate limit exceeded: {e.rate_remain}/{e.rate_limit}")
            print(f"Retry after: {e.rate_reset} seconds")

        except ValoPyHTTPError as e:
            print(f"HTTP Error {e.status_code}: {e.message}")

asyncio.run(safe_fetch_account())
