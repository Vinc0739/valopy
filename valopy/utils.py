"""Utility functions for the valopy library."""

import logging
from dataclasses import fields, is_dataclass
from typing import TYPE_CHECKING, List, Type, get_args, get_origin

if TYPE_CHECKING:
    from valopy.models import ValoPyModel

_log = logging.getLogger(__name__)


def dict_to_dataclass(data: dict, dataclass_type: Type["ValoPyModel"]) -> "ValoPyModel":
    """Convert a dictionary to a dataclass instance, handling nested dataclasses.

    Recursively converts nested dictionaries to their corresponding dataclass types
    if they are also dataclasses, and lists of nested dataclasses.

    Uses dataclass field introspection for performance optimization.

    Parameters
    ----------
    data : dict
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

    # Use dataclass fields for better performance and reliability
    kwargs = {}
    field_map = {field.name: field for field in fields(dataclass_type)}

    _log.debug("Converting dict to %s", dataclass_type.__name__)

    for field_name, field_obj in field_map.items():
        if field_name not in data:
            continue

        value = data[field_name]
        field_type = field_obj.type

        # Handle nested dataclasses
        if is_dataclass(field_type) and isinstance(value, dict):
            _log.debug("Converting nested field '%s'", field_name)
            kwargs[field_name] = dict_to_dataclass(value, field_type)  # type: ignore
        # Handle lists of dataclasses
        elif isinstance(value, list) and value:
            # Get the inner type from List[T]
            origin = get_origin(field_type)
            if origin in (list, List):
                inner_type = get_args(field_type)[0] if get_args(field_type) else None
                if inner_type and is_dataclass(inner_type):
                    _log.debug("Converting list field '%s' with %d items", field_name, len(value))
                    kwargs[field_name] = [
                        dict_to_dataclass(item, inner_type) if isinstance(item, dict) else item  # type: ignore
                        for item in value
                    ]
                else:
                    kwargs[field_name] = value
            else:
                kwargs[field_name] = value
        # Handle all other cases (primitives, non-dataclass objects, etc.)
        else:
            kwargs[field_name] = value

    return dataclass_type(**kwargs)  # type: ignore
