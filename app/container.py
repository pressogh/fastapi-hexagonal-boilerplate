from dependency_injector import containers, providers
from dependency_injector.containers import DeclarativeContainer

from app.file.container import FileContainer
from app.user.container import UserContainer


class AppContainer(DeclarativeContainer):
    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration(
        packages=[
            "app.file.adapter.input.api.v1",
            "app.user.adapter.input.api.v1",
        ]
    )

    file = providers.Container(FileContainer)
    user = providers.Container(UserContainer)
