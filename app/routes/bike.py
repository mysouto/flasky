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
        type=request_body["type"],
        size=request_body["size"],
    )

    # add to dict
    db.session.add(new_bike)

    # IMPORTANT - make sure to make a commit
    db.session.commit()

    # id is automatically populated after add and commit steps
    return {"id": new_bike.id}, 201


# CREATE GET ROUTE
# to query bikes in database
@bike_bp.route("", methods=["GET"])
def get_all_bikes():
    # only thing changed: add .query.all below
    bikes = Bike.query.all()

    response = []
    for bike in bikes:
        bike_dict = {
            "id": bike.id,
            "name": bike.name,
            "price": bike.price,
            "size": bike.size,
            "type": bike.type,
        }

        response.append(bike_dict)
    return jsonify(response), 200
