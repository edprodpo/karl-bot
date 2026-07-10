import logging

from vkbottle.bot import (
    BotLabeler,
    Message,
)

import orjson
from punq import Container

from src.application.common.texts import TextProvider
from src.application.rules.chat import (
    BotMentionRule,
    ChatRule,
)
from src.domain.entities.users import User
from src.domain.exceptions.base import ApplicationException
from src.project.containers import get_container
from src.services.exceptions.chats import ChatAccessException
from src.services.use_cases.ai.generate_response import GenerateGroupChatResponseUseCase


logger = logging.getLogger(__name__)
labeler = BotLabeler(auto_rules=[ChatRule()])


@labeler.message(BotMentionRule())
async def generate_response_handler(
    message: Message,
    user: User,
    text_provider: TextProvider,
):
    container: Container = get_container()
    use_case: GenerateGroupChatResponseUseCase = container.resolve(GenerateGroupChatResponseUseCase)

    try:
        response: str = await use_case.execute(
            request=message.text,
            user=user,
            chat_id=message.peer_id,
        )
        return await message.reply(message=response)

    except ChatAccessException as error:
        logger.exception(
            msg='У данного чата нет доступа.',
            extra={'error_meta': orjson.dumps(error).decode()},
        )
        return await message.reply(message=text_provider.errors.no_chat_access())

    except ApplicationException as error:
        logger.exception(
            msg='Произошла ошибка.',
            extra={'error_meta': orjson.dumps(error).decode()},
        )
        return await message.reply(message=text_provider.errors.connection_error())


@labeler.message()
async def pass_message_handler(message: Message):
    ...
