"""Utility functions for the valopy library."""

import logging
from dataclasses import is_dataclass
from typing import Any, Type

_log = logging.getLogger(__name__)


def _get_inner_type(field_type: Any) -> Any | None:
    """Extract inner type from List[T] or other generic types.

    Parameters
    ----------
    field_type : Any
        The field type, possibly a generic like List[T].

    Returns
    -------
    Any | None
        The inner type if available, None otherwise.
    """
    # Handle List[T], Optional[T], etc.
    if hasattr(field_type, "__origin__") and hasattr(field_type, "__args__"):
        return field_type.__args__[0] if field_type.__args__ else None
    return None


def dict_to_dataclass(data: dict, dataclass_type: Any) -> Any:
    """Convert a dictionary to a dataclass instance, handling nested dataclasses.

    Recursively converts nested dictionaries to their corresponding dataclass types
    if they are also dataclasses, and lists of nested dataclasses.

    Parameters
    ----------
    data : dict
        The dictionary to convert.
    dataclass_type : Any
        The dataclass type to convert to.

    Returns
    -------
    Any
        An instance of the dataclass.

    Examples
    --------
    >>> data = {'name': 'John', 'card': {'small': 'url1', 'large': 'url2'}}
    >>> account = dict_to_dataclass(data, AccountV1)
    >>> account.name
    'John'
    >>> account.card.small
    'url1'
    """
    if not isinstance(data, dict):
        _log.debug("Data is not a dict, returning as-is: %s", type(data).__name__)
        return data

    # Get the dataclass fields and their type hints
    field_types = dataclass_type.__annotations__
    kwargs = {}

    _log.debug(
        "Converting dict to %s with fields: %s",
        dataclass_type.__name__,
        list(field_types.keys()),
    )

    for field_name, field_type in field_types.items():
        if field_name in data:
            value = data[field_name]

            # Handle nested dataclasses
            if is_dataclass(field_type) and isinstance(value, dict):
                _log.debug("Converting nested field '%s'", field_name)
                kwargs[field_name] = dict_to_dataclass(value, field_type)  # type: ignore
            # Handle lists of dataclasses
            elif isinstance(value, list) and value:
                inner_type = _get_inner_type(field_type)
                if inner_type and is_dataclass(inner_type):
                    _log.debug(
                        "Converting list field '%s' with %d items",
                        field_name,
                        len(value),
                    )
                    kwargs[field_name] = [
                        dict_to_dataclass(item, inner_type) if isinstance(item, dict) else item for item in value
                    ]
                else:
                    kwargs[field_name] = value
            else:
                kwargs[field_name] = value
        else:
            _log.debug(
                "Field '%s' not found in data for %s",
                field_name,
                dataclass_type.__name__,
            )

    instance = dataclass_type(**kwargs)
    _log.debug("Successfully converted dict to %s instance", dataclass_type.__name__)
    return instance


def get_model_class_for_endpoint(endpoint: str, endpoint_model_map: dict[str, Type[Any]]) -> Type[Any] | None:
    """Get the model class for an endpoint by matching patterns.

    Matches endpoints against patterns in the map to handle parameterized endpoints
    like `/v1/account/{name}/{tag}`.

    Parameters
    ----------
    endpoint : str
        The endpoint path (with parameters replaced, e.g., `/v1/account/PlayerName/TAG`).
    endpoint_model_map : dict[str, Type[Any]]
        Dictionary mapping endpoint patterns to model classes.

    Returns
    -------
    Type[Any] | None
        The model class if found, otherwise None.

    Examples
    --------
    >>> model = get_model_class_for_endpoint('/v1/account/John/123', ENDPOINT_MODEL_MAP)
    >>> model.__name__
    'AccountV1'
    """
    # Direct lookup first
    if endpoint in endpoint_model_map:
        _log.debug("Found direct match for endpoint: %s", endpoint)
        return endpoint_model_map[endpoint]

    _log.debug("No direct match found, attempting pattern matching for: %s", endpoint)

    # Pattern matching for parameterized endpoints
    for pattern, model_class in endpoint_model_map.items():
        # Check if endpoint matches the pattern structure by comparing path segments
        endpoint_parts = endpoint.split("/")
        pattern_parts = pattern.split("/")

        if len(endpoint_parts) != len(pattern_parts):
            continue

        match = True
        for ep_part, pat_part in zip(endpoint_parts, pattern_parts):
            if not (ep_part == pat_part or pat_part.startswith("{")):
                match = False
                break

        if match:
            _log.debug(
                "Found pattern match for endpoint %s -> pattern %s (model: %s)",
                endpoint,
                pattern,
                model_class.__name__,
            )
            return model_class

    _log.warning("No model class found for endpoint: %s", endpoint)
    return None
