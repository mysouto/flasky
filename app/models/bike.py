from app import db


# important, where magic happens
class Bike(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    size = db.Column(db.Integer)
    type = db.Column(db.String)
    # adding FK for parent Cyclist
    cyclist_id = db.Column(db.Integer, db.ForeignKey('cyclist.id'))
    # define database relation with back_populates
    cyclist = db.relationship("Cyclist", back_populates="bikes")

    def to_dict(self):
        bike_dict = {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "size": self.price,
            "type": self.type,
        }
        return bike_dict

    @classmethod
    # create Bike object from dict representation
    def from_dict(cls, data_dict):
        # check if all items are required
        if "name" in data_dict and "price" in data_dict and "size" in data_dict and "type" in data_dict:

            # creating new bike object
            new_obj = cls(
                name=data_dict["name"],
                price=data_dict["price"],
                size=data_dict["size"],
                type=data_dict["type"]
            )

        return new_obj
        # same as logic below in POST below
        # new_bike = Bike(
        #     name=request_body["name"],
        #     price=request_body["price"],
        #     size=request_body["size"],
        #     type=request_body["type"]
        # )
