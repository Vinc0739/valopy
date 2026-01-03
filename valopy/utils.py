"""Utility functions for the valopy library."""

import logging
import re
from dataclasses import fields, is_dataclass
from datetime import datetime, timedelta, timezone
from typing import TYPE_CHECKING, Any, Type, cast, get_args, get_origin

if TYPE_CHECKING:
    from valopy.models import ValoPyModel

_log = logging.getLogger(__name__)


def _parse_datetime_string(value: str) -> datetime | None:
    """Parse datetime string in multiple formats.

    Supports:
    - ISO 8601 with timezone (2025-12-04T12:34:56Z, 2025-12-04T12:34:56+00:00)
    - Common format (Dec 4 2025)
    - Relative times (3 minutes ago, 2 hours ago, 1 day ago, etc.)

    Parameters
    ----------
    value : str
        The datetime string to parse.

    Returns
    -------
    datetime | None
        Parsed datetime object, or None if parsing fails.
    """
    if not isinstance(value, str) or not value.strip():
        return None

    # Try ISO 8601 formats first
    try:
        # Handle UTC indicator "Z"
        if "T" in value:
            return datetime.fromisoformat(value.replace("Z", "+00:00"))
        # Try parsing date-only format
        parsed = datetime.fromisoformat(value)
        return parsed.replace(tzinfo=None)
    except (ValueError, AttributeError):
        pass

    # Try "Dec 4 2025" format for version build_date response field
    try:
        return datetime.strptime(value, "%b %d %Y")
    except ValueError:
        pass

    # Try relative time format like "3 minutes ago" or "2 hours ago" for account v1 last_update field
    match = re.match(r"(\d+)\s+(minute|hour|day|week|month|year)s?\s+ago", value.lower())
    if match:
        amount = int(match.group(1))
        unit = match.group(2)
        try:
            match unit:
                case "minute":
                    return datetime.now(timezone.utc) - timedelta(minutes=amount)
                case "hour":
                    return datetime.now(timezone.utc) - timedelta(hours=amount)
                case "day":
                    return datetime.now(timezone.utc) - timedelta(days=amount)
                case "week":
                    return datetime.now(timezone.utc) - timedelta(weeks=amount)
                case "month":
                    return datetime.now(timezone.utc) - timedelta(days=amount * 30)
                case "year":
                    return datetime.now(timezone.utc) - timedelta(days=amount * 365)

        except (ValueError, OverflowError):
            pass

    _log.debug("Could not parse datetime string: %s", value)
    return None


def dict_to_dataclass(data: dict[str, Any], dataclass_type: Type["ValoPyModel"]) -> "ValoPyModel":
    """Convert a dictionary to a dataclass instance, handling nested dataclasses.
    Recursively converts nested dictionaries to their corresponding dataclass types
    if they are also dataclasses, and lists of nested dataclasses.
    Uses dataclass field introspection for performance optimization.

    Parameters
    ----------
    data : dict[str, Any]
        The dictionary to convert.
    dataclass_type : Type[ValoPyModel]
        The dataclass type to convert to (must be AccountV1, AccountV2, Content, or Version).

    Returns
    -------
    ValoPyModel
        An instance of the dataclass.
    """

    if not isinstance(data, dict):
        _log.debug("Data is not a dict, returning as-is: %s", type(data).__name__)
        return data  # type: ignore

    kwargs: dict[str, Any] = {}
    data_get = data.get

    _log.debug("Converting dict to %s", dataclass_type.__name__)
    for field in fields(dataclass_type):

        value = data_get(field.name)
        if value is None and field.name not in data:
            continue

        field_type = field.type

        # Parse datetime strings to datetime objects
        if field_type is datetime and isinstance(value, str):
            parsed = _parse_datetime_string(value)
            if parsed is not None:
                kwargs[field.name] = parsed
            else:
                kwargs[field.name] = value

        # Nested dataclass
        elif is_dataclass(field_type) and isinstance(value, dict):
            kwargs[field.name] = dict_to_dataclass(value, cast("Type[ValoPyModel]", field_type))

        # List of dataclasses
        elif get_origin(field_type) is list:
            args = get_args(field_type)
            if args and is_dataclass(args[0]) and isinstance(value, list):
                kwargs[field.name] = [
                    dict_to_dataclass(item, cast("Type[ValoPyModel]", args[0]))
                    for item in value
                    if isinstance(item, dict)
                ]
            else:
                kwargs[field.name] = value
        else:
            kwargs[field.name] = value

    return dataclass_type(**kwargs)  # type: ignore


def parse_datetimes(obj: Any) -> Any:
    """Recursively parse ISO 8601 datetime strings to datetime objects.

    Traverses dataclass instances and converts string fields that match ISO 8601
    format to datetime objects. Handles nested dataclasses and lists.

    Parameters
    ----------
    obj : Any
        A dataclass instance, list, or value to parse.

    Returns
    -------
    Any
        The object with datetime strings converted to datetime objects.
    """

    if isinstance(obj, str):
        # Try to parse ISO 8601 datetime strings
        try:
            # Handle both with and without microseconds/timezone
            if "T" in obj and ("Z" in obj or "+" in obj or obj.count(":") >= 2):
                return datetime.fromisoformat(obj.replace("Z", "+00:00"))
        except (ValueError, AttributeError):
            pass
        return obj

    if is_dataclass(obj) and not isinstance(obj, type):
        # Recursively parse fields in dataclass
        for field in fields(obj):
            value = getattr(obj, field.name, None)
            if value is not None:
                parsed = parse_datetimes(value)
                if parsed is not value:
                    setattr(obj, field.name, parsed)
        return obj

    if isinstance(obj, list):
        # Recursively parse items in list
        return [parse_datetimes(item) for item in obj]

    if isinstance(obj, dict):
        # Recursively parse values in dict
        return {key: parse_datetimes(value) for key, value in obj.items()}

    return obj
