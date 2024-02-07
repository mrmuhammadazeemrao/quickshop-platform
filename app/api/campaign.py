from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.orm import selectinload
from typing import List

from app.core.database import get_db
from app.models.product import Campaign
from app.serializers.campaign import CampaignWithItems

router = APIRouter()


@router.get("/", response_model=List[CampaignWithItems])
def read_campaigns(db: Session = Depends(get_db)):
    campaigns = db.query(Campaign).options(selectinload(Campaign.campaign_items)).all()
    return campaigns
