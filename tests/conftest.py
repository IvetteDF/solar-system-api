from app.models.planet import Planet
import pytest
from app import create_app
from app import db

@pytest.fixture
def app():
    app = create_app({"TESTING":True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_planets(app):
    venus = Planet(name="venus", description="hottie w a body", moons=0)
    earth = Planet(name="earth", description="in her flop era", moons=1)

    db.session.add_all([venus, earth])
    db.session.commit()


