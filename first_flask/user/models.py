from first_flask import db


class Show(db.Model):
    # __tablename__ = 'covid'
    id=db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(50))
    age = db.Column(db.Integer)

    def __repr__(self):
        return {
            "id" : self.id,

            "name" : self.name,
            "age": self.age
        }