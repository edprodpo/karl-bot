from dataclasses import dataclass

from src.domain.entities.chats import (
    Chat,
    TypeChat,
)
from src.domain.entities.users import User
from src.services.exceptions.chats import ChatAccessException
from src.services.use_cases.ai.base import BaseGenerateResponseUseCase


@dataclass
class GenerateGroupChatResponseUseCase(BaseGenerateResponseUseCase):
    async def execute(
        self,
        request: str,
        user: User,
        chat_id: int,
    ) -> str:
        chat: Chat | None = await self._get_or_create_chat(
            chat_id=chat_id,
            title=None,
            type_chat=TypeChat.GROUP,
            is_active=False,
        )

        if not chat or not chat.is_active:
            raise ChatAccessException(chat_id=chat_id)

        thread_id = user.thread_id
        response: str = await self.ai_client.generate_response(
            request=request,
            user=user,
        )

        await self._update_user_by_vk_id(
            vk_id=user.vk_id,
            thread_id=user.thread_id if thread_id != user.thread_id else None,
        )
        await self._create_message(
            request=request,
            response=response,
            user_vk_id=user.vk_id,
            chat_id=chat.chat_id,
        )

        return response
