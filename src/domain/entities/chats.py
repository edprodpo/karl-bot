import enum
from dataclasses import (
    dataclass,
    field,
)

from src.domain.entities.base import BaseEntity


class TypeChat(enum.Enum):
    PRIVATE = 'PRIVATE'
    GROUP = 'GROUP'


@dataclass
class Chat(BaseEntity):
    chat_id: int
    title: str | None = field(
        default=None,
        kw_only=True,
    )
    type_chat: TypeChat = field(
        default=TypeChat.PRIVATE,
        kw_only=True,
    )
    is_active: bool = field(
        default=False,
        kw_only=True,
    )

    def __hash__(self) -> int:
        return hash(self.chat_id)

    def __eq__(self, __value: 'Chat') -> bool:
        return self.chat_id == __value.chat_id
