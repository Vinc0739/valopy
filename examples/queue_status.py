import asyncio

from valopy import Client, Region


async def main() -> None:
    async with Client(api_key="your-api-key") as client:
        # Get queue status
        queues = await client.get_queue_status(region=Region.EU)

        for queue in queues:
            if queue.mode in ["Unrated", "Competitive"]:

                print(f"\n{queue.mode}")
                print(f"  Team Size: {queue.team_size}v{queue.team_size}")
                print(f"  Party: {queue.party_size.min}-{queue.party_size.max}")
                print(f"  Required Level: {queue.required_account_level}")


if __name__ == "__main__":
    asyncio.run(main())
