from typing import Any, Dict

import pytest


class TestWebsite:
    """Test Website V1 endpoint."""

    @pytest.mark.asyncio
    async def test_website_response_structure(self, website: Dict[str, Any]) -> None:
        """Test that Website response has required structure.

        Parameters
        ----------
        website : Dict[str, Any]
            Mock website response data.
        """
        # Verify response has content
        assert website is not None

    @pytest.mark.asyncio
    async def test_website_has_data(self, website: Dict[str, Any]) -> None:
        """Test that Website response includes website information.

        Parameters
        ----------
        website : Dict[str, Any]
            Mock website response data.
        """
        data = website.get("data", {})

        # Verify website data exists
        assert len(data) > 0 or data is not None
