from vkbottle.bot import (
    BotLabeler,
    Message,
)

from src.application.rules.chat import PrivateRule


labeler = BotLabeler(auto_rules=[PrivateRule()])


@labeler.message()
async def pass_handler(message: Message):
    return await message.answer(
        message='Нейрокуратор вам доступен бесплатно только в общем чате вашего потока только на время обучения. Для того, чтобы задать вопрос, напишите сообщение в чат потока согласно инструкции.', # noqa
    )
