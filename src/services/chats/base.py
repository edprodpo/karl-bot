from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from src.domain.entities.chats import Chat


@dataclass
class BaseChatService(ABC):
    @abstractmethod
    async def create(self, chat: Chat) -> Chat:
        ...

    @abstractmethod
    async def get_by_chat_id(self, chat_id: int) -> Chat:
        ...
