from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass
from mailbox import Message


@dataclass
class BaseMessageService(ABC):
    @abstractmethod
    async def create(
        self,
        message: Message,
        user_vk_id: int,
        chat_id: int,
    ) -> None:
        ...
