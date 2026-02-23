from enum import StrEnum

class ValueObject:
    """Base class for value objects."""
    pass

class TokenType(ValueObject, StrEnum):
    ACCESS = "access_token"
    REFRESH = "refresh_token"
