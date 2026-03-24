from dependency_injector import containers, providers

from app.file.adapter.output.persistence.repository_adapter import (
    FileRepositoryAdapter,
)
from app.file.adapter.output.persistence.sqlalchemy.file import (
    FileSQLAlchemyRepository,
)
from app.file.application.service.file import FileService


class FileContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=["app.file.adapter.input.api.v1.file"]
    )

    sqlalchemy_repository = providers.Singleton(FileSQLAlchemyRepository)
    repository = providers.Factory(
        FileRepositoryAdapter,
        repository=sqlalchemy_repository,
    )
    service = providers.Factory(FileService, repository=repository)
