import asyncio

from valopy import Client, CountryCode


async def get_website_info():
    async with Client(api_key="your-api-key") as client:
        # Get all website content information
        website = await client.get_website(countrycode=CountryCode.DE_DE)

        # Get the first content item (newest to oldest)
        content = website[0]
        print(f"Content ID: {content.id}")
        print(f"Banner URL: {content.banner_url}")
        print(f"Description: {content.description}")
        print(f"Category: {content.category}")
        print(f"Date: {content.date}")
        print(f"External Link: {content.external_link}")
        print(f"Title: {content.title}")
        print(f"URL: {content.url}")


asyncio.run(get_website_info())
