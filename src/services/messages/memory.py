from dataclasses import (
    dataclass,
    field,
)

from src.domain.entities.messages import Message
from src.services.messages.base import BaseMessageService


@dataclass
class MemoryMessageService(BaseMessageService):
    _messages: list[Message] = field(
        default_factory=list,
        kw_only=True,
    )

    async def create(
        self,
        message: Message,
        user_vk_id: int,
        chat_id: int,
    ) -> None:
        self._messages.append(message)
