import asyncio

from valopy import Client


async def get_content():
    async with Client(api_key="your-api-key") as client:
        # Get content data
        content = await client.get_content()

        print(f"Version: {content.version}")
        print(f"Characters: {len(content.characters)}")
        print(f"Maps: {len(content.maps)}")
        print(f"Skins: {len(content.skins)}")
        print(f"Acts: {len(content.acts)}")

        # List all characters
        print("\nAvailable Characters:")
        for character in content.characters:
            print(f"  - {character.name} (ID: {character.id})")

        # List active acts
        print("\nActive Acts:")
        for act in content.acts:
            if act.isActive:
                print(f"  - {act.name} (ID: {act.id})")

asyncio.run(get_content())
