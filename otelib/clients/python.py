"""OTE Client for use with a local OTEAPI Core installation."""
import sys
from typing import TYPE_CHECKING

from otelib.strategies import DataResource, Filter, Function, Mapping, Transformation

if TYPE_CHECKING:  # pragma: no cover
    from pathlib import Path
    from typing import Optional, Union


class OTEClientPython:
    """The OTEClient object representing a local Python environment with OTEAPI Core.

    Parameters:
        url (str): The base URL of the OTEAPI Service.

    Attributes:
        url (str): The base URL of the OTEAPI Service.

    """

    def __init__(self, python_interpreter: "Optional[Union[Path, str]]" = None) -> None:
        """Initiates an OTEAPI Core client."""
        self._python_interpreter = Path(python_interpreter or sys.executable).resolve()

    def create_dataresource(self, **kwargs) -> DataResource:
        """Create a new data resource.

        Any given keyword arguments are passed on to the `create()` method.

        Returns:
            The newly created data resource.

        """
        data_resource = DataResource(py_exec=self._python_interpreter)
        data_resource.create(**kwargs)
        return data_resource

    def create_transformation(self, **kwargs) -> Transformation:
        """Create a new transformation.

        Any given keyword arguments are passed on to the `create()` method.

        Returns:
            The newly created transformation.

        """
        transformation = Transformation(self.url)
        transformation.create(**kwargs)
        return transformation

    def create_filter(self, **kwargs) -> Filter:
        """Create a new filter.

        Any given keyword arguments are passed on to the `create()` method.

        Returns:
            The newly created filter.

        """
        filter_ = Filter(self.url)
        filter_.create(**kwargs)
        return filter_

    def create_mapping(self, **kwargs) -> Mapping:
        """Create a new mapping.

        Any given keyword arguments are passed on to the `create()` method.

        Returns:
            The newly created mapping.

        """
        mapping = Mapping(self.url)
        mapping.create(**kwargs)
        return mapping

    def create_function(self, **kwargs) -> Function:
        """Create a new function.

        Any given keyword arguments are passed on to the `create()` method.

        Returns:
            The newly created function.

        """
        function_ = Function(self.url)
        function_.create(**kwargs)
        return function_
