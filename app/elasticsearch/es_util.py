import os
from elasticsearch import Elasticsearch


def create_es_client():
    return Elasticsearch([{'host': os.getenv("ELASTICSEARCH_HOST", "localhost"),
                           'port': os.getenv("ELASTICSEARCH_PORT", 9200),
                           'scheme': "http"}])
