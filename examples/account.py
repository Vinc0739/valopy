"Get account information by name and tag."

import asyncio

from valopy import Client


async def main() -> None:
    async with Client(api_key="your-api-key") as client:
        # Get account information
        account = await client.get_account_v2(name="PlayerName", tag="TAG")

        print(f"Player: {account.name}#{account.tag}")
        print(f"PUUID: {account.puuid}")
        print(f"Region: {account.region}")
        print(f"Level: {account.account_level}")


if __name__ == "__main__":
    asyncio.run(main())
