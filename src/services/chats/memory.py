from dataclasses import (
    dataclass,
    field,
)

from src.domain.entities.chats import Chat
from src.services.chats.base import BaseChatService
from src.services.exceptions.chats import (
    ChatExistException,
    ChatNotFoundException,
)


@dataclass
class MemoryChatService(BaseChatService):
    _chats: list[Chat] = field(
        default_factory=list,
        kw_only=True,
    )

    async def create(self, chat: Chat) -> Chat:
        if any(existing_chat for existing_chat in self._chats if existing_chat == chat):
            raise ChatExistException(chat_id=chat.chat_id)

        self._chats.append(chat)
        return chat

    async def get_by_chat_id(self, chat_id: int) -> Chat:
        try:
            return next(chat for chat in self._chats if chat.chat_id == chat_id)

        except StopIteration:
            raise ChatNotFoundException(chat_id=chat_id)
