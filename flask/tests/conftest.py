import pytest
from app import create_app
from extensions import db


@pytest.fixture
def app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
            # Use in-memory database for tests
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        }
    )

    # Create tables for the in-memory database
    with app.app_context():
        db.create_all()

    yield app

    # Drop tables after the test
    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()
