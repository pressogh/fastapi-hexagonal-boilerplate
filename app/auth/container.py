from dependency_injector import containers, providers
from valkey.asyncio import from_url

from app.auth.adapter.output.persistence.repository_adapter import (
    RefreshTokenRepositoryAdapter,
)
from app.auth.adapter.output.persistence.valkey.refresh_token import (
    ValkeyRefreshTokenRepository,
)
from app.auth.application.service.auth import AuthService
from app.user.adapter.output.persistence.repository_adapter import (
    UserRepositoryAdapter,
)
from app.user.adapter.output.persistence.sqlalchemy.user import (
    UserSQLAlchemyRepository,
)
from core.config import config


class AuthContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=["app.auth.adapter.input.api.v1.auth"]
    )

    valkey_client = providers.Singleton(
        from_url,
        config.VALKEY_URL,
        decode_responses=True,
    )
    refresh_token_persistence = providers.Singleton(
        ValkeyRefreshTokenRepository,
        client=valkey_client,
    )
    refresh_token_repository = providers.Factory(
        RefreshTokenRepositoryAdapter,
        repository=refresh_token_persistence,
    )
    user_sqlalchemy_repository = providers.Singleton(UserSQLAlchemyRepository)
    user_repository = providers.Factory(
        UserRepositoryAdapter,
        repository=user_sqlalchemy_repository,
    )
    service = providers.Factory(
        AuthService,
        user_repository=user_repository,
        refresh_token_repository=refresh_token_repository,
    )
