from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.selectors.category import selector_get_categories_with_sub_categories
from app.serializers.category import CategorySerializer

router = APIRouter()


@router.get("/", response_model=List[CategorySerializer])
def read_categories(db: Session = Depends(get_db)):
    categories = selector_get_categories_with_sub_categories(db)
    return categories
