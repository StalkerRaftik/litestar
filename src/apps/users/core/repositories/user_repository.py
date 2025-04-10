from abc import ABC, abstractmethod
from typing import List, Optional

from apps.users.core.models.user import User
from apps.users.core.services.dto.create_user_dto import CreateUserDTO
from apps.users.core.services.dto.update_user_dto import UpdateUserDTO


class IUserRepository(ABC):
    @abstractmethod
    async def create(self, user: CreateUserDTO) -> User:
        pass

    @abstractmethod
    async def get_all(self) -> List[User]:
        pass

    @abstractmethod
    async def get_by_id(self, user_id: int) -> Optional[User]:
        pass

    @abstractmethod
    async def get_by_name(self, name: str) -> Optional[User]:
        pass

    @abstractmethod
    async def update(self, user_id: int, user: UpdateUserDTO) -> Optional[User]:
        pass

    @abstractmethod
    async def delete(self, user_id: int) -> bool:
        pass
