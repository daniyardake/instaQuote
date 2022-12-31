from flask import Blueprint, request, abort, jsonify, session
from flask_login import login_user
from .models import User, db
from .stringParser import StringParser

from . import language

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():
    if (not request.json) or (not request.json.get('login')) or (not request.json.get('password')):
        abort(400)
    login = request.json.get('login')
    password = request.json.get('password')

    user = User.query.filter_by(login=login).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or user.password != password:
        return jsonify({StringParser.get('error'): StringParser.get('wrong_login')})


@auth.route('/user/signup', methods=['POST'])
def signup():
    if (not request.json) or (not request.json.get('login')) or (not request.json.get('password')):
        abort(400)
    exists = db.session.query(User.id).filter_by(
        login=request.json.get('login')).first() is not None
    if (exists):
        return jsonify({
            StringParser.get('error'): StringParser.get('user_exists')
        })
    user = User(login=request.json.get('login'),
                password=request.json.get('password'))
    db.session.add(user)
    db.session.commit()
    login_user(user, remember=True)
    return jsonify({'sucess': '100'})


@auth.route('/user/list')
def list():
    return jsonify([u.to_dict() for u in User.query.all()])
