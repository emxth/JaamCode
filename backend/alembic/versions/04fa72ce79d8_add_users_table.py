"""legacy no-op revision

Revision ID: 04fa72ce79d8
Revises: 8baa680e75e5
Create Date: 2026-05-25 19:00:56.795874

"""

from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = "04fa72ce79d8"
down_revision: str | Sequence[str] | None = "8baa680e75e5"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    # Kept to preserve published revision history.
    pass


def downgrade() -> None:
    """Downgrade schema."""
    # Kept to preserve published revision history.
    pass
