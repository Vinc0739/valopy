import asyncio

from valopy import Client


async def force_update_account():
    async with Client(api_key="your-api-key") as client:
        # Force update the account data
        account = await client.get_account_v1(
            "PlayerName",
            "TAG",
            force_update=True
        )

        print(f"Fresh data for: {account.name}#{account.tag}")
        print(f"Updated at: {account.last_update}")

asyncio.run(force_update_account())
