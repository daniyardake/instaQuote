from flask import Blueprint, request
from .. import db

image = Blueprint('image', __name__)


@image.route('image/', methods=['POST'])
def create_image():
    return 'Index'


@image.route('image/update/<id>', methods=['DELETE', 'UPDATE'])
def update_image():
    return 'Profile'
