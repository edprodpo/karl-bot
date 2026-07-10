from vkbottle.bot import Bot

from src.application.handlers.group_chat import labeler as group_chat_labeler
from src.application.handlers.private_chat import labeler as private_chat_labeler
from src.application.middlewares.texts import TextProviderMiddleware
from src.application.middlewares.users import GetOrCreateUserMiddleware
from src.project.configs import settings


def register_middlewares(bot: Bot) -> None:
    bot.labeler.message_view.register_middleware(GetOrCreateUserMiddleware)
    bot.labeler.message_view.register_middleware(TextProviderMiddleware)


def load_labelers(bot: Bot) -> None:
    bot.labeler.load(private_chat_labeler)
    bot.labeler.load(group_chat_labeler)


def init_vk_bot() -> Bot:
    bot = Bot(token=settings.VK_API_KEY)

    register_middlewares(bot=bot)
    load_labelers(bot=bot)

    return bot
