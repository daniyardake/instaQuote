from flask import Blueprint, request
from . import db

image = Blueprint('image', __name__)


@image.route('/image/', methods=['POST'])
def create_link():
    return 'Index'


@image.route('/image/update/<id>', methods=['DELETE', 'UPDATE'])
def update_link():
    return 'Profile'
