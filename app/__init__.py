from flask import Flask
# don't need to memorize, know how to write
# can refer back from previous projects


# function needs to be named exactly "create_app"
# when `run Flask` it will look for create_app function
def create_app():
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    # 6. final steps: Make sure Flask knows app functions exits -> go to init file (from bike file)
    # -- import bike_bp from bike file
    from .routes.bike import bike_bp

    # 7. register/connect blueprint back to app
    # "this is the blueprint i wanna connect to my server"
    # We use app's pre-defined function register_blueprint to register bike_bp blueprint
    app.register_blueprint(bike_bp)

    # creates app instance and returns it
    return app
