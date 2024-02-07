from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import get_current_user
from app.models.order import OrderItem
from app.models.user import User
from app.selectors.review import selector_reviews_for_product
from app.serializers.review import ReviewCreate
from app.services.review import service_create_review

router = APIRouter()


@router.get("/{product_id}")
async def get_reviews_for_product_endpoint(
    product_id: int,
    db: Session = Depends(get_db),
):
    reviews = selector_reviews_for_product(db, product_id)

    if not reviews:
        raise HTTPException(status_code=404, detail="No reviews found for the specified product")

    return reviews


@router.post("/", response_model=None)
async def post_review(
        review_data: ReviewCreate,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db),
):
    order_item = db.query(OrderItem).get(review_data.order_item_id)

    if not order_item:
        raise HTTPException(status_code=404, detail="Order item not found")

    # Ensure the order item is associated with the current user
    if order_item.order.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="You are not allowed to review this order item")

    # Check if the order item already has a review
    if order_item.review:
        raise HTTPException(status_code=400, detail="Review already submitted for this order item")

    # Create the review
    review = service_create_review(db=db, review_data=review_data, order_item=order_item, user=current_user)

    return review
