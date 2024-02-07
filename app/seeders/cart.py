from sqlalchemy.orm import Session
from faker import Faker
from app.models.cart import Cart, CartItem
from app.models.user import User
from app.models.product import Product
from app.core.database import Base, get_db, engine

fake = Faker()


def create_dummy_carts(db: Session, num_carts: int = 10, max_cart_items: int = 5):
    users = db.query(User).all()
    products = db.query(Product).all()

    for _ in range(num_carts):
        user = fake.random_element(elements=users)
        cart = Cart(status=fake.random_element(elements=["active", "inactive"]), user=user)
        db.add(cart)
        try:
            db.commit()
        except Exception as e:
            print(e)

        for _ in range(fake.random_int(min=1, max=max_cart_items)):
            product = fake.random_element(elements=products)
            cart_item = CartItem(
                quantity=fake.random_int(min=1, max=10),
                cart=cart,
                product=product,
            )
            db.add(cart_item)
        try:
            db.commit()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    # Create tables
    Base.metadata.create_all(bind=engine)

    # Create a session using the get_db function
    with next(get_db()) as db:
        create_dummy_carts(db, num_carts=20, max_cart_items=5)
