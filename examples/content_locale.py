import asyncio

from valopy import Client, Locale


async def get_localized_content():
    async with Client(api_key="your-api-key") as client:
        # Get content in Spanish
        content = await client.get_content(locale=Locale.ES_ES)

        print("Characters (Spanish):")
        for character in content.characters[:5]:  # First 5
            print(f"  - {character.name}")
            # Access localized names if available
            if character.localizedNames and "es-ES" in character.localizedNames: # currently always None
                print(f"    Spanish: {character.localizedNames['es-ES']}")

        # Get content in Japanese
        content_jp = await client.get_content(locale=Locale.JA_JP)

        print("\nCharacters (Japanese):")
        for character in content_jp.characters[:5]:  # First 5
            print(f"  - {character.name}")


asyncio.run(get_localized_content())
