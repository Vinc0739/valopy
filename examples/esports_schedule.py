import asyncio

from valopy import Client, League


async def main() -> None:
    async with Client(api_key="your-api-key") as client:
        # Get esports schedule
        events = await client.get_esports_schedule()

        print(f"Total events: {len(events)}")

        if events:
            event = events[0]
            print(f"Event: {event.league.name}")
            print(f"State: {event.state}")
            print(f"Tournament: {event.tournament.name}")
            if event.match.teams:
                for team in event.match.teams:
                    print(f"  - {team.name}: {team.game_wins} wins")

        # Filter by league
        vct_events = await client.get_esports_schedule(league=League.VCT_AMERICAS)
        print(f"\nVCT Americas events: {len(vct_events)}")


if __name__ == "__main__":
    asyncio.run(main())
