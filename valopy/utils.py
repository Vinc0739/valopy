"""Utility functions for the valopy library."""

import logging
from dataclasses import fields, is_dataclass
from typing import TYPE_CHECKING, Any, Type, cast, get_args, get_origin

if TYPE_CHECKING:
    from valopy.models import ValoPyModel

_log = logging.getLogger(__name__)


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

        # Nested dataclass
        if is_dataclass(field_type) and isinstance(value, dict):
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
