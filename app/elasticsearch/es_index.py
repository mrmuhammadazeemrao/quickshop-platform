import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from app.core.database import get_db
from app.elasticsearch.es_mapper import product_to_document
from app.models.product import Product


def index_products():
    db = next(get_db())
    for product in db.query(Product).all():
        product_document = product_to_document(product)
        product_document.save()


if __name__ == '__main__':
    index_products()
