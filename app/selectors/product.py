from sqlalchemy.orm import Session

from app.models.product import Product


def selector_get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()
