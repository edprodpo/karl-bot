import pytest
from faker import Faker

from src.services.vk_service.base import BaseVKService


@pytest.mark.asyncio
async def test_vk_service_get_chat_title_success(
    vk_service: BaseVKService,
    faker: Faker,
):
    chat_id: int = faker.random_int()
    title: str = faker.text()
    vk_service._set_title(chat_id, title)

    result: str = await vk_service.get_chat_title(chat_id=chat_id)

    assert result == title, f'{result=}'


@pytest.mark.asyncio
async def test_vk_service_get_chat_title_none(
    vk_service: BaseVKService,
    faker: Faker,
):
    result: None = await vk_service.get_chat_title(chat_id=faker.random_int())

    assert result is None, f'{result=}'
