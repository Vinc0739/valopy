import asyncio

from valopy import Client


async def get_account_v2_info():
    async with Client(api_key="your-api-key") as client:
        # Fetch account information (V2)
        account = await client.get_account_v2("PlayerName", "TAG")

        print(f"Player: {account.name}#{account.tag}")
        print(f"PUUID: {account.puuid}")
        print(f"Region: {account.region}")
        print(f"Level: {account.account_level}")
        print(f"Title: {account.title}")
        print(f"Card ID: {account.card}")
        print(f"Platforms: {', '.join(account.platforms)}")
        print(f"Updated At: {account.updated_at}")


asyncio.run(get_account_v2_info())
