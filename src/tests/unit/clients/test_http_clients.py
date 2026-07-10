import pytest
from faker import Faker

from src.services.clients.http_clients.base import BaseHTTPClient
from src.services.exceptions.http_clients import HTTPClientException


@pytest.mark.asyncio
async def test_http_client_get_success(
    http_client: BaseHTTPClient,
    url: str,
    faker: Faker,
):
    data = faker.text()
    status_code = 200
    http_client._add_response(
        method='get',
        url=url,
        data=data,
        status_code=status_code,
    )

    result: dict = await http_client.get(url=url)

    assert result.get('data') == data, f'{result=}'
    assert result.get('status_code') == status_code, f'{result=}'


@pytest.mark.asyncio
async def test_http_client_get_http_client_exception(
    http_client: BaseHTTPClient,
    url: str,
    faker: Faker,
):
    http_client._add_response(
        method='get',
        url=url,
        data=faker.text(),
        status_code=404,
    )
    with pytest.raises(HTTPClientException):
        await http_client.get(url=url)


@pytest.mark.asyncio
async def test_http_client_post_success(
    http_client: BaseHTTPClient,
    url: str,
    faker: Faker,
):
    data = faker.text()
    status_code = 200
    http_client._add_response(
        method='post',
        url=url,
        data=data,
        status_code=status_code,
    )

    result: dict = await http_client.post(url=url)

    assert result.get('data') == data, f'{result=}'
    assert result.get('status_code') == status_code, f'{result=}'


@pytest.mark.asyncio
async def test_http_client_post_http_client_exception(
    http_client: BaseHTTPClient,
    url: str,
    faker: Faker,
):
    http_client._add_response(
        method='post',
        url=url,
        data=faker.text(),
        status_code=404,
    )
    with pytest.raises(HTTPClientException):
        await http_client.post(url=url)


@pytest.mark.asyncio
async def test_http_client_patch_success(
    http_client: BaseHTTPClient,
    url: str,
    faker: Faker,
):
    data = faker.text()
    status_code = 200
    http_client._add_response(
        method='patch',
        url=url,
        data=data,
        status_code=status_code,
    )

    result: dict = await http_client.patch(url=url)

    assert result.get('data') == data, f'{result=}'
    assert result.get('status_code') == status_code, f'{result=}'


@pytest.mark.asyncio
async def test_http_client_patch_http_client_exception(
    http_client: BaseHTTPClient,
    url: str,
    faker: Faker,
):
    http_client._add_response(
        method='patch',
        url=url,
        data=faker.text(),
        status_code=404,
    )
    with pytest.raises(HTTPClientException):
        await http_client.patch(url=url)
