from sqlalchemy.orm import Session

from app.models.order import Order
from app.models.user import User


def selector_get_user_orders(db: Session, user: User):
    return db.query(Order).filter(Order.user_id == user.id).all()
