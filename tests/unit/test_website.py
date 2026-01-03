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

            # Verify first item
            first_item = result[0]
            assert isinstance(first_item, WebsiteContent)
            assert first_item.id == website["data"][0]["id"]
            assert first_item.title == website["data"][0]["title"]

        await client.close()
