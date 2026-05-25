from __future__ import annotations

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database.base import Base
from app.shared.models.mixins import AuditMixin, BaseModelMixin, SoftDeleteMixin, TimestampMixin


class User(Base, BaseModelMixin, TimestampMixin, SoftDeleteMixin, AuditMixin):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(320), unique=True, index=True, nullable=False)
