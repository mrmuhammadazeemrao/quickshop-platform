from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload

from app.models.cart import Cart, CartItem
from app.models.user import User
from app.serializers.cart import AddToCartRequest


def service_get_or_create_user_cart(db: Session, current_user: User):
    user_cart = (
        db.query(Cart)
        .filter_by(user_id=current_user.id, status="active")
        .options(
            joinedload(Cart.user),
            joinedload(Cart.cart_items).joinedload(CartItem.product)
        )
        .first()
    )
    if not user_cart:
        user_cart = Cart(user_id=current_user.id, status="active")
        db.add(user_cart)
        db.commit()
        db.refresh(user_cart)

    return user_cart


def service_add_to_cart(db: Session, user_cart: Cart, request_data: AddToCartRequest):
    # Check if the product is already in the user's cart, update quantity if it is
    cart_item = db.query(CartItem).filter(CartItem.cart_id == user_cart.id,
                                          CartItem.product_id == request_data.product_id).first()
    if cart_item:
        cart_item.quantity += request_data.quantity
    else:
        cart_item = CartItem(cart_id=user_cart.id, product_id=request_data.product_id, quantity=request_data.quantity)
        db.add(cart_item)

    db.commit()
    db.refresh(cart_item)

    return user_cart


def service_remove_from_cart(db: Session, user_cart: Cart, product_id: int):
    cart_item = (
        db.query(CartItem)
        .filter_by(cart_id=user_cart.id, product_id=product_id)
        .first()
    )

    if not cart_item:
        raise HTTPException(status_code=404, detail="Product not found in cart")

    db.delete(cart_item)
    db.commit()

    db.refresh(user_cart)

    return user_cart
