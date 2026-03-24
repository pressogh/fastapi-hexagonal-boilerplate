from uuid import UUID

from app.file.domain.entity.file import File
from app.file.domain.repository.file import FileRepository


class FileRepositoryAdapter:
    def __init__(self, *, repository: FileRepository):
        self.repository = repository

    async def get_by_id(self, file_id: UUID) -> File | None:
        return await self.repository.get_by_id(file_id)

    async def list(self) -> list[File]:
        return await self.repository.list()

    async def save(self, file: File) -> File:
        return await self.repository.save(file)
