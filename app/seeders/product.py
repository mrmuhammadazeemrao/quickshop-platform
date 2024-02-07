import random

from sqlalchemy.orm import Session
from faker import Faker
from app.models.product import Product, Category, Campaign, CampaignItem
from app.core.database import Base, get_db

fake = Faker()


def create_dummy_products(db: Session):
    # Create dummy data for Category
    parents = []
    for _ in range(10):
        category = Category(title=fake.word())
        db.add(category)
        parents.append(category)
    db.commit()

    for _ in range(20):
        category = Category(title=fake.word(), parent=random.choice(parents))
        db.add(category)
    db.commit()

    # Create dummy data for Products
    categories = db.query(Category).all()

    for _ in range(30):
        product = Product(
            title=fake.word(),
            price=fake.random_int(min=10, max=100),
            image=fake.image_url(),
            description=fake.text(),
            category_id=fake.random_element(elements=[c.id for c in categories]),
        )
        db.add(product)
    db.commit()

    # Create dummy data for Campaigns and CampaignItems
    for _ in range(3):
        campaign = Campaign(title=fake.word())
        db.add(campaign)
        db.commit()

        for _ in range(5):
            campaign_item = CampaignItem(
                title=fake.word(),
                image=fake.image_url(),
                category_id=fake.random_element(elements=[c.id for c in categories]),
                campaign_id=campaign.id,
            )
            db.add(campaign_item)
        db.commit()


if __name__ == "__main__":
    # Create tables
    Base.metadata.create_all(bind=next(get_db()).bind)

    # Create a session using the get_db function
    with next(get_db()) as db:
        create_dummy_products(db)
