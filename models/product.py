from ..extensions import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
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
