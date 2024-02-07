from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

from app.serializers.product import CartProduct


class OrderItemBase(BaseModel):
    id: int
    product: CartProduct
    quantity: int


class OrderItemCreate(OrderItemBase):
    product_id: int


class OrderCreate(BaseModel):
    delivery_date: datetime
    shipping_address: str
    comment: str
    order_items: List[OrderItemCreate]


class OrderRead(BaseModel):
    id: int
    status: str
    delivery_date: Optional[datetime]
    shipping_address: str
    comment: Optional[str]
    user_id: int
    order_items: List[OrderItemBase]


class PlaceOrderRequest(BaseModel):
    shipping_address: str
