import re

from vkbottle.bot import Message
from vkbottle.dispatch.rules import ABCRule

from src.project.configs import settings


class PrivateRule(ABCRule[Message]):
    async def check(self, event: Message) -> bool:
        return event.peer_id < 2_000_000_000


class ChatRule(ABCRule[Message]):
    async def check(self, event: Message) -> bool:
        return event.peer_id > 2_000_000_000


class BotMentionRule(ABCRule[Message]):
    async def check(self, event: Message) -> bool:
        if event.reply_message:
            if event.reply_message.from_id == -event.group_id:
                return True

        splitted_text = re.split(r'[ ,.]+', event.text.lower())
        first_word = splitted_text[0]
        return any(first_word == word for word in settings.VK_BOT_KEYWORDS)
