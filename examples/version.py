import asyncio

from valopy import Client, Region


async def main() -> None:
    async with Client(api_key="your-api-key") as client:
        # Get current game version information.
        version = await client.get_version(region=Region.EU)

        print(f"Version: {version.version_for_api}")
        print(f"Branch: {version.branch}")
        print(f"Build: {version.build_ver}")
        print(f"Released: {version.build_date}")


if __name__ == "__main__":
    asyncio.run(main())
