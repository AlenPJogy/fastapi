"""add comments table

Revision ID: 8d20496357fa
Revises: 04ddfd0738c2
Create Date: 2026-08-01 15:52:00.269823

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8d20496357fa'
down_revision: Union[str, Sequence[str], None] = '04ddfd0738c2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
