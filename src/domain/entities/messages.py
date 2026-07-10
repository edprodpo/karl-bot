from dataclasses import (
    dataclass,
    field,
)

from src.domain.entities.base import BaseEntity


@dataclass
class Message(BaseEntity):
    request: str
    response: str | None = field(
        default=None,
        kw_only=True,
    )

    def add_response(self, response: str) -> None:
        self.response = response
