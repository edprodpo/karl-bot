from vkbottle import BaseMiddleware
from vkbottle.bot import Message

from punq import Container

from src.domain.entities.users import User
from src.project.containers import get_container
from src.services.use_cases.users.get_or_create import GetOrCreateUserUseCase


class GetOrCreateUserMiddleware(BaseMiddleware[Message]):
    async def pre(self) -> None:
        container: Container = get_container()
        use_case: GetOrCreateUserUseCase = container.resolve(GetOrCreateUserUseCase)

        user_model = await self.event.get_user()
        user: User = await use_case.execute(
            vk_id=user_model.id,
            name=f"{user_model.first_name} {user_model.last_name}",
        )

        self.send({'user': user})
