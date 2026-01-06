from typing import Any, Dict
from unittest.mock import AsyncMock, patch

import pytest

from valopy.client import Client
from valopy.models import AccountV1, AccountV2, CardData, Result
from valopy.utils import dict_to_dataclass


class TestAccountV1:
    """Test Account V1 endpoint."""

    @pytest.mark.asyncio
    async def test_get_account_v1_parsing(self, account_v1: Dict[str, Any]) -> None:
        """Test that Account V1 response is correctly parsed.

        Parameters
        ----------
        account_v1 : Dict[str, Any]
            Mock account V1 response data.
        """

        client = Client(api_key="test-key")

        account_data = dict_to_dataclass(account_v1["data"], AccountV1)

        with patch.object(client.adapter, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = Result(
                status_code=account_v1["status"], message="OK", data=account_data
            )

            result: AccountV1 = await client.get_account_v1(
                name=account_v1["data"]["name"], tag=account_v1["data"]["tag"]
            )

            # Verify correct parsing
            assert isinstance(result, AccountV1)
            assert isinstance(result.card, CardData)
            assert result.puuid == account_v1["data"]["puuid"]
            assert result.account_level == account_v1["data"]["account_level"]

        await client.close()


class TestAccountV2:
    """Test Account V2 endpoint."""

    @pytest.mark.asyncio
    async def test_get_account_v2_parsing(self, account_v2: Dict[str, Any]) -> None:
        """Test that Account V2 response is correctly parsed.

        Parameters
        ----------
        account_v2 : Dict[str, Any]
            Mock account V2 response data.
        """

        client = Client(api_key="test-key")

        account_data = dict_to_dataclass(account_v2["data"], AccountV2)

        with patch.object(client.adapter, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = Result(
                status_code=account_v2["status"], message="OK", data=account_data
            )

            result: AccountV2 = await client.get_account_v2(
                name=account_v2["data"]["name"], tag=account_v2["data"]["tag"]
            )

            # Verify correct parsing
            assert isinstance(result, AccountV2)
            assert result.puuid == account_v2["data"]["puuid"]
            assert result.account_level == account_v2["data"]["account_level"]
            assert isinstance(result.platforms, list)

        await client.close()
