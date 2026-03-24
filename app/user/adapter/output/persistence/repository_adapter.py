from collections.abc import Sequence
from uuid import UUID

from app.user.domain.entity.user import User
from app.user.domain.repository.user import UserRepository


class UserRepositoryAdapter:
    def __init__(self, *, repository: UserRepository):
        self.repository = repository

    async def get_by_id(self, user_id: UUID) -> User | None:
        return await self.repository.get_by_id(user_id)

    async def get_by_username(self, username: str) -> User | None:
        return await self.repository.get_by_username(username)

    async def get_by_email(self, email: str) -> User | None:
        return await self.repository.get_by_email(email)

    async def list(self) -> Sequence[User]:
        return await self.repository.list()

    async def save(self, user: User) -> User:
        return await self.repository.save(user)
