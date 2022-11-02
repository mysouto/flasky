import pytest
from app import create_app
from app import db  # db variable is shared across files, instance of database
# signals, create new db after request
from flask.signals import request_finished
from app.models.bike import Bike


@pytest.fixture
def app():
    app = create_app({"TESTING": True})  # creates app object

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()  # if request is finiished, removes db session

    with app.app_context():
        db.create_all()
        # yield when request is made
        yield app

    # cleans database after each unit test
    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def two_bikes(app):
    # initialize 2 objects and put them into database
    # random test data
    # pass all attributes, except for id
    bike1 = Bike(name="Speedy", price=10, size=30, type="hybrid")
    bike2 = Bike(name="Motor", price=200, size=60, type="motor")

    db.session.add(bike1)
    db.session.add(bike2)
    # commit session
    db.session.commit()
