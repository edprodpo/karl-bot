import logging
from dataclasses import dataclass

from httpx import (
    HTTPError,
    Response,
)

from src.domain.entities.users import User
from src.services.clients.ai_clients.base import BaseAIClient
from src.services.clients.http_clients.base import BaseHTTPClient
from src.services.exceptions.ai_clients import AIBadRequestException


logger = logging.getLogger(__name__)


@dataclass
class N8NClient(BaseAIClient):
    client: BaseHTTPClient
    url: str

    def _data(self, request: str, user: User) -> dict[str, str]:
        return {
            'text': request,
            'user_id': user.vk_id,
            'username': user.name,
            'first_name': user.name,
        }

    async def generate_response(self, request: str, user: User) -> str:
        try:
            response: Response = await self.client.post(
                url=self.url,
                data=self._data(request, user),
                timeout=360,
            )
            response.raise_for_status()

            json_data: dict = response.json()
            result: str = json_data.get('response')
            if result is None:
                raise AIBadRequestException(error='Нет ответа.')

            return self._strip_markdown(result)

        except HTTPError as exception:
            logger.exception('Ошибка n8n: %s', exception)
            raise AIBadRequestException(error=str(exception))
