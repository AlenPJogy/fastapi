"""remove comment table

Revision ID: 68e0451ab0e2
Revises: b66c71c36ee9
Create Date: 2026-08-01 19:02:57.403073

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '68e0451ab0e2'
down_revision: Union[str, Sequence[str], None] = 'b66c71c36ee9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_table('comments')
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.create_table('comments',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('comment', sa.String(), nullable=False, server_default='no comments yet'),
        sa.Column('post_id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
        )
    pass
