import json
from attr import validate
from flask import abort, Blueprint, jsonify, make_response, request
from app import db
from app.models.bike import Bike

bike_bp = Blueprint("bike_bp", __name__, url_prefix="/bike")


def validate_bike(bike_id):
    try:
        bike_id = int(bike_id)
    except ValueError:
        response_str = f"Invalid bike_id: {bike_id}. ID must be a integer."
        abort(make_response({"message": response_str}, 400))

    matching_bike = Bike.query.get(bike_id)

    # bike with matching id not found -> 404
    if matching_bike is None:
        response_str = f"Could not find bike with ID {bike_id}"
        abort(make_response({"message": response_str}, 404))

    # if matching bike found, return bike object
    return matching_bike


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


# CREATE GET ROUTE FOR 1 BIKE
@bike_bp.route("/<bike_id>", methods=["GET"])
def get_one_bike(bike_id):
    chosen_bike = validate_bike(bike_id)
    # returns jsonified object and response code as tuple
    bike_dict = {
        "id": chosen_bike.id,
        "name": chosen_bike.name,
        "price": chosen_bike.price,
        "size": chosen_bike.size,
        "type": chosen_bike.type
    }

    return jsonify(bike_dict), 200
