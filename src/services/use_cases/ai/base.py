from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from src.domain.entities.chats import (
    Chat,
    TypeChat,
)
from src.domain.entities.messages import Message
from src.domain.entities.users import User
from src.services.chats.base import BaseChatService
from src.services.clients.ai_clients.base import BaseAIClient
from src.services.exceptions.chats import ChatNotFoundException
from src.services.messages.base import BaseMessageService
from src.services.users.base import BaseUserService
from src.services.vk_service.base import BaseVKService


@dataclass
class BaseGenerateResponseUseCase(ABC):
    ai_client: BaseAIClient
    chat_service: BaseChatService
    vk_service: BaseVKService
    message_service: BaseMessageService
    user_service: BaseUserService

    async def _get_or_create_chat(
        self,
        chat_id: int,
        title: str | None,
        type_chat: TypeChat,
        is_active: bool = False,
    ) -> Chat:
        try:
            chat: Chat = await self.chat_service.get_by_chat_id(chat_id=chat_id)

            return chat

        except ChatNotFoundException:
            if title is None:
                title: str | None = await self.vk_service.get_chat_title(chat_id=chat_id)

                if title is None:
                    return None

            chat: Chat = Chat(
                chat_id=chat_id,
                title=title,
                type_chat=type_chat,
                is_active=is_active,
            )
            created_chat: Chat = await self.chat_service.create(chat=chat)

            return created_chat

    async def _create_message(
        self,
        request: str,
        response: str,
        user_vk_id: int,
        chat_id: int,
    ) -> None:
        message: Message = Message(
            request=request,
            response=response,
        )
        await self.message_service.create(
            message=message,
            user_vk_id=user_vk_id,
            chat_id=chat_id,
        )

    async def _update_user_by_vk_id(
        self,
        vk_id: int,
        thread_id: str | None = None,
    ) -> None:
        if thread_id:
            await self.user_service.update_thread_id_by_vk_id(
                vk_id=vk_id,
                thread_id=thread_id,
            )

    @abstractmethod
    async def execute(
        self,
        request: str,
        user: User,
        chat_id: int,
    ) -> str:
        ...
