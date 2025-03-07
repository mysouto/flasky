from app import db


class Cyclist(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    # add relation to bikes
    bikes = db.relationship("Bike", back_populates="cyclist")
    # "cyclist" is the attribute defined in Bike model
    # cyclist = db.relationship("Cyclist", back_populates="bikes")

    def to_dict(self):
        bikes_list = [bike.to_dict() for bike in self.bikes]

        cyclist_dict = {
            "id": self.id,
            "name": self.name,
            # add new key:value
            "bikes": bikes_list,
        }

        return cyclist_dict

    @classmethod
    def from_dict(cls, data_dict):
        # check if data_dict has all valid req attributes
        if "name" in data_dict:
            # creating new cyclist object
            new_obj = cls(
                name=data_dict["name"],
            )

        return new_obj
