"""Tests for `otelib.backends.services.dataresource`."""
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from typing import Callable, Union

    from tests.conftest import OTEResponse, ResourceType


def test_create() -> None:
    """Test `DataResource.create()`."""
    from otelib.backends.python.dataresource import DataResource
    data_resource = DataResource('python')

    assert data_resource.id is None

    data_resource.create(
        downloadUrl="https://filesamples.com/samples/code/json/sample2.json",
        mediaType="application/json",
    )

    assert data_resource.id


def test_fetch() -> None:
    """Test `DataResource.fetch()`."""
    import json

    from otelib.backends.python.dataresource import DataResource
    from oteapi.plugins import load_strategies
    load_strategies()

    expected_result = {'content': {'firstName': 'Joe',
                       'lastName': 'Jackson',
                       'gender': 'male',
                       'age': 28,
                       'address': 
                       {'streetAddress': '101',
                        'city': 'San Diego', 'state': 'CA'},
                       'phoneNumbers':
                        [{'type': 'home', 'number': '7349282382'}]}}

    data_resource = DataResource('python')
    data_resource.create(
        downloadUrl="https://filesamples.com/samples/code/json/sample2.json",
        mediaType="application/json",
    )
    content = data_resource.fetch(session_id=None).json()

    assert json.loads(content) == expected_result 
#
#
#def test_fetch_fails(
#    mock_ote_response: "OTEResponse",
#    ids: "Callable[[Union[ResourceType, str]], str]",
#    server_url: str,
#) -> None:
#    """Check `DataResource.fetch()` raises `ApiError` upon request failure."""
#    from otelib.exceptions import ApiError
#    from otelib.backends.services.dataresource import DataResource
#
#    mock_ote_response(
#        method="post",
#        endpoint="/dataresource",
#        return_json={"resource_id": ids("dataresource")},
#    )
#
#    mock_ote_response(
#        method="get",
#        endpoint=f"/dataresource/{ids('dataresource')}",
#        status_code=500,
#        return_content=b"Internal Server Error",
#    )
#
#    data_resource = DataResource(server_url)
#
#    # We must first create the resource - getting a resource ID
#    data_resource.create(
#        downloadUrl="https://filesamples.com/samples/code/json/sample2.json",
#        mediaType="application/json",
#    )
#
#    with pytest.raises(ApiError, match="APIError"):
#        # `session_id` has a wrong type, the request should fail.
#        data_resource.fetch(session_id=123)
#
#
#def test_initialize(
#    mock_ote_response: "OTEResponse",
#    ids: "Callable[[Union[ResourceType, str]], str]",
#    server_url: str,
#) -> None:
#    """Test `DataResource.fetch()`."""
#    import json
#
#    from otelib.backends.services.dataresource import DataResource
#
#    mock_ote_response(
#        method="post",
#        endpoint="/dataresource",
#        return_json={"resource_id": ids("dataresource")},
#    )
#
#    mock_ote_response(
#        method="post",
#        endpoint=f"/dataresource/{ids('dataresource')}/initialize",
#        return_json={},
#    )
#
#    data_resource = DataResource(server_url)
#
#    # We must first create the resource - getting a resource ID
#    data_resource.create(
#        downloadUrl="https://filesamples.com/samples/code/json/sample2.json",
#        mediaType="application/json",
#    )
#
#    content = data_resource.initialize(session_id=None)
#
#    assert json.loads(content) == {}
#
#
#def test_initialize_fails(
#    mock_ote_response: "OTEResponse",
#    ids: "Callable[[Union[ResourceType, str]], str]",
#    server_url: str,
#) -> None:
#    """Check `DataResource.fetch()` raises `ApiError` upon request failure."""
#    from otelib.exceptions import ApiError
#    from otelib.backends.services.dataresource import DataResource
#
#    mock_ote_response(
#        method="post",
#        endpoint="/dataresource",
#        return_json={"resource_id": ids("dataresource")},
#    )
#
#    mock_ote_response(
#        method="post",
#        endpoint=f"/dataresource/{ids('dataresource')}/initialize",
#        status_code=500,
#        return_content=b"Internal Server Error",
#    )
#
#    data_resource = DataResource(server_url)
#
#    # We must first create the resource - getting a resource ID
#    data_resource.create(
#        downloadUrl="https://filesamples.com/samples/code/json/sample2.json",
#        mediaType="application/json",
#    )
#
#    with pytest.raises(ApiError, match="APIError"):
#        # `session_id` has a wrong type, the request should fail.
#        data_resource.initialize(session_id=123)
#