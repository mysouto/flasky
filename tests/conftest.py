import pytest
from app import create_app
from app import db  # db variable is shared across files, instance of database
# signals, create new db after request
from flask.signals import request_finished


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
