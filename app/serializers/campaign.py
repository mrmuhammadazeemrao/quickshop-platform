from typing import List
from pydantic import BaseModel

from app.serializers.category import SubCategorySerializer


class CampaignItemBase(BaseModel):
    id: int
    title: str
    image: str
    category: SubCategorySerializer


class CampaignBase(BaseModel):
    id: int
    title: str
    campaign_items: List[CampaignItemBase]


class CampaignWithItems(BaseModel):
    id: int
    title: str
    campaign_items: List[CampaignItemBase]
