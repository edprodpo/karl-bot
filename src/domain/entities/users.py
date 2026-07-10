from dataclasses import (
    dataclass,
    field,
)

from src.domain.entities.base import BaseEntity


@dataclass
class User(BaseEntity):
    vk_id: int
    email: str | None = field(
        default=None,
        kw_only=True,
    )
    name: str | None = field(
        default=None,
        kw_only=True,
    )
    thread_id: str | None = field(
        default=None,
        kw_only=True,
    )

    def set_thread_id(self, thread_id: str) -> None:
        self.thread_id = thread_id

    def __hash__(self) -> int:
        return hash(self.vk_id)

    def __eq__(self, __value: 'User') -> bool:
        return self.vk_id == __value.vk_id
