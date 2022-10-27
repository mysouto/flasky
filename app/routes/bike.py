import json
from flask import abort, Blueprint, jsonify, request
from app import db
from app.models.bike import Bike

bike_bp = Blueprint("bike_bp", __name__, url_prefix="/bike")


# CREATE POST ROUTE
# decorator
@bike_bp.route("", methods=["POST"])
def add_bike():
    request_body = request.get_json()

    # convert to bike dict
    new_bike = Bike(
        name=request_body["name"],
        price=request_body["price"],
        size=request_body["size"],
        type=request_body["type"]
    )

    # add to dict
    db.session.add(new_bike)

    # IMPORTANT - make sure to make a commit
    # saving new record to table
    db.session.commit()

    # id is automatically populated after add and commit steps
    return {"id": new_bike.id}, 201


# CREATE GET ROUTE
# to query bikes in database
@bike_bp.route("", methods=["GET"])
def get_all_bikes():
    # only thing changed: add .query.all below
    # queries and gets a list of all instances of bike
    bikes = Bike.query.all()

    # logic to convert python bike object to dict and json
    response = []
    for bike in bikes:
        bike_dict = {
            "id": bike.id,
            "name": bike.name,
            "price": bike.price,
            "size": bike.size,
            "type": bike.type
        }

        response.append(bike_dict)

    return jsonify(response), 200
