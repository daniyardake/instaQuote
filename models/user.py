from . import db


class User(db.Model):
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(1000))
    password = db.Column(db.String(100))
