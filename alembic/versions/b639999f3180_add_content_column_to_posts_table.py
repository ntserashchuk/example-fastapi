"""add content column to posts table

Revision ID: b639999f3180
Revises: 70712d24b7c3
Create Date: 2025-02-28 14:32:22.111682

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b639999f3180'
down_revision: Union[str, None] = '70712d24b7c3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
