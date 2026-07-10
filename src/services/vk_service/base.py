from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass


@dataclass
class BaseVKService(ABC):
    @abstractmethod
    async def get_chat_title(self, chat_id: int) -> str | None:
        ...
