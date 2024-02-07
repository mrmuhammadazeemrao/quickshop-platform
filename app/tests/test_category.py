from fastapi.testclient import TestClient

from app.core.database import get_db
from app.serializers.category import CategoryCreate
from app.services.category import service_create_category
from main import app

client = TestClient(app)

test_db = next(get_db())


def test_read_categories(initialize_test_database):
    parent = service_create_category(test_db,
                                     category=CategoryCreate(**{"title": "Test Parent Category"}))
    service_create_category(test_db,
                            category=CategoryCreate(**{"title": "Test Child Category", "parent_id": parent.id}))

    response = client.get("/categories")

    categories = response.json()

    assert response.status_code == 200
    assert isinstance(categories, list)
    assert len(categories) > 0
    assert "id" in categories[0]
    assert "title" in categories[0]
    assert "sub_categories" in categories[0]
