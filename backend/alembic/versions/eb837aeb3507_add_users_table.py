"""legacy no-op revision

Revision ID: eb837aeb3507
Revises: 04fa72ce79d8
Create Date: 2026-05-25 19:09:41.148222

"""

from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = "eb837aeb3507"
down_revision: str | Sequence[str] | None = "04fa72ce79d8"
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
