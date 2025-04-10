from typing import TYPE_CHECKING, List

from litestar import Controller, delete, get, post, put
from litestar.dto.msgspec_dto import MsgspecDTO
from litestar.exceptions import NotFoundException

from apps.users.core.services.dto.create_user_dto import CreateUserDTO
from apps.users.core.services.dto.return_user_dto import ReturnUserDTO
from apps.users.core.services.dto.update_user_dto import UpdateUserDTO
from apps.users.core.services.user_service import UserService
from apps.users.db.repository import SQLAlchemyUserRepository

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class UserController(Controller):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.repository_class = SQLAlchemyUserRepository
        self.user_service_class = UserService

    @get(return_dto=MsgspecDTO[List[ReturnUserDTO]])
    async def get_users(self, db_session: "AsyncSession") -> list[ReturnUserDTO]:
        repository = self.repository_class(db_session)
        user_service = self.user_service_class(repository)
        return await user_service.get_all_users()

    @get("/{user_id:int}", return_dto=MsgspecDTO[ReturnUserDTO])
    async def get_user(self, user_id: int, db_session: "AsyncSession") -> ReturnUserDTO:
        repository = self.repository_class(db_session)
        user_service = self.user_service_class(repository)
        user = await user_service.get_user_by_id(user_id)
        if not user:
            raise NotFoundException(f"User with ID {user_id} not found")
        return user

    @post(dto=MsgspecDTO[CreateUserDTO], return_dto=MsgspecDTO[ReturnUserDTO])
    async def create_user(
        self, data: CreateUserDTO, db_session: "AsyncSession"
    ) -> ReturnUserDTO:
        repository = self.repository_class(db_session)
        user_service = self.user_service_class(repository)
        return await user_service.create_user(data)

    @put(
        "/{user_id:int}",
        dto=MsgspecDTO[UpdateUserDTO],
        return_dto=MsgspecDTO[ReturnUserDTO],
    )
    async def update_user(
        self, user_id: int, data: UpdateUserDTO, db_session: "AsyncSession"
    ) -> ReturnUserDTO:
        repository = self.repository_class(db_session)
        user_service = self.user_service_class(repository)
        user = await user_service.update_user(user_id, data)
        if not user:
            raise NotFoundException(f"User with ID {user_id} not found")
        return user

    @delete("/{user_id:int}")
    async def delete_user(self, user_id: int, db_session: "AsyncSession") -> None:
        repository = self.repository_class(db_session)
        user_service = self.user_service_class(repository)
        is_success = await user_service.delete_user(user_id)
        if not is_success:
            raise NotFoundException(f"User with ID {user_id} not found")
