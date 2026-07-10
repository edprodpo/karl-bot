from dataclasses import dataclass

from httpx import (
    AsyncClient,
    HTTPError,
)

from src.services.clients.http_clients.base import BaseHTTPClient
from src.services.exceptions.http_clients import HTTPClientException


@dataclass
class HTTPXClient(BaseHTTPClient):
    client: AsyncClient

    async def get(
        self,
        url: str,
        headers: dict | None = None,
        params: dict | None = None,
        timeout: int = 180,
    ) -> dict:
        try:
            response = await self.client.get(
                url=url,
                headers=headers,
                params=params,
                timeout=timeout,
            )
            response.raise_for_status()

            return response.json()

        except HTTPError as error:
            raise HTTPClientException(
                status_code=error.response.status_code,
                error=error.args[0],
            )

    async def post(
        self,
        url: str,
        headers: dict | None = None,
        params: dict | None = None,
        data: dict | None = None,
        json: dict | None = None,
        timeout: int = 180,
    ) -> dict:
        try:
            response = await self.client.post(
                url=url,
                headers=headers,
                params=params,
                data=data,
                json=json,
                timeout=timeout,
            )
            response.raise_for_status()

            return response.json()

        except HTTPError as error:
            raise HTTPClientException(
                status_code=error.response.status_code,
                error=error.args[0],
            )

    async def patch(
        self,
        url: str,
        headers: dict | None = None,
        params: dict | None = None,
        data: dict | None = None,
        json: dict | None = None,
        timeout: int = 180,
    ) -> dict:
        try:
            response = await self.client.patch(
                url=url,
                headers=headers,
                params=params,
                data=data,
                json=json,
                timeout=timeout,
            )
            response.raise_for_status()

            return response.json()

        except HTTPError as error:
            raise HTTPClientException(
                status_code=error.response.status_code,
                error=error.args[0],
            )
