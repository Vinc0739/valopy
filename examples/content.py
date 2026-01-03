"""Get game content like characters, maps, and skins."""

import asyncio

from valopy import Client, Locale


async def main() -> None:
    async with Client(api_key="your-api-key") as client:
        # Get content with optional locale
        content = await client.get_content(locale=Locale.EN_US)

        print(f"Version: {content.version}")
        print(f"Characters ({len(content.characters)}):")
        for char in content.characters[:5]:
            print(f"  - {char.name}")

        print(f"Maps ({len(content.maps)}):")
        for map_item in content.maps[:5]:
            print(f"  - {map_item.name}")


if __name__ == "__main__":
    asyncio.run(main())
