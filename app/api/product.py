from typing import List, Optional

from elasticsearch_dsl import Search, Q
from fastapi import APIRouter, HTTPException

from app.serializers.product import ProductList

router = APIRouter()


@router.get("/{product_id}", response_model=ProductList)
async def get_product_by_id(product_id: str):
    s = Search(using="default").index("products_index").query(Q("ids", values=[product_id]))

    response = s.execute()

    if not response.hits:
        raise HTTPException(status_code=404, detail="Product not found")

    product = response.hits[0]
    return {"id": product.meta.id, **product.to_dict()}


@router.get("/", response_model=List[ProductList])
async def get_products(query: Optional[str] = "", category: Optional[str] = ""):
    s = Search(using="default").index("products_index")
    if query:
        s = s.query(Q("multi_match", query=query, fields=["title", "description"]))
    if category:
        s = s.query(Q("multi_match", query=category, fields=["sub_category.title"]))

    response = s.execute()

    products = [{"id": hit.meta.id, **hit.to_dict()} for hit in response.hits]
    return products
