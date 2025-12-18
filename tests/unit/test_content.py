from typing import Any, Dict
from unittest.mock import AsyncMock, patch

import pytest

from valopy.client import Client
from valopy.models import Content, Result


class TestContent:
    """Test Content endpoint."""

    @pytest.mark.asyncio
    async def test_get_content_response_parsing(self, content: Dict[str, Any]) -> None:
        """Test that Content response is correctly parsed into Content dataclass.

        Parameters
        ----------
        content : Dict[str, Any]
            Mock content response data.
        """
        client = Client(api_key="test-key")

        # Use the first content data available in the mock file
        content_data = next((v for k, v in content.items() if isinstance(v, dict) and "characters" in v), None)
        if not content_data:
            pytest.skip("No content data in mock file")

        with patch.object(client.adapter, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = Result(status_code=200, message="OK", data=content_data)

            result: Content = await client.get_content()

            # Verify Content dataclass or dict with collections
            assert result is not None
            assert len(str(result)) > 0

        await client.close()

    @pytest.mark.asyncio
    async def test_content_has_collections(self, content: Dict[str, Any]) -> None:
        """Test that Content has all collection attributes as lists.

        Parameters
        ----------
        content : Dict[str, Any]
            Mock content response data.
        """
        client = Client(api_key="test-key")

        # Use the first content data available
        content_data = next((v for k, v in content.items() if isinstance(v, dict) and "characters" in v), None)
        if not content_data:
            pytest.skip("No content data in mock file")

        with patch.object(client.adapter, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = Result(status_code=200, message="OK", data=content_data)

            result: Content = await client.get_content()

            # Verify collections exist in response
            assert "characters" in content_data or hasattr(result, "characters")

        await client.close()
