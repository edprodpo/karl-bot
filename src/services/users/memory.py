from dataclasses import (
    dataclass,
    field,
)

from src.domain.entities.users import User
from src.services.exceptions.users import (
    UserExistException,
    UserNotFoundException,
)
from src.services.users.base import BaseUserService


@dataclass
class MemoryUserService(BaseUserService):
    _users: list[User] = field(
        default_factory=list,
        kw_only=True,
    )

    async def create(self, user: User) -> User:
        if any(existing_user for existing_user in self._users if existing_user == user):
            raise UserExistException(vk_id=user.vk_id)

        self._users.append(user)

        return user

    async def get_by_vk_id(self, vk_id: int) -> User:
        try:
            return next(user for user in self._users if user.vk_id == vk_id)

        except StopIteration:
            raise UserNotFoundException(vk_id=vk_id)

    async def update_thread_id_by_vk_id(self, vk_id: int, thread_id: str) -> User:
        try:
            user: User = next(user for user in self._users if user.vk_id == vk_id)
            user.set_thread_id(thread_id=thread_id)

            return user

        except StopIteration:
            raise UserNotFoundException(vk_id=vk_id)
