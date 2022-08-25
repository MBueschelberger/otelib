"""Tests for `otelib.backends.services.filter`."""
# pylint: disable=redefined-builtin
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from typing import Callable, Union

    from tests.conftest import OTEResponse, ResourceType


def test_create(
    testdata: "Callable[[Union[ResourceType, str]], dict]",
) -> None:
    """Test `Filter.create()`."""
    from otelib.backends.python.filter import Filter

    filter = Filter('python')

    assert filter.id is None

    filter.create(
        filterType="filter/sql",
        query=testdata("filter")["sqlquery"],
    )

    assert filter.id


def test_fetch(
    testdata: "Callable[[Union[ResourceType, str]], dict]",
) -> None:
    """Test `Filter.fetch()`."""
    import json
    from oteapi.plugins import load_strategies
    load_strategies()

    from otelib.backends.python.filter import Filter

    filter = Filter('python')

    # We must first create the resource - getting a resource ID
    filter.create(
        filterType="filter/sql",
        query=testdata("filter")["sqlquery"],
    )

    content = filter.fetch(session_id=None)

    assert json.loads(content) == {}


#def test_fetch_fails(
#    mock_ote_response: "OTEResponse",
#    ids: "Callable[[Union[ResourceType, str]], str]",
#    server_url: str,
#    testdata: "Callable[[Union[ResourceType, str]], dict]",
#) -> None:
#    """Check `Filter.fetch()` raises `ApiError` upon request failure."""
#    from otelib.exceptions import ApiError
#    from otelib.backends.services.filter import Filter
#
#    mock_ote_response(
#        method="post",
#        endpoint="/filter",
#        return_json={"filter_id": ids("filter")},
#    )
#
#    mock_ote_response(
#        method="get",
#        endpoint=f"/filter/{ids('filter')}",
#        status_code=500,
#        return_content=b"Internal Server Error",
#    )
#
#    filter = Filter(server_url)
#
#    # We must first create the resource - getting a resource ID
#    filter.create(
#        filterType="filter/sql",
#        query=testdata("filter")["sqlquery"],
#    )
#
#    with pytest.raises(ApiError, match="APIError"):
#        # `session_id` has a wrong type, the request should fail.
#        filter.fetch(session_id=123)
#
#
#def test_initialize(
#    mock_ote_response: "OTEResponse",
#    ids: "Callable[[Union[ResourceType, str]], str]",
#    server_url: str,
#    testdata: "Callable[[Union[ResourceType, str]], dict]",
#) -> None:
#    """Test `Filter.fetch()`."""
#    import json
#
#    from otelib.backends.services.filter import Filter
#
#    mock_ote_response(
#        method="post",
#        endpoint="/filter",
#        return_json={"filter_id": ids("filter")},
#    )
#
#    mock_ote_response(
#        method="post",
#        endpoint=f"/filter/{ids('filter')}/initialize",
#        return_json=testdata("filter"),
#    )
#
#    filter = Filter(server_url)
#
#    # We must first create the resource - getting a resource ID
#    filter.create(
#        filterType="filter/sql",
#        query=testdata("filter")["sqlquery"],
#    )
#
#    content = filter.initialize(session_id=None)
#
#    assert json.loads(content) == testdata("filter")
#
#
#def test_initialize_fails(
#    mock_ote_response: "OTEResponse",
#    ids: "Callable[[Union[ResourceType, str]], str]",
#    server_url: str,
#    testdata: "Callable[[Union[ResourceType, str]], dict]",
#) -> None:
#    """Check `Filter.fetch()` raises `ApiError` upon request failure."""
#    from otelib.exceptions import ApiError
#    from otelib.backends.services.filter import Filter
#
#    mock_ote_response(
#        method="post",
#        endpoint="/filter",
#        return_json={"filter_id": ids("filter")},
#    )
#
#    mock_ote_response(
#        method="post",
#        endpoint=f"/filter/{ids('filter')}/initialize",
#        status_code=500,
#        return_content=b"Internal Server Error",
#    )
#
#    filter = Filter(server_url)
#
#    # We must first create the resource - getting a resource ID
#    filter.create(
#        filterType="filter/sql",
#        query=testdata("filter")["sqlquery"],
#    )
#
#    with pytest.raises(ApiError, match="APIError"):
#        # `session_id` has a wrong type, the request should fail.
#        filter.initialize(session_id=123)
#