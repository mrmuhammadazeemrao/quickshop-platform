from sqlalchemy.orm import Session
from app.models.order import Review, OrderItem
from app.serializers.review import ReviewCreate


def service_create_review(db: Session, review_data: ReviewCreate, order_item: OrderItem, user):
    review = Review(
        rating=review_data.rating,
        comment=review_data.comment,
        order_item=order_item,
    )

    db.add(review)
    db.commit()
    db.refresh(review)

    return review
