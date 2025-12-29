import asyncio

from valopy import Client, Region


async def main() -> None:
    async with Client(api_key="your-api-key") as client:
        # Get queue status for EU region
        queues = await client.get_queue_status(region=Region.EU)

        for queue_data in queues:
            print(f"\nMode: {queue_data.mode} ({queue_data.mode_id})")
            print(f"  Enabled: {queue_data.enabled}")
            print(f"  Ranked: {queue_data.ranked}")
            print(f"  Team Size: {queue_data.team_size}")
            print(f"  Number of Teams: {queue_data.number_of_teams}")
            print(f"  Required Level: {queue_data.required_account_level}")

            print("\n  Party Size:")
            print(f"    Min: {queue_data.party_size.min}")
            print(f"    Max: {queue_data.party_size.max}")
            print(f"    Full Party Bypass: {queue_data.party_size.full_party_bypass}")

            if queue_data.maps:
                print("\n  Available Maps:")
                for map_entry in queue_data.maps:
                    status = "✓" if map_entry.enabled else "✗"
                    print(f"    {status} {map_entry.map.name}")

            print(f"\n  Platforms: {', '.join(queue_data.platforms)}")


if __name__ == "__main__":
    asyncio.run(main())
