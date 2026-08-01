"""remove user_id column

Revision ID: 5b3a4e4aa26d
Revises: b66c71c36ee9
Create Date: 2026-08-01 17:07:25.245183

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5b3a4e4aa26d'
down_revision: Union[str, Sequence[str], None] = 'b66c71c36ee9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
