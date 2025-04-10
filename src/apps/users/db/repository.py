from typing import List, Optional

from msgspec.structs import asdict
from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from apps.users.core.models.user import User
from apps.users.core.repositories.user_repository import IUserRepository
from apps.users.core.services.dto.create_user_dto import CreateUserDTO
from apps.users.core.services.dto.update_user_dto import UpdateUserDTO
from apps.users.db.models import UserModel


class SQLAlchemyUserRepository(IUserRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(self, user: CreateUserDTO) -> User:
        user_data = asdict(user)
        db_user = UserModel(**user_data)
        self._session.add(db_user)
        await self._session.commit()
        await self._session.refresh(db_user)
        return User(
            id=db_user.id,
            name=db_user.name,
            surname=db_user.surname,
            password=db_user.password,
            created_at=db_user.created_at,
            updated_at=db_user.updated_at,
        )

    async def get_all(self) -> List[User]:
        stmt = select(UserModel)
        result = await self._session.execute(stmt)
        users = result.scalars().all()

        return [
            User(
                id=user.id,
                name=user.name,
                surname=user.surname,
                password=user.password,
                created_at=user.created_at,
                updated_at=user.updated_at,
            )
            for user in users
        ]

    async def get_by_id(self, user_id: int) -> Optional[User]:
        stmt = select(UserModel).where(UserModel.id == user_id)
        result = await self._session.execute(stmt)
        user = result.scalar_one_or_none()
        if not user:
            return None

        return User(
            id=user.id,
            name=user.name,
            surname=user.surname,
            password=user.password,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

    async def get_by_name(self, name: str) -> Optional[User]:
        stmt = select(UserModel).where(UserModel.name == name)
        result = await self._session.execute(stmt)
        user = result.scalar_one_or_none()
        if not user:
            return None
        return User(
            id=user.id,
            name=user.name,
            surname=user.surname,
            password=user.password,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

    async def update(self, user_id: int, user: UpdateUserDTO) -> Optional[User]:
        update_values = asdict(user)
        stmt = update(UserModel).where(UserModel.id == user_id).values(**update_values)
        await self._session.execute(stmt)
        await self._session.commit()
        return await self.get_by_id(user_id)

    async def delete(self, user_id: int) -> bool:
        stmt = delete(UserModel).where(UserModel.id == user_id)
        result = await self._session.execute(stmt)
        await self._session.commit()
        return result.rowcount > 0
