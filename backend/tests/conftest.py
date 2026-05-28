from __future__ import annotations

import os

import pytest
from alembic.config import Config

from alembic import command


@pytest.fixture(scope="session", autouse=True)
def apply_migrations() -> None:
    db_url = os.environ.get("DATABASE_URL")
    if not db_url:
        raise RuntimeError("DATABASE_URL must be set for tests")

    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", db_url)

    command.upgrade(alembic_cfg, "head")
