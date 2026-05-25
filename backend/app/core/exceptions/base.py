from dataclasses import dataclass


@dataclass(frozen=True)
class DomainError(Exception):
    code: str
    message: str
    http_status: int = 400
