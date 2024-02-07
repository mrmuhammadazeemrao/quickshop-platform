from sqlalchemy.orm import Session
from faker import Faker
from app.models.order import Order, OrderItem, Review
from app.core.database import Base, get_db, engine
from app.models.product import Product

fake = Faker()


def create_dummy_orders(db: Session, num_orders: int = 5):
    for _ in range(num_orders):
        order = Order(
            status=fake.random_element(elements=["Pending", "Shipped", "Delivered"]),
            delivery_date=fake.date_time(),
            shipping_address=fake.address(),
            comment=fake.text(),
            user_id=fake.random_int(min=1, max=50),
        )
        db.add(order)
        db.commit()

        # Create dummy data for OrderItems
        products = list(db.query(Product).all())
        for _ in range(fake.random_int(min=1, max=5)):
            order_item = OrderItem(
                quantity=fake.random_int(min=1, max=10),
                order=order,
                product=products.pop(),
            )
            db.add(order_item)
            db.commit()

            # Create dummy data for Reviews
            if fake.boolean(chance_of_getting_true=50):
                review = Review(
                    rating=fake.random_int(min=1, max=5),
                    comment=fake.text(),
                    order_item=order_item,
                )
                db.add(review)
                db.commit()


if __name__ == "__main__":
    # Create tables
    Base.metadata.create_all(bind=engine)

    # Create a session using the get_db function
    with next(get_db()) as db:
        create_dummy_orders(db, num_orders=100)
