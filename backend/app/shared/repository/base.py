from __future__ import annotations

from typing import TypeVar

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database.base import Base
from app.shared.utils.datetime import now_utc

ModelT = TypeVar("ModelT", bound=Base)


class BaseRepository[ModelT]:
    def __init__(self, db: Session, model: type[ModelT]) -> None:
        self.db = db
        self.model = model

    def add(self, entity: ModelT) -> ModelT:
        self.db.add(entity)
        return entity

    # def get_by_id(self, entity_id: uuid.UUID) -> ModelT | None:
    #     stmt = select(self.model).where(self.model.id == entity_id)

    #     # If model has deleted_at, exclude deleted rows by default
    #     if hasattr(self.model, "deleted_at"):
    #         stmt = stmt.where(self.model.deleted_at.is_(None))  # type: ignore[attr-defined]

    #     return self.db.execute(stmt).scalar_one_or_none()

    def list(self, *, limit: int = 50, offset: int = 0) -> list[ModelT]:
        stmt = select(self.model).limit(limit).offset(offset)

        if hasattr(self.model, "deleted_at"):
            stmt = stmt.where(self.model.deleted_at.is_(None))  # type: ignore[attr-defined]

        return list(self.db.execute(stmt).scalars().all())

    def delete_soft(self, entity: ModelT) -> None:
        if hasattr(entity, "deleted_at"):
            entity.deleted_at = now_utc()  # type: ignore[attr-defined]
        else:
            self.db.delete(entity)

    def delete_hard(self, entity: ModelT) -> None:
        self.db.delete(entity)
