import asyncio

from valopy import Client

async def fetch_multiple_accounts():
    players = [
        ("Bumbibjörn1", "demi"),
        ("needy", "owo"),
        ("长生天", "0829"),
    ]

    async with Client(api_key="your-api-key") as client:
        # Fetch all accounts concurrently
        tasks = [
            client.get_account_v1(name, tag)
            for name, tag in players
        ]

        accounts = await asyncio.gather(*tasks, return_exceptions=True)

        # Process results
        for (name, tag), result in zip(players, accounts):
            if isinstance(result, Exception):
                print(f"{name}#{tag}: Error - {result}")
            else:
                print(f"{name}#{tag}: Level {result.account_level}") #type: ignore

asyncio.run(fetch_multiple_accounts())
