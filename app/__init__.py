from flask import Flask
# don't need to memorize, know how to write
# can refer back from previous projects
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


# APP FUNCTION registers blueprint
# function needs to be named exactly "create_app"
# when `run Flask` it will look for create_app function
def create_app():
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    # CONFIG FOR DATABASE
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # where database is on the internet
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:postgres@localhost:5432/bikes_developement"

    # CONNECT DATABASE TO APP
    # flask app/server
    db.init_app(app)
    # migrate help set up database
    migrate.init_app(app, db)

    # 6. final steps: Make sure Flask knows app functions exits -> go to init file (from bike file)
    # -- import bike blueprint from bike file
    from .routes.bike import bike_bp

    # 7. register/connect blueprint back to app
    # "this is the blueprint i wanna connect to my server"
    # We use app's pre-defined function register_blueprint to register bike_bp blueprint
    app.register_blueprint(bike_bp)

    # creates app instance and returns it
    return app
