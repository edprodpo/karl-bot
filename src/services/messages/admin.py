from dataclasses import dataclass
from mailbox import Message

from src.project.configs import settings
from src.services.clients.http_clients.base import BaseHTTPClient
from src.services.messages.base import BaseMessageService
from src.services.messages.converters import convert_message_to_dict_w_vk_id


@dataclass
class AdminAPIMessageService(BaseMessageService):
    client: BaseHTTPClient

    @property
    def _auth_header(self) -> dict:
        return {'Authorization': f'Bearer {settings.ADMIN_API_TOKEN}'}

    async def create(
        self,
        message: Message,
        user_vk_id: int,
        chat_id: int,
    ) -> None:
        await self.client.post(
            url=f'{settings.ADMIN_API_URL}/v1/chats/{chat_id}/messages/',
            headers=self._auth_header,
            json=convert_message_to_dict_w_vk_id(message=message, vk_id=user_vk_id),
        )
