from sqlalchemy.orm import Session

from app.models.order import Order, OrderItem
from app.models.user import User
from app.services.cart import service_get_or_create_user_cart


def service_place_order(db: Session, user: User, shipping_address: str):
    user_cart = service_get_or_create_user_cart(db, user)

    new_order = Order(
        status="pending",
        user_id=user.id,
        shipping_address=shipping_address
    )
    db.add(new_order)
    db.commit()

    for cart_item in user_cart.cart_items:
        order_item = OrderItem(
            quantity=cart_item.quantity,
            order_id=new_order.id,
            product_id=cart_item.product_id
        )
        db.add(order_item)

    user_cart.cart_items = []
    db.commit()

    return new_order
