"""create_tables

Revision ID: abc123
Revises:
Create Date: 2023-01-01 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'abc123'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'categories',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), index=True, nullable=False),
        sa.Column('parent_id', sa.Integer(), sa.ForeignKey('categories.id'), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index('idx_category_title', 'categories', ['title'], unique=False)

    op.create_table(
        'products',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), index=True, nullable=False),
        sa.Column('price', sa.Float(), nullable=False),
        sa.Column('image', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('category_id', sa.Integer(), sa.ForeignKey('categories.id'), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index('idx_product_title', 'products', ['title'], unique=False)

    op.create_table(
        'campaigns',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index('idx_campaign_title', 'campaigns', ['title'], unique=False)

    op.create_table(
        'campaign_items',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('image', sa.String(), nullable=False),
        sa.Column('category_id', sa.Integer(), sa.ForeignKey('categories.id'), nullable=False),
        sa.Column('campaign_id', sa.Integer(), sa.ForeignKey('campaigns.id'), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index('idx_campaign_item_title', 'campaign_items', ['title'], unique=False)


def downgrade():
    op.drop_table('products')
    op.drop_table('categories')
    op.drop_table('campaign_items')
    op.drop_table('campaigns')
