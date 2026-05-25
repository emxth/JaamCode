from __future__ import annotations

from app.modules.users.repository.user_repository import UserRepository
from app.shared.uow.unit_of_work import UnitOfWork


class UserService:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow
        self.repo = UserRepository(uow.db)

    def register_user(self, *, email: str):
        if self.repo.exists_by_email(email):
            raise ValueError("email already exists")

        user = self.repo.create(email=email)
        self.uow.commit()
        return user
