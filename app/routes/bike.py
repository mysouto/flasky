import re
from flask import Blueprint, jsonify


class Bike:
    def __init__(self, id, name, price, size, type):
        # id helps keep track of each bike to refer to unique item
        self.id = id
        self.name = name
        self.price = price
        self.size = size
        self.type = type


# hardcoding bikes data
# created 3 instances of bike class, like an invetory
bikes = [
    Bike(5, "Nina", 100, 48, "gravel"),
    Bike(8, "Bike 3000", 1000, 50, "hybrid"),
    Bike(2, "Auberon", 2000, 52, "electronic"),
]

# print(bikes)

# CREATING A BLUEPRINT
# 1. import bluenprint class
# 2. create instance of blueprint class
# - 3 arguments: str, __name__, url_prefix="/bike"
# -- url prefix, were to start blueprint
bike_bp = Blueprint("bike_bp", __name__, url_prefix="/bike")


# 4. create function to return JSON for client
# 5. add constructor
# "" that follows /bike, methods=[requests]
@bike_bp.route("", methods=["GET"])
def get_all_bikes():
    # convert python objects/class into JSON
    # 1. convert to dictionary (lst of dicts)
    response = []
    for bike in bikes:
        bike_dict = {
            "id": bike.id,
            "name": bike.name,
            "price": bike.price,
            "size": bike.size,
            "type": bike.type,
        }

        response.append(bike_dict)  # add bike dict to list

    # convert python list -> jsonify
    # return jsonify(["this", "is", "working!"]), 200  # 200: status code

    # RETURN LOGIC
    # logic: jsonify response with status 200
    return jsonify(response), 200

# 6. Make sure Flask knows app functions exits -> go to init file
