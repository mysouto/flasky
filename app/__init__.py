from flask import Flask
# don't need to memorize, know how to write
# can refer back from previous projects


# function needs to be named exactly "create_app"
# when `run Flask` it will look for create_app function
def create_app():
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    # creates app instance and returns it
    return app
