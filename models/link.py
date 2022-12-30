from . import db


class Link(db.Model):
    uri = db.Column(db.String(150), primary_key=True)
    name = db.Column(db.String(100))
    created_by_login = db.Column(db.String(100))
    images = db.Column(db.String(100))  # TODO: change this one
    customer_name = db.Column(db.String(100))
