"""add content column to posts table

Revision ID: 18905365a79e
Revises: 98645a4146be
Create Date: 2025-12-06 16:40:13.923872

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '18905365a79e'
down_revision: Union[str, Sequence[str], None] = '98645a4146be'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(),nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
