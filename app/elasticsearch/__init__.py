from app.models.product import Product
from app.models.order import OrderItem
from app.models.cart import CartItem

import os
from elasticsearch_dsl.connections import connections
from dotenv import load_dotenv

load_dotenv()
ELASTICSEARCH_HOST = os.getenv("ELASTICSEARCH_HOST")
ELASTICSEARCH_PORT = os.getenv("ELASTICSEARCH_PORT")

connections.create_connection(alias='default', hosts=[f'http://{ELASTICSEARCH_HOST}:{ELASTICSEARCH_PORT}'])
