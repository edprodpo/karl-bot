from dataclasses import dataclass

from src.domain.entities.users import User
from src.project.configs import settings
from src.services.clients.http_clients.base import BaseHTTPClient
from src.services.exceptions.http_clients import HTTPClientException
from src.services.exceptions.users import (
    UserExistException,
    UserNotFoundException,
)
from src.services.users.base import BaseUserService
from src.services.users.converters import (
    convert_user_from_dict,
    convert_user_to_dict,
)


@dataclass
class AdminAPIUserService(BaseUserService):
    client: BaseHTTPClient

    @property
    def _auth_header(self) -> dict:
        return {'Authorization': f'Bearer {settings.ADMIN_API_TOKEN}'}

    async def create(self, user: User) -> User:
        try:
            response: dict = await self.client.post(
                url=f'{settings.ADMIN_API_URL}/v1/users/',
                headers=self._auth_header,
                json=convert_user_to_dict(user=user),
            )
            result: User = convert_user_from_dict(response.get('data'))

            return result

        except HTTPClientException as error:
            if error.status_code == 400:
                raise UserExistException(vk_id=user.vk_id)

            raise

    async def get_by_vk_id(self, vk_id: int) -> User:
        try:
            response: dict = await self.client.get(
                url=f'{settings.ADMIN_API_URL}/v1/users/{vk_id}/',
                headers=self._auth_header,
            )
            result: User = convert_user_from_dict(response.get('data'))

            return result

        except HTTPClientException as error:
            if error.status_code == 404:
                raise UserNotFoundException(vk_id=vk_id)

            raise

    async def update_thread_id_by_vk_id(self, vk_id: int, thread_id: str) -> User:
        try:
            response: dict = await self.client.patch(
                url=f'{settings.ADMIN_API_URL}/v1/users/{vk_id}/',
                headers=self._auth_header,
                json={'thread_id': thread_id},
            )
            result: User = convert_user_from_dict(response.get('data'))

            return result

        except HTTPClientException as error:
            if error.status_code == 404:
                raise UserNotFoundException(vk_id=vk_id)

            raise
