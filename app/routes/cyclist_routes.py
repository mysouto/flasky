from attr import validate
from flask import abort, Blueprint, jsonify, make_response, request
from app import db
from app.models.cyclist import Cyclist
from .routes_helper import get_one_obj_or_abort
# IMPORT BIKE
from app.models.bike import Bike

cyclist_bp = Blueprint("cyclist_bp", __name__, url_prefix="/cyclist")


@cyclist_bp.route("", methods=["POST"])
def add_cyclist():
    request_body = request.get_json()
    new_cyclist = Cyclist.from_dict(request_body)

    db.session.add(new_cyclist)
    db.session.commit()

    return {"id": new_cyclist.id}, 201


@cyclist_bp.route("", methods=["GET"])
def get_all_cyclists():
    cyclists = Cyclist.query.all()

    response = [cyclist.to_dict() for cyclist in cyclists]

    return jsonify(response)


# GET all bikes that a cyclist has
# http://127.0.0.1:5000/cyclist/cyclist_id/bikes
@cyclist_bp.route("/<cyclist_id>/bike", methods=["GET"])
def get_all_bikes_belonging_to_a_cyclist(cyclist_id):
    cyclist = get_one_obj_or_abort(Cyclist, cyclist_id)

    # cyclist.bikes gives us a list of a all bikes belonging to a cyclist wtih specified id
    bikes_response = [bike.to_dict() for bike in cyclist.bikes]

    return jsonify(bikes_response), 200


# Post 1 bike to a cyclist
@cyclist_bp.route("/<cyclist_id>/bike", methods=["POST"])
def post_bike_belonging_to_a_cyclist(cyclist_id):
    parent_cyclist = get_one_obj_or_abort(Cyclist, cyclist_id)

    # creat bike from request
    request_body = request.get_json()
    new_bike = Bike.from_dict(request_body)
    # IMPORT BIKE at top of this file
    # from app.models.bike import Bike

    # set child relational attributes to parent attribute
    # setting cyclist attribute to new parent
    # Flask populates cyclist id to database
    new_bike.cyclist = parent_cyclist

    # add and commit
    db.session.add(new_bike)
    db.session.commit()

    return jsonify({"message": f"Bike {new_bike.name} belonging to {new_bike.cyclist.name} successfully added"})
    # new_bike.cyclist.name accesses cyclist name attribute
