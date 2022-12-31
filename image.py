from flask import Blueprint, request
from flask_login import login_required, current_user
from . import db

image = Blueprint('image', __name__)


@image.route('/image/', methods=['POST'])
@login_required
def create_image():
    return 'Create Image'


@image.route('/image/update/<id>', methods=['DELETE', 'UPDATE'])
@login_required
def update_image():
    return 'Update Image'
