from dataclasses import (
    dataclass,
    field,
)
from typing import Any

from src.services.clients.http_clients.base import BaseHTTPClient
from src.services.exceptions.http_clients import HTTPClientException


@dataclass
class MemoryHTTPClient(BaseHTTPClient):
    _responses: dict[tuple[str, str], dict] = field(
        default_factory=dict,
        kw_only=True,
    )

    def _add_response(
        self,
        method: str,
        url: str,
        data: Any,
        status_code: int,
    ) -> None:
        self._responses[(method, url)] = {
            'data': data,
            'status_code': status_code,
        }

    async def get(
        self,
        url: str,
        headers: dict | None = None,
        params: dict | None = None,
        timeout: int = 180,
    ) -> dict:
        response: dict = self._responses[('get', url)]
        status_code: int = response.get('status_code')
        if 400 <= status_code <= 500:
            raise HTTPClientException(status_code=status_code, error='http error')

        return response

    async def post(
        self,
        url: str,
        headers: dict | None = None,
        params: dict | None = None,
        data: dict | None = None,
        json: dict | None = None,
        timeout: int = 180,
    ) -> dict:
        response: dict = self._responses[('post', url)]
        status_code: int = response.get('status_code')
        if 400 <= status_code <= 500:
            raise HTTPClientException(status_code=status_code, error='http error')

        return response

    async def patch(
        self,
        url: str,
        headers: dict | None = None,
        params: dict | None = None,
        data: dict | None = None,
        json: dict | None = None,
        timeout: int = 180,
    ) -> dict:
        response: dict = self._responses[('patch', url)]
        status_code: int = response.get('status_code')
        if 400 <= status_code <= 500:
            raise HTTPClientException(status_code=status_code, error='http error')

        return response
