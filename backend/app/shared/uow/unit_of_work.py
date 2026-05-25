from __future__ import annotations

from contextlib import AbstractContextManager

from sqlalchemy.orm import Session

from app.core.database.session import SessionLocal


class UnitOfWork(AbstractContextManager["UnitOfWork"]):
    """
    Explicit-commit unit of work.

    Rule:
      - Services call uow.commit() when successful.
      - If commit is never called, we rollback on exit.
      - If an exception happens, rollback on exit.
    """

    def __init__(self) -> None:
        self.db: Session = SessionLocal()
        self._committed = False

    def commit(self) -> None:
        self.db.commit()
        self._committed = True

    def rollback(self) -> None:
        self.db.rollback()

    def close(self) -> None:
        self.db.close()

    def __exit__(self, exc_type, exc, tb) -> None:
        try:
            if exc is not None:
                self.rollback()
                return

            if not self._committed:
                self.rollback()
        finally:
            self.close()
