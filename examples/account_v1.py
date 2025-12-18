import asyncio

from valopy import Client


async def get_account_info():
    async with Client(api_key="your-api-key") as client:
        # Fetch account information
        account = await client.get_account_v1("PlayerName", "TAG")

        print(f"Player: {account.name}#{account.tag}")
        print(f"PUUID: {account.puuid}")
        print(f"Region: {account.region}")
        print(f"Level: {account.account_level}")
        print(f"Last Update: {account.last_update}")

        # Access card information
        print(f"Card ID: {account.card.id}")
        print(f"Card (Small): {account.card.small}")
        print(f"Card (Large): {account.card.large}")
        print(f"Card (Wide): {account.card.wide}")


asyncio.run(get_account_info())
