"""Added Cart Models

Revision ID: 376d527d8824
Revises: a208ed1d41d9
Create Date: 2023-12-14 21:47:09.187899

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '376d527d8824'
down_revision: Union[str, None] = 'a208ed1d41d9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'carts',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('status', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.Index('idx_cart_user_id', 'user_id'),
        sa.UniqueConstraint('user_id', 'status', name='uq_cart_user_status')
    )

    op.create_table(
        'cart_items',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('quantity', sa.Integer(), nullable=False),
        sa.Column('cart_id', sa.Integer(), nullable=False),
        sa.Column('product_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.Index('idx_cart_item_cart_id', 'cart_id'),
        sa.Index('idx_cart_item_product_id', 'product_id'),
        sa.UniqueConstraint('cart_id', 'product_id', name='uq_cart_item_cart_product'),
        sa.CheckConstraint('quantity >= 0', name='check_quantity_non_negative')
    )


def downgrade():
    op.drop_table('cart_items')
    op.drop_table('carts')
