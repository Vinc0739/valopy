import asyncio

from valopy import Client, Region


async def get_version_info():
    async with Client(api_key="your-api-key") as client:
        # Fetch current version information
        version = await client.get_version(region=Region.NA)

        print(f"Region: {version.region}")
        print(f"Branch: {version.branch}")
        print(f"Build Version: {version.build_ver}")
        print(f"Build Date: {version.build_date}")
        print(f"Last Checked: {version.last_checked}")
        print(f"Version: {version.version}")
        print(f"Version for API: {version.version_for_api}")


asyncio.run(get_version_info())
