from sqlalchemy import Column, Integer, String, Float, ForeignKey, Index
from sqlalchemy.orm import relationship

from app.core.database import TimeStampedBaseModel


class Product(TimeStampedBaseModel):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    price = Column(Float, nullable=False)
    image = Column(String, nullable=False)
    description = Column(String)

    # Define the relationship with Category
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    category = relationship("Category", back_populates="products")

    order_item = relationship("OrderItem", back_populates="product")
    cart_item = relationship("CartItem", back_populates="product")


class Category(TimeStampedBaseModel):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)

    # Self-relationship for sub-categories
    parent_id = Column(Integer, ForeignKey("categories.id"))
    parent = relationship("Category", back_populates="sub_categories", remote_side=[id])
    sub_categories = relationship("Category", back_populates="parent")

    # Define the relationship with Product
    products = relationship("Product", back_populates="category")

    # Define the relationship with CampaignItem
    campaign_items = relationship("CampaignItem", back_populates="category")

    # Index on title for faster lookups
    Index("idx_category_title", title)


class CampaignItem(TimeStampedBaseModel):
    __tablename__ = "campaign_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    image = Column(String, nullable=False)

    # Define the relationships with Category and Campaign
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    category = relationship("Category", back_populates="campaign_items")

    campaign_id = Column(Integer, ForeignKey("campaigns.id"), nullable=False)
    campaign = relationship("Campaign", back_populates="campaign_items")

    # Index on title for faster lookups
    Index("idx_campaign_item_title", title)


class Campaign(TimeStampedBaseModel):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)

    # Define the relationship with CampaignItem
    campaign_items = relationship("CampaignItem", back_populates="campaign")

    # Index on title for faster lookups
    Index("idx_campaign_title", title)
