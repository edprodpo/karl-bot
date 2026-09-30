import logging

from vkbottle import BaseMiddleware
from vkbottle.bot import Message

from punq import Container

from src.domain.entities.users import User
from src.project.containers import get_container
from src.services.use_cases.users.get_or_create import GetOrCreateUserUseCase


logger = logging.getLogger(__name__)


class GetOrCreateUserMiddleware(BaseMiddleware[Message]):
    async def pre(self) -> None:
        if self.event.from_id <= 0:
            return

        if self.event.out:
            return

        try:
            container: Container = get_container()
            use_case: GetOrCreateUserUseCase = container.resolve(GetOrCreateUserUseCase)

            user_model = await self.event.get_user()
            user: User = await use_case.execute(
                vk_id=user_model.id,
                name=f"{user_model.first_name} {user_model.last_name}",
            )
            logger.info('Пользователь получен: %s', user)

            self.send({'user': user})

        except Exception as exception:
            logger.exception('Произошла ошибка.', exc_info=exception)

            await self.event.answer(message='Произошла ошибка. Попробуйте ещё раз позже.')

            return
