"""initial

Revision ID: 8baa680e75e5
Revises:
Create Date: 2026-05-25 02:03:12.164282

"""

from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = "8baa680e75e5"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
