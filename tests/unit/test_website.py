from typing import Any, Dict, List
from unittest.mock import AsyncMock, patch

import pytest

from valopy.client import Client
from valopy.enums import CountryCode
from valopy.models import Result, WebsiteContent
from valopy.utils import dict_to_dataclass


class TestWebsite:
    """Test Website endpoint."""

    @pytest.mark.asyncio
    async def test_get_website_parsing(self, website: Dict[str, Any]) -> None:
        """Test that Website response is correctly parsed.

        Parameters
        ----------
        website : Dict[str, Any]
            Mock website response data.
        """

        client = Client(api_key="test-key")

        website_data = [dict_to_dataclass(item, WebsiteContent) for item in website["data"]]

        with patch.object(client.adapter, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = Result(status_code=website["status"], message="OK", data=website_data)

            result: List[WebsiteContent] = await client.get_website(countrycode=CountryCode.DE_DE)

            # Verify correct parsing
            assert isinstance(result, list)
            assert len(result) == len(website["data"])
            assert all(isinstance(item, WebsiteContent) for item in result)

            # Verify first item data
            first_item = result[0]
            first_mock = website["data"][0]
            assert first_item.id == first_mock["id"]
            assert first_item.banner_url == first_mock["banner_url"]
            assert first_item.category == first_mock["category"]
            assert first_item.title == first_mock["title"]
            assert first_item.url == first_mock["url"]

        await client.close()
