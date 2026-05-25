from __future__ import annotations

import os

import pytest
from alembic.config import Config

from alembic import command


@pytest.fixture(scope="session", autouse=True)
def apply_migrations() -> None:
    """
    Ensure the test database schema is up to date before running tests.
    """
    alembic_cfg = Config("alembic.ini")

    # Optional: allow overriding DB from env in tests/CI
    db_url = os.environ.get("DATABASE_URL")
    if db_url:
        alembic_cfg.set_main_option("sqlalchemy.url", db_url)

    command.upgrade(alembic_cfg, "head")
