import asyncio

from valopy import Client


async def main() -> None:
    players = [
        ("Player1", "TAG1"),
        ("Player2", "TAG2"),
        ("Player3", "TAG3"),
    ]

    async with Client(api_key="your-api-key") as client:
        # Fetch multiple accounts concurrently.
        tasks = [client.get_account_v2(name=name, tag=tag) for name, tag in players]
        accounts = await asyncio.gather(*tasks, return_exceptions=True)

        for (name, tag), result in zip(players, accounts):
            if isinstance(result, BaseException):
                print(f"{name}#{tag}: Error - {result}")
            else:
                print(f"{name}#{tag}: Level {result.account_level}")


if __name__ == "__main__":
    asyncio.run(main())
