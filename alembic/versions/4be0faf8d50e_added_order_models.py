"""Added Order Models

Revision ID: 4be0faf8d50e
Revises: 376d527d8824
Create Date: 2023-12-14 22:10:24.134557

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '4be0faf8d50e'
down_revision: Union[str, None] = '376d527d8824'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'orders',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('status', sa.String(), nullable=False),
        sa.Column('delivery_date', sa.DateTime(timezone=True), nullable=True),
        sa.Column('shipping_address', sa.String(), nullable=False),
        sa.Column('comment', sa.String(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.Index('idx_order_user_id', 'user_id'),
    )

    op.create_table(
        'order_items',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('quantity', sa.Integer(), nullable=False),
        sa.Column('order_id', sa.Integer(), nullable=False),
        sa.Column('product_id', sa.Integer(), nullable=False),
        sa.Column('review_id', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.Index('idx_order_item_order_id', 'order_id'),
        sa.Index('idx_order_item_product_id', 'product_id'),
        sa.UniqueConstraint('order_id', 'product_id', name='uq_order_item_order_product'),
        sa.CheckConstraint('quantity >= 0', name='check_quantity_non_negative')
    )

    op.create_table(
        'reviews',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('rating', sa.Float(), nullable=False),
        sa.Column('comment', sa.String(), nullable=True),
        sa.Column('order_item_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.Index('idx_review_order_item_id', 'order_item_id')
    )


def downgrade():
    op.drop_table('reviews')
    op.drop_table('order_items')
    op.drop_table('orders')
