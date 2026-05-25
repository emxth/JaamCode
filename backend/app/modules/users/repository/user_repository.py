from __future__ import annotations

import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.users.models.user import User
from app.shared.repository.base import BaseRepository


class UserRepository(BaseRepository[User]):
    def __init__(self, db: Session) -> None:
        super().__init__(db, User)

    def get_by_email(self, email: str) -> User | None:
        stmt = select(User).where(User.email == email, User.deleted_at.is_(None))
        return self.db.execute(stmt).scalar_one_or_none()

    def exists_by_email(self, email: str) -> bool:
        stmt = select(User.id).where(User.email == email, User.deleted_at.is_(None)).limit(1)
        return self.db.execute(stmt).scalar_one_or_none() is not None

    def create(self, *, email: str) -> User:
        user = User(id=uuid.uuid4(), email=email)
        self.add(user)
        return user

    def get_by_id(self, user_id: uuid.UUID) -> User | None:
        stmt = select(User).where(User.id == user_id, User.deleted_at.is_(None))
        return self.db.execute(stmt).scalar_one_or_none()
