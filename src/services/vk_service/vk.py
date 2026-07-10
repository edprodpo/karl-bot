from dataclasses import dataclass

from vkbottle import API

from src.services.vk_service.base import BaseVKService


@dataclass
class VKService(BaseVKService):
    vk_api: API

    async def get_chat_title(self, chat_id: int) -> str | None:
        response = await self.vk_api.messages.get_conversations_by_id(
            peer_ids=[chat_id],
        )

        items = response.items

        if not items:
            return None

        chat_settings = items[0].chat_settings
        return chat_settings.title if chat_settings else None
