import pytest

from src.domain.entities.chats import Chat
from src.domain.entities.messages import Message
from src.domain.entities.users import User
from src.services.messages.base import BaseMessageService
from src.tests.factories.chats import ChatFactory
from src.tests.factories.messages import MessageFactory
from src.tests.factories.users import UserFactory


@pytest.mark.asyncio
async def test_message_service_create(message_service: BaseMessageService):
    user: User = UserFactory()
    chat: Chat = ChatFactory()
    message: Message = MessageFactory()

    await message_service.create(
        message=message,
        user_vk_id=user.vk_id,
        chat_id=chat.chat_id,
    )
    result: Message = message_service._messages[0]

    assert result.request == message.request, f'{result=}'
    assert result.response == message.response, f'{result=}'
