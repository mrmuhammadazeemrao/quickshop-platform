from sqlalchemy.orm import Session

from app.models.product import Category
from app.serializers.category import CategoryCreate


def service_create_category(db: Session, category: CategoryCreate):
    db_category = Category(**category.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)

    return db_category
