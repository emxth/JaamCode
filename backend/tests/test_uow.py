from __future__ import annotations

from app.modules.users.service.user_service import UserService
from app.shared.uow.unit_of_work import UnitOfWork


def test_uow_rolls_back_when_not_committed() -> None:
    with UnitOfWork() as uow:
        svc = UserService(uow)
        svc.repo.create(email="test-rollback@example.com")
        # no commit -> must rollback automatically

    with UnitOfWork() as uow2:
        svc2 = UserService(uow2)
        assert svc2.repo.exists_by_email("test-rollback@example.com") is False


def test_uow_commits_when_committed() -> None:
    with UnitOfWork() as uow:
        svc = UserService(uow)
        svc.register_user(email="test-commit@example.com")

    with UnitOfWork() as uow2:
        svc2 = UserService(uow2)
        assert svc2.repo.exists_by_email("test-commit@example.com") is True
