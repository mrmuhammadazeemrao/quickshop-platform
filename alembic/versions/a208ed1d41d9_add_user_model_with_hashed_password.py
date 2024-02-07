"""Add User model with hashed password

Revision ID: a208ed1d41d9
Revises: abc123
Create Date: 2023-12-14 21:29:34.534863

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = 'a208ed1d41d9'
down_revision: Union[str, None] = 'abc123'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('email', sa.String(), nullable=True),
        sa.Column('password_hash', sa.String(), nullable=True),
        sa.Column('profile_image', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.Index('idx_user_email', 'email'),
        sa.UniqueConstraint('email', name='uq_user_email')
    )


def downgrade():
    op.drop_table('users')
