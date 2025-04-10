from typing import List, Optional
import hashlib
import secrets

from apps.users.core.models.user import User
from apps.users.core.repositories.user_repository import IUserRepository
from apps.users.core.services.dto.create_user_dto import CreateUserDTO
from apps.users.core.services.dto.return_user_dto import ReturnUserDTO
from apps.users.core.services.dto.update_user_dto import UpdateUserDTO


class UserService:
    def __init__(self, repository: IUserRepository):
        self._repository = repository

    def _hash_password(self, password: str) -> str:
        salt = secrets.token_hex(16)
        hashed = hashlib.sha256((password + salt).encode()).hexdigest()
        return f"{salt}:{hashed}"

    def _verify_password(self, password: str, stored_hash: str) -> bool:
        salt, stored_hash = stored_hash.split(":")
        hashed = hashlib.sha256((password + salt).encode()).hexdigest()
        return hashed == stored_hash

    def _user_to_return_user_dto(self, user: User) -> ReturnUserDTO:
        return ReturnUserDTO(
            id=user.id,
            name=user.name,
            surname=user.surname,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

    async def create_user(self, create_user_dto: CreateUserDTO) -> ReturnUserDTO:
        hashed_password = self._hash_password(create_user_dto.password)
        create_user_dto.password = hashed_password
        user = await self._repository.create(create_user_dto)
        return self._user_to_return_user_dto(user)

    async def get_all_users(self) -> List[ReturnUserDTO]:
        users = await self._repository.get_all()
        return [self._user_to_return_user_dto(user) for user in users]

    async def get_user_by_id(self, user_id: int) -> Optional[ReturnUserDTO]:
        user = await self._repository.get_by_id(user_id)
        if user:
            return self._user_to_return_user_dto(user)
        return None

    async def get_user_by_name(self, name: str) -> Optional[ReturnUserDTO]:
        user = await self._repository.get_by_name(name)
        if user:
            return self._user_to_return_user_dto(user)
        return None

    async def update_user(
        self, user_id: int, update_data: UpdateUserDTO
    ) -> Optional[ReturnUserDTO]:
        update_dict = {k: v for k, v in update_data.__dict__.items() if v is not None}
        if "password" in update_dict:
            update_dict["password"] = self._hash_password(update_dict["password"])
        user = await self._repository.update(user_id, **update_dict)
        if user:
            return self._user_to_return_user_dto(user)
        return None

    async def delete_user(self, user_id: int) -> bool:
        return await self._repository.delete(user_id)
