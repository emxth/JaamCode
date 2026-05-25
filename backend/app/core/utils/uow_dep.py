from __future__ import annotations

from collections.abc import Generator

from app.shared.uow.unit_of_work import UnitOfWork


def get_uow() -> Generator[UnitOfWork, None, None]:
    with UnitOfWork() as uow:
        yield uow
