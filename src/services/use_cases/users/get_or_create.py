from dataclasses import dataclass

from src.domain.entities.users import User
from src.services.exceptions.users import UserNotFoundException
from src.services.users.base import BaseUserService


@dataclass
class GetOrCreateUserUseCase:
    user_service: BaseUserService

    async def execute(
        self,
        vk_id: int,
        name: str,
        email: str | None = None,
    ) -> User:
        try:
            user: User = await self.user_service.get_by_vk_id(vk_id=vk_id)
            return user

        except UserNotFoundException:
            created_user: User = await self.user_service.create(
                user=User(vk_id=vk_id, email=email, name=name),
            )

            return created_user
