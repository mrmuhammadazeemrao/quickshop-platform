from pydantic import BaseModel


class ProductList(BaseModel):
    id: str
    title: str
    description: str
    price: float
    image: str
    sub_category: dict


class CartProduct(BaseModel):
    id: int
    title: str
    description: str
    price: float
