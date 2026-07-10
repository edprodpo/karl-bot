from dataclasses import (
    dataclass,
    field,
)

from src.domain.entities.users import User
from src.services.clients.ai_clients.base import BaseAIClient
from src.services.exceptions.ai_clients import AIBadRequestException


@dataclass
class MemoryAIClient(BaseAIClient):
    _response: str | None = field(
        default=None,
        kw_only=True,
    )

    def _set_response(self, response: str) -> None:
        self._response = response

    async def generate_response(self, request: str, user: User) -> str:
        if self._response is None:
            raise AIBadRequestException(error='error')

        return self._response
