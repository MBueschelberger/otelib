"""Filter strategy."""
from typing import TYPE_CHECKING

from oteapi.models import FilterConfig

from .base import AbstractServicesStrategy

if TYPE_CHECKING:  # pragma: no cover
    from typing import Optional


class Filter(AbstractServicesStrategy):
    """Context class for the Filter Strategy Interfaces"""

    strategy_name = "filter"
    strategy_config = FilterConfig
