from datetime import datetime
from typing import List

from pydantic import BaseModel

from app.serializers.product import CartProduct
from app.serializers.user import UserRead


class CartItemRead(BaseModel):
    id: int
    quantity: int
    product: CartProduct


class CartRead(BaseModel):
    id: int
    status: str
    created_at: datetime
    user: UserRead
    total: float
    cart_items: List[CartItemRead]


class AddToCartRequest(BaseModel):
    product_id: int
    quantity: int
