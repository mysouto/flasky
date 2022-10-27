# import json
# from flask import abort, Blueprint, jsonify, make_response


# class Bike:
#     def __init__(self, id, name, price, size, type):
#         # id helps keep track of each bike to refer to unique item
#         self.id = id
#         self.name = name
#         self.price = price
#         self.size = size
#         self.type = type


# # hardcoding bikes data
# # created 3 instances of bike class, like an invetory
# bikes = [
#     Bike(5, "Nina", 100, 48, "gravel"),
#     Bike(8, "Bike 3000", 1000, 50, "hybrid"),
#     Bike(2, "Auberon", 2000, 52, "electronic"),
# ]


# # CREATING A BLUEPRINT
# # 1. import blueprint class
# # 2. create instance of blueprint class
# # - 3 arguments: str, __name__, url_prefix="/bike"
# # -- url prefix, were to start blueprint
# bike_bp = Blueprint("bike_bp", __name__, url_prefix="/bike")


# # 4. create route function to return JSON for client
# # 5. add decorator with arguments (args define what type of request will be routed to this function)
# # "" that follows /bike, methods=[requests]
# @bike_bp.route("", methods=["GET"])
# # function will execute whenever a request that matches the decorator is received
# def get_all_bikes():
#     # convert python objects/class into JSON
#     # 1. convert instances of bike class to dictionaries
#     # return lst of dicts
#     response = []
#     for bike in bikes:
#         bike_dict = {
#             "id": bike.id,
#             "name": bike.name,
#             "price": bike.price,
#             "size": bike.size,
#             "type": bike.type,
#         }

#         response.append(bike_dict)  # add bike dict to list

#     # 2. convert python list -> jsonify
#     # 3. RETURN LOGIC
#     # logic: jsonify response with status 200
#     # For each endpoint, we must return the HTTP response
#     return jsonify(response), 200

# # 6. Make sure Flask knows app functions exits -> go to init file


# # CREATING A NEW ROUTE
# # 1. make a route to fetch a single object (bike)
# # 2. handle invalid request 400 code
# # 3. handle object not found 404
# @bike_bp.route("/<bike_id>", methods=["GET"])
# def get_one_bike(bike_id):
#     # "/<bike_id>" and bike_id param have to be named the exame same thing
#     # 1. valide bike id input
#     # see if bike_id can be converted to an int
#     # try-except: try to convert to int, if error: catch and raise 400 error
#     try:
#         bike_id = int(bike_id)
#     except ValueError:
#         response_str = f"Invalid bike_id: {bike_id}. ID must be a integer."
#         return jsonify({"message": response_str}), 400

#     # validate with helper validation function
#     bike_id = validate_id(bike_id)

#     # after try-except: bike_id will be a valid int
#     # 2. iterate thru data to find item with matching id
#     for bike in bikes:
#         if bike.id == bike_id:
#             # if id matched, create dict
#             bike_dict = {
#                 "id": bike.id,
#                 "name": bike.name,
#                 "price": bike.price,
#                 "size": bike.size,
#                 "type": bike.type,
#             }
#             # 3. if id in data, return bike's data with 200 response 200
#             return jsonify(bike_dict), 200

#     # 4. after loop: bike with matching id not found -> raise "404 object not found" error
#     response_message = f"Could not find bike with ID {bike_id}"
#     return jsonify({"message": response_message}), 404


# # REVIEW SESSION
# # ADD VALIDATION LOGIC to 1 helper function
# def validate_id(id):
#     try:
#         int_id = int(id)
#     except ValueError:
#         # bubble up exception
#         response_str = f"Invalid id: {id}. ID must be an integer."
#         abort(make_response(jsonify({"message": response_str}), 400))

#     return int_id
