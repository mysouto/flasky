from app import db


class Cyclist(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)

    def to_dict(self):
        cyclist_dict = {
            "id": self.id,
            "name": self.name,
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
