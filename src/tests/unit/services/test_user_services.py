import pytest
from faker import Faker

from src.domain.entities.users import User
from src.services.exceptions.users import (
    UserExistException,
    UserNotFoundException,
)
from src.services.users.base import BaseUserService
from src.tests.factories.users import UserFactory


@pytest.mark.asyncio
async def test_user_service_create_success(user_service: BaseUserService):
    user: User = UserFactory()
    created_user: User = await user_service.create(user=user)

    assert created_user == user, f'{created_user=}'


@pytest.mark.asyncio
async def test_user_service_create_user_exist_exception(user_service: BaseUserService):
    user: User = UserFactory()
    await user_service.create(user=user)

    with pytest.raises(UserExistException):
        await user_service.create(user=user)


@pytest.mark.asyncio
async def test_user_service_get_by_vk_id_success(user_service: BaseUserService):
    user: User = UserFactory()
    await user_service.create(user=user)
    result: User = await user_service.get_by_vk_id(vk_id=user.vk_id)

    assert result == user, f'{result=}'


@pytest.mark.asyncio
async def test_user_service_get_by_vk_id_not_found_exception(user_service: BaseUserService):
    user: User = UserFactory()
    with pytest.raises(UserNotFoundException):
        await user_service.get_by_vk_id(vk_id=user.vk_id)


@pytest.mark.asyncio
async def test_user_service_update_thread_id_by_vk_id_success(
    user_service: BaseUserService,
    faker: Faker,
):
    user: User = UserFactory()
    thread_id = faker.text()
    user_service._users.append(user)

    updated_user: User = await user_service.update_thread_id_by_vk_id(
        vk_id=user.vk_id,
        thread_id=thread_id,
    )

    assert updated_user == user, f'{updated_user=}'
    assert updated_user.thread_id == thread_id, f'{updated_user=}'


@pytest.mark.asyncio
async def test_user_service_update_thread_id_by_vk_id_not_found_exception(
    user_service: BaseUserService,
    faker: Faker,
):
    user: User = UserFactory()
    thread_id = faker.text()

    with pytest.raises(UserNotFoundException):
        await user_service.update_thread_id_by_vk_id(
            vk_id=user.vk_id,
            thread_id=thread_id,
        )
