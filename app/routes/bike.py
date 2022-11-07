import json
from attr import validate
from flask import abort, Blueprint, jsonify, make_response, request
from app import db
from app.models.bike import Bike
from .routes_helper import get_one_obj_or_abort

bike_bp = Blueprint("bike_bp", __name__, url_prefix="/bike")


# CREATE POST ROUTE
# decorator
@bike_bp.route("", methods=["POST"])
def add_bike():
    request_body = request.get_json()

    # convert FROM json obj TO Bike class
    # new_bike = Bike(
    #     name=request_body["name"],
    #     price=request_body["price"],
    #     size=request_body["size"],
    #     type=request_body["type"]
    # )

    # convert Bike objct to bike dict
    new_bike = Bike.from_dict(request_body)

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
    # ADDING QUERY PARAMETER -> FUNCTIONALITY
    # functionality: only get some bikes -> Add Query Parameter
    name_param = request.args.get("name")  # arg for .get: name of query param

    # add logic to check if param is required? or specified
    if name_param is None:
        # queries and gets a list of all instances of bike
        bikes = Bike.query.all()
    else:
        # filder_by filters by a condition specified in arg
        # need to specify column by using "name="
        bikes = Bike.query.filter_by(name=name_param)

    # logic to convert python bike object to dict and json
    # response = []
    # iterate over bikes object
    # for bike in bikes:
    #     bike_dict = bike.to_dict() # replaces bike_dict below
        # bike_dict = {
        #     "id": bike.id,
        #     "name": bike.name,
        #     "price": bike.price,
        #     "size": bike.size,
        #     "type": bike.type
        # }
        # response.append(bike_dict)

    # list comprehension syntax
    response = [bike.to_dict() for bike in bikes]

    return jsonify(response), 200


# Create GET route for 1 bike
@bike_bp.route("/<bike_id>", methods=["GET"])
def get_one_bike(bike_id):
    chosen_bike = get_one_obj_or_abort(Bike, bike_id)

    # returns jsonified object and response code as tuple
    bike_dict = {
        "id": chosen_bike.id,
        "name": chosen_bike.name,
        "price": chosen_bike.price,
        "size": chosen_bike.size,
        "type": chosen_bike.type
    }

    return jsonify(bike_dict), 200


# Create PUT route to add a object
@bike_bp.route("/<bike_id>", methods=["PUT"])
def update_bike_with_new_vals(bike_id):
    # validate with helper to pass reqs
    # bike = validate_bike(bike_id)
    # get_one_obj_or_abort(class, object_id)
    bike = get_one_obj_or_abort(Bike, bike_id)

    request_body = request.get_json()

    # all attributes required -> using PUT to replace entire entity
    # if any attribute missing, return message
    if "name" not in request_body or \
        "size" not in request_body or \
        "price" not in request_body or \
            "type" not in request_body:
        return jsonify({"message": "Request must include name, size, price, and type"})

    # specify and set new values
    bike.name = request_body["name"]
    bike.size = request_body["size"]
    bike.price = request_body["price"]
    bike.type = request_body["type"]

    # commit change
    db.session.commit()

    # return make_response(f"Bike {bike_id} successfully updated.")
    return jsonify(f"Bike {bike_id} successfully updated."), 200


# Create DELETE route
# using id
@bike_bp.route("/<bike_id>", methods=["DELETE"])
def delete_one_bike(bike_id):
    # bike = validate_bike(bike_id)
    bike = get_one_obj_or_abort(Bike, bike_id)

    # command to delete object from database
    # param: bike
    db.session.delete(bike)

    db.session.commit()

    return jsonify(f"Bike #{bike_id} successfully deleted."), 200
