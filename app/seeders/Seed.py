import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from app.core.database import get_db
from app.seeders.cart import create_dummy_carts
from app.seeders.order import create_dummy_orders
from app.seeders.product import create_dummy_products
from app.seeders.user import create_dummy_users

FLAG_FILE_PATH = "seed_done"

if __name__ == '__main__':
    if not os.path.exists(FLAG_FILE_PATH):
        with next(get_db()) as db:
            create_dummy_users(db, num_users=50)
            create_dummy_products(db)
            create_dummy_orders(db, num_orders=100)
            create_dummy_carts(db, num_carts=20, max_cart_items=5)

    with open(FLAG_FILE_PATH, "w"):
        pass
