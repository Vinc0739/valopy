from typing import Any, Dict
from unittest.mock import AsyncMock, patch

import pytest

from valopy.client import Client
from valopy.models import AccountV1, AccountV2, CardData, Result
from valopy.utils import dict_to_dataclass


class TestAccountV1:
    """Test Account V1 endpoint."""

    @pytest.mark.asyncio
    async def test_get_account_v1_response_parsing(self, account_v1: Dict[str, Any]) -> None:
        """Test that Account V1 response is correctly parsed into AccountV1 dataclass.

        Parameters
        ----------
        account_v1 : Dict[str, Any]
            Mock account V1 response data.
        """
        client = Client(api_key="test-key")

        # Create the dataclass from mock data
        account_data = dict_to_dataclass(account_v1["data"], AccountV1)

        with patch.object(client.adapter, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = Result(status_code=account_v1["status"], message="OK", data=account_data)

            result: AccountV1 = await client.get_account_v1(
                name=account_v1["data"]["name"], tag=account_v1["data"]["tag"]
            )

            # Verify AccountV1 attributes
            assert isinstance(result, AccountV1)
            assert result.puuid == account_v1["data"]["puuid"]
            assert result.region == account_v1["data"]["region"]
            assert result.account_level == account_v1["data"]["account_level"]
            assert result.name == account_v1["data"]["name"]
            assert result.tag == account_v1["data"]["tag"]
            assert result.last_update == account_v1["data"]["last_update"]
            assert result.last_update_raw == account_v1["data"]["last_update_raw"]

            # Verify CardData structure
            assert isinstance(result.card, CardData)
            assert result.card.small == account_v1["data"]["card"]["small"]
            assert result.card.large == account_v1["data"]["card"]["large"]
            assert result.card.wide == account_v1["data"]["card"]["wide"]
            assert result.card.id == account_v1["data"]["card"]["id"]

        await client.close()

    @pytest.mark.asyncio
    async def test_get_account_v1_fields_present(self, account_v1: Dict[str, Any]) -> None:
        """Test that all required fields are present in parsed Account V1.

        Parameters
        ----------
        account_v1 : Dict[str, Any]
            Mock account V1 response data.
        """
        client = Client(api_key="test-key")
        account_data = dict_to_dataclass(account_v1["data"], AccountV1)

        with patch.object(client.adapter, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = Result(status_code=200, message="OK", data=account_data)

            result: AccountV1 = await client.get_account_v1("example", "1234")

            # Verify all required attributes exist
            assert hasattr(result, "puuid")
            assert hasattr(result, "region")
            assert hasattr(result, "account_level")
            assert hasattr(result, "name")
            assert hasattr(result, "tag")
            assert hasattr(result, "card")
            assert hasattr(result, "last_update")
            assert hasattr(result, "last_update_raw")

            # Verify types
            assert isinstance(result.puuid, str)
            assert isinstance(result.account_level, int)
            assert result.account_level > 0

        await client.close()


class TestAccountV2:
    """Test Account V2 endpoint."""

    @pytest.mark.asyncio
    async def test_get_account_v2_response_parsing(self, account_v2: Dict[str, Any]) -> None:
        """Test that Account V2 response is correctly parsed into AccountV2 dataclass.

        Parameters
        ----------
        account_v2 : Dict[str, Any]
            Mock account V2 response data.
        """
        client = Client(api_key="test-key")
        account_data = dict_to_dataclass(account_v2["data"], AccountV2)

        with patch.object(client.adapter, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = Result(status_code=account_v2["status"], message="OK", data=account_data)

            result: AccountV2 = await client.get_account_v2(
                name=account_v2["data"]["name"], tag=account_v2["data"]["tag"]
            )

            # Verify AccountV2 attributes
            assert isinstance(result, AccountV2)
            assert result.puuid == account_v2["data"]["puuid"]
            assert result.region == account_v2["data"]["region"]
            assert result.account_level == account_v2["data"]["account_level"]
            assert result.name == account_v2["data"]["name"]
            assert result.tag == account_v2["data"]["tag"]
            assert result.card == account_v2["data"]["card"]
            assert result.title == account_v2["data"]["title"]
            assert result.platforms == account_v2["data"]["platforms"]
            assert result.updated_at == account_v2["data"]["updated_at"]

        await client.close()

    @pytest.mark.asyncio
    async def test_get_account_v2_specific_fields(self, account_v2: Dict[str, Any]) -> None:
        """Test that V2-specific fields (title, platforms) are present and correct.

        Parameters
        ----------
        account_v2 : Dict[str, Any]
            Mock account V2 response data.
        """
        client = Client(api_key="test-key")
        account_data = dict_to_dataclass(account_v2["data"], AccountV2)

        with patch.object(client.adapter, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = Result(status_code=200, message="OK", data=account_data)

            result: AccountV2 = await client.get_account_v2("example", "1234")

            # V2 specific fields
            assert hasattr(result, "title")
            assert isinstance(result.title, str)
            assert hasattr(result, "platforms")
            assert isinstance(result.platforms, list)
            assert len(result.platforms) > 0

        await client.close()
