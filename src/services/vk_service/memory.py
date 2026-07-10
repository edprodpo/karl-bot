from dataclasses import (
    dataclass,
    field,
)

from src.services.vk_service.base import BaseVKService


@dataclass
class MemoryVKService(BaseVKService):
    _title: dict[int, str] = field(
        default_factory=dict,
        kw_only=True,
    )

    def _set_title(self, chat_id: int, title: str) -> None:
        self._title[chat_id] = title

    async def get_chat_title(self, chat_id: int) -> str | None:
        return self._title.get(chat_id)
