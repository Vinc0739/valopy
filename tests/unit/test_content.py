from typing import Any, Dict
from unittest.mock import AsyncMock, patch

import pytest

from valopy.client import Client
from valopy.models import Content, Result
from valopy.utils import dict_to_dataclass


class TestContent:
    """Test Content endpoint."""

    @pytest.mark.asyncio
    async def test_get_content_parsing(self, content: Dict[str, Any]) -> None:
        """Test that Content response is correctly parsed.

        Parameters
        ----------
        content : Dict[str, Any]
            Mock content response data.
        """

        client = Client(api_key="test-key")

        content_data = dict_to_dataclass(content["data"], Content)

        with patch.object(client.adapter, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = Result(status_code=content["status"], message="OK", data=content_data)

            result: Content = await client.get_content()

            # Verify correct parsing
            assert isinstance(result, Content)
            assert hasattr(result, "characters")
            assert hasattr(result, "maps")
            assert isinstance(result.characters, list)

        await client.close()
