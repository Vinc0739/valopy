import asyncio
from valopy import Client, ValoPyHTTPError, ValoPyRateLimitError


async def fetch_with_retry(client, max_retries=3):
    """Fetch account with retry logic."""
    retry_count = 0
    base_delay = 1

    while retry_count < max_retries:
        try:
            account = await client.get_account_v1("PlayerName", "TAG")
            return account

        except ValoPyRateLimitError:
            retry_count += 1
            if retry_count >= max_retries:
                print("Max retries reached")
                raise

            delay = base_delay * (2**retry_count)
            print(f"Rate limited. Retrying in {delay}s...")
            await asyncio.sleep(delay)

        except ValoPyHTTPError as e:
            print(f"HTTP Error: {e.status_code} - {e.message}")
            raise


async def main():
    async with Client(api_key="your-api-key") as client:
        try:
            account = await fetch_with_retry(client)
            print(f"Success: {account.name}#{account.tag}")  # type: ignore
        except Exception as e:
            print(f"Failed: {e}")


asyncio.run(main())
