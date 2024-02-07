import os
from elasticsearch_dsl.connections import connections
from dotenv import load_dotenv

load_dotenv()
ELASTICSEARCH_HOST = os.getenv("ELASTICSEARCH_HOST")
ELASTICSEARCH_PORT = os.getenv("ELASTICSEARCH_PORT")

connections.create_connection(alias='default', hosts=[f'http://{ELASTICSEARCH_HOST}:{ELASTICSEARCH_PORT}'])
