import asyncio

from valopy import (
    Client,
    ValoPyNotFoundError,
    ValoPyPermissionError,
    ValoPyRateLimitError,
    ValoPyRequestError,
)


async def main() -> None:
    async with Client(api_key="your-api-key") as client:
        # Handle common API errors gracefully.
        try:
            account = await client.get_account_v2_by_puuid(puuid="some-puuid-string")
            print(f"Found: {account.name}#{account.tag}")

        except ValoPyRequestError as e:
            print(f"Request error: {e.message}")
        except ValoPyNotFoundError:
            print("Account not found")

        except ValoPyPermissionError:
            print("Invalid API key")

        except ValoPyRateLimitError as e:
            print(f"Rate limited. Retry after {e.rate_reset}s")


if __name__ == "__main__":
    asyncio.run(main())
