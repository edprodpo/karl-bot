from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from src.domain.entities.users import User


@dataclass
class BaseUserService(ABC):
    @abstractmethod
    async def create(self, user: User) -> User:
        ...

    @abstractmethod
    async def get_by_vk_id(self, vk_id: int) -> User:
        ...

    @abstractmethod
    async def update_thread_id_by_vk_id(self, vk_id: int, thread_id: str) -> User:
        ...
