from pydantic import BaseModel, PositiveFloat, conint


class ReviewCreate(BaseModel):
    rating: PositiveFloat
    comment: str = None
    order_item_id: conint(ge=1)
