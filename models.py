from . import db
from flask_login import UserMixin


class Link(db.Model):
    uri = db.Column(db.String(150), primary_key=True)
    name = db.Column(db.String(100))
    created_by_login = db.Column(db.String(100))
    images = db.Column(db.String(100))  # TODO: change this one
    customer_name = db.Column(db.String(100))


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_by_login = db.Column(db.String(100))
    name = db.Column(db.String(100))
    image_link = db.Column(db.String(300))
    price = db.Column(db.Integer)
    description = db.Column(db.String(500))
    tags = db.relationship('Tag', backref='image')

    def __repr__(self):
        return f'<Image "{self.name}...">'


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(500))
    image_id = db.Column(db.Integer, db.ForeignKey('product.id'))

    def __repr__(self):
        return f'<Tag "{self.title}">'


class User(UserMixin, db.Model):
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(1000))
    password = db.Column(db.String(100))

    def to_dict(self):
        data = {
            'id': self.id,
            'login': self.login,
            'password': self.password
        }
        return data
