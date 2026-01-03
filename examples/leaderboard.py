import asyncio

from valopy import Client, Platform, Region


async def main() -> None:
    async with Client(api_key="your-api-key") as client:
        # Get leaderboard for NA region on PC
        leaderboard = await client.get_leaderboard(region=Region.NA, platform=Platform.PC, size=10)

        print(f"Top {len(leaderboard.players)} Players")
        print(f"Updated: {leaderboard.updated_at}\n")

        for player in leaderboard.players:
            print(f"{player.leaderboard_rank}. {player.name}#{player.tag} - {player.rr} RR ({player.wins} wins)")

        # Show pagination info
        if leaderboard.results:
            print(f"\nTotal players: {leaderboard.results.total}")


if __name__ == "__main__":
    asyncio.run(main())
