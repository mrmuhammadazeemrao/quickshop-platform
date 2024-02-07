from typing import List, Optional
from pydantic import BaseModel


class SubCategorySerializer(BaseModel):
    id: int
    title: str


class CategorySerializer(BaseModel):
    id: int
    title: str
    sub_categories: List[SubCategorySerializer]


class CategoryCreate(BaseModel):
    title: str
    parent_id: Optional[int] = None
