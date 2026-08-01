"""Merge parallel heads

Revision ID: c441ec44d588
Revises: 04c3ca33659d, 5b3a4e4aa26d, 68e0451ab0e2, 8d20496357fa
Create Date: 2026-08-01 19:13:44.129957

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c441ec44d588'
down_revision: Union[str, Sequence[str], None] = ('04c3ca33659d', '5b3a4e4aa26d', '68e0451ab0e2', '8d20496357fa')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
