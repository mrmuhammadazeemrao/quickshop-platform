from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import authenticate_user
from app.models.user import User
from app.selectors.order import selector_get_user_orders
from app.serializers.order import OrderRead, PlaceOrderRequest
from app.services.order import service_place_order

router = APIRouter()


@router.get("/my_orders", response_model=List[OrderRead])
async def get_user_orders(
        current_user: User = Depends(authenticate_user),
        db: Session = Depends(get_db)
):
    """
    Get orders for the authenticated user.
    """
    orders = selector_get_user_orders(db, current_user)
    return orders


@router.post("/place_order")
async def place_order(
        request_data: PlaceOrderRequest,
        current_user: User = Depends(authenticate_user),
        db: Session = Depends(get_db)
):
    """
    Place an order for the items in the cart.
    """
    order = service_place_order(db, current_user, request_data.shipping_address)
    if not order:
        raise HTTPException(status_code=400, detail="Could not place the order")

    return {"message": "Order placed successfully", "order_id": order.id}
