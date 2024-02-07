from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index, CheckConstraint, func
from sqlalchemy.orm import relationship, Session
from app.core.database import Base, TimeStampedBaseModel
from app.models.product import Product


class Cart(TimeStampedBaseModel):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, nullable=False)

    # Define the relationship with User
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="cart")

    # Define the relationship with CartItem
    cart_items = relationship("CartItem", back_populates="cart", cascade="all, delete-orphan")

    # Index on user_id for faster lookups
    Index("idx_cart_user_id", user_id)

    # Ensure that the combination of user_id and status is unique
    UniqueConstraint(user_id, status, name="uq_cart_user_status")

    def calculate_total(self, db: Session):
        total = (
            db.query(func.sum(CartItem.quantity * Product.price))
            .join(CartItem.product)
            .filter(CartItem.cart_id == self.id)
            .scalar()
        )
        return total or 0.0


class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, nullable=False)

    # Define the relationship with Cart
    cart_id = Column(Integer, ForeignKey("carts.id"), nullable=False)
    cart = relationship("Cart", back_populates="cart_items")

    # Define the relationship with Product
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    product = relationship("Product", back_populates="cart_item")

    # Index on cart_id and product_id for faster lookups
    Index("idx_cart_item_cart_id", cart_id)
    Index("idx_cart_item_product_id", product_id)

    # Ensure that the combination of cart_id and product_id is unique
    UniqueConstraint(cart_id, product_id, name="uq_cart_item_cart_product")

    # Check constraint to ensure quantity is non-negative
    CheckConstraint("quantity >= 0", name="check_quantity_non_negative")
