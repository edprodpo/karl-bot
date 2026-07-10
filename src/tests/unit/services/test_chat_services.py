import pytest

from src.domain.entities.chats import Chat
from src.services.chats.base import BaseChatService
from src.services.exceptions.chats import (
    ChatExistException,
    ChatNotFoundException,
)
from src.tests.factories.chats import ChatFactory


@pytest.mark.asyncio
async def test_chat_service_create_success(chat_service: BaseChatService):
    chat: Chat = ChatFactory()
    created_chat: Chat = await chat_service.create(chat=chat)

    assert created_chat == chat, f'{created_chat=}'


@pytest.mark.asyncio
async def test_chat_service_create_chat_exist_exception(chat_service: BaseChatService):
    chat: Chat = ChatFactory()

    await chat_service.create(chat=chat)

    with pytest.raises(ChatExistException):
        await chat_service.create(chat=chat)


@pytest.mark.asyncio
async def test_chat_service_get_by_chat_id_success(chat_service: BaseChatService):
    chat: Chat = ChatFactory()

    await chat_service.create(chat=chat)
    result: Chat = await chat_service.get_by_chat_id(chat_id=chat.chat_id)

    assert result == chat, f'{result=}'


@pytest.mark.asyncio
async def test_chat_service_get_by_chat_id_not_found_exception(chat_service: BaseChatService):
    chat: Chat = ChatFactory()

    with pytest.raises(ChatNotFoundException):
        await chat_service.get_by_chat_id(chat_id=chat.chat_id)
