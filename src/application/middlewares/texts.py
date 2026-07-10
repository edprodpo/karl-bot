from vkbottle import BaseMiddleware
from vkbottle.bot import Message

from src.application.common.texts import text_provider


class TextProviderMiddleware(BaseMiddleware[Message]):
    async def pre(self) -> None:
        self.send({'text_provider': text_provider})
