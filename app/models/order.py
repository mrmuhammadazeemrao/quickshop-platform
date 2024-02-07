from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, UniqueConstraint, CheckConstraint, Index
from sqlalchemy.orm import relationship
from app.core.database import TimeStampedBaseModel


class Order(TimeStampedBaseModel):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, nullable=False)
    delivery_date = Column(DateTime, nullable=True)
    shipping_address = Column(String, nullable=False)
    comment = Column(String, nullable=True)

    # Define the relationship with User
    from app.models.user import User
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="orders")

    # Define the relationship with OrderItem
    order_items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")

    # Index on user_id for faster lookups
    Index("idx_order_user_id", user_id)


class OrderItem(TimeStampedBaseModel):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, nullable=False)

    # Define the relationship with Order
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    order = relationship("Order", back_populates="order_items")

    # Define the relationship with Product
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    product = relationship("Product", back_populates="order_item")

    # Define the relationship with Review
    review = relationship("Review", back_populates="order_item", uselist=False)

    # Index on order_id and product_id for faster lookups
    Index("idx_order_item_order_id", order_id)
    Index("idx_order_item_product_id", product_id)

    # Ensure that the combination of order_id and product_id is unique
    UniqueConstraint(order_id, product_id, name="uq_order_item_order_product")

    # Check constraint to ensure quantity is non-negative
    CheckConstraint("quantity >= 0", name="check_quantity_non_negative")


class Review(TimeStampedBaseModel):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Float, nullable=False)
    comment = Column(String, nullable=True)

    # Define the relationship with OrderItem
    order_item_id = Column(Integer, ForeignKey("order_items.id"), nullable=False)
    order_item = relationship("OrderItem", back_populates="review")
