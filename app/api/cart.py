from http.client import HTTPException

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import authenticate_user
from app.models.user import User
from app.selectors.product import selector_get_product
from app.serializers.cart import CartRead, AddToCartRequest
from app.services.cart import service_get_or_create_user_cart, service_add_to_cart, service_remove_from_cart

router = APIRouter()


@router.get("/my_cart", response_model=CartRead)
async def my_cart(current_user: User = Depends(authenticate_user), db: Session = Depends(get_db)):
    user_cart = service_get_or_create_user_cart(db, current_user)
    user_cart.total = user_cart.calculate_total(db)

    return user_cart


@router.post("/add_to_cart", response_model=CartRead)
async def add_to_cart(
        request_data: AddToCartRequest,
        current_user: User = Depends(authenticate_user),
        db: Session = Depends(get_db)
):
    product = selector_get_product(db, request_data.product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    user_cart = service_get_or_create_user_cart(db, current_user)
    user_cart = service_add_to_cart(db, user_cart, request_data)
    user_cart.total = user_cart.calculate_total(db)

    return user_cart


@router.delete("/remove_from_cart/{product_id}", response_model=CartRead)
async def remove_from_cart(
        product_id: int,
        current_user: User = Depends(authenticate_user),
        db: Session = Depends(get_db)
):
    product = selector_get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    user_cart = service_get_or_create_user_cart(db, current_user)
    user_cart = service_remove_from_cart(db, user_cart, product_id)
    user_cart.total = user_cart.calculate_total(db)

    return user_cart
