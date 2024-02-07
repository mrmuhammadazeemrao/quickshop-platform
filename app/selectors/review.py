from sqlalchemy.orm import Session, joinedload
from app.models.order import OrderItem, Review, Order
from app.models.user import User


def selector_reviews_for_product(db: Session, product_id: int):
    """
    Get all reviews for a product based on its ID.
    """
    reviews = (
        db.query(Review)
        .join(OrderItem)
        .join(Order)
        .join(User)
        .filter(OrderItem.product_id == product_id)
        .options(
            joinedload(Review.order_item).joinedload(OrderItem.order).joinedload(Order.user)
        )
        .all()
    )

    return reviews
