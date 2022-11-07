from flask import jsonify, abort, make_response


def get_one_obj_or_abort(cls, obj_id):
    try:
        obj_id = int(obj_id)
    except ValueError:
        response_str = f"Invalid ID: `{obj_id}`. ID must be an integer"
        abort(make_response(jsonify({"message": response_str}), 400))

    matching_obj = cls.query.get(obj_id)

    if not matching_obj:
        response_str = f"{cls.__name__} with id `{obj_id}` was not found in the database."
        abort(make_response(jsonify({"message": response_str}), 404))

    return matching_obj


# FROM bike routes file
# replacement for helper above?
# WHY DO WE HAVE THIS HERE AND NOT IN BIKE CLASS MODEL FILE?
# @classmethod
# def get_one_obj_or_abort(cls, obj_id):
#     try:
#         obj_id = int(obj_id)
#     except ValueError:
#         response_str = f"Invalid bike_id: `{obj_id}`. ID must be a integer."
#         abort(make_response({"message": response_str}, 400))

#     matching_obj = Bike.query.get(obj_id)

#     # bike with matching id not found -> 404
#     if matching_obj is None:
#         response_str = f"{cls.__nam__} with id `{obj_id}` was not found in the database."
#         abort(make_response({"message": response_str}, 404))

#     # if matching bike found, return bike object
#     return matching_obj
