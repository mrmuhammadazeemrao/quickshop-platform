import pytest
import os

from app.core.database import Base, engine


@pytest.fixture(autouse=True)
def set_test_environment():
    os.environ["ENVIRONMENT"] = "test"


@pytest.fixture(scope="session")
def initialize_test_database():
    # Create tables in the test database
    Base.metadata.create_all(bind=engine)

    # Provide the test session as a yield value
    yield

    # Remove the tables and close the engine
    Base.metadata.drop_all(bind=engine)
    engine.dispose()
