from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass


@dataclass
class BaseHTTPClient(ABC):
    @abstractmethod
    async def get(
        self,
        url: str,
        headers: dict | None = None,
        params: dict | None = None,
        timeout: int = 180,
    ) -> dict:
        ...

    @abstractmethod
    async def post(
        self,
        url: str,
        headers: dict | None = None,
        params: dict | None = None,
        data: dict | None = None,
        json: dict | None = None,
        timeout: int = 180,
    ) -> dict:
        ...

    @abstractmethod
    async def patch(
        self,
        url: str,
        headers: dict | None = None,
        params: dict | None = None,
        data: dict | None = None,
        json: dict | None = None,
        timeout: int = 180,
    ) -> dict:
        ...
