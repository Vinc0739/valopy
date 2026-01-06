from typing import Any, Dict
from unittest.mock import AsyncMock, patch

import pytest

from valopy.client import Client
from valopy.enums import Region
from valopy.models import Result, Version
from valopy.utils import dict_to_dataclass


class TestVersion:
    """Test Version V1 endpoint."""

    @pytest.mark.asyncio
    async def test_get_version_parsing(self, version: Dict[str, Any]) -> None:
        """Test that Version response is correctly parsed.

        Parameters
        ----------
        version : Dict[str, Any]
            Mock version response data.
        """

        client = Client(api_key="test-key")

        version_data = dict_to_dataclass(version["data"], Version)

        with patch.object(client.adapter, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = Result(
                status_code=version["status"], message="OK", data=version_data
            )

            result: Version = await client.get_version(region=Region.EU)

            # Verify correct parsing
            assert isinstance(result, Version)
            assert result.region == version["data"]["region"]
            assert result.branch == version["data"]["branch"]
            assert result.build_ver == version["data"]["build_ver"]

        await client.close()
