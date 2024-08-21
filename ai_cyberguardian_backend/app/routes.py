from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from .models import User
from . import db, ai

bp = Blueprint('routes', __name__)

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if User.query.filter_by(username=data['username']).first() or User.query.filter_by(email=data['email']).first():
        return jsonify({"msg": "User already exists"}), 400

    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully"}), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()

    if user is None or not user.check_password(data['password']):
        return jsonify({"msg": "Invalid credentials"}), 401

    access_token = create_access_token(identity=user.username)
    return jsonify(access_token=access_token), 200

@bp.route('/ai-analysis', methods=['POST'])
@jwt_required()
def ai_analysis():
    user = get_jwt_identity()
    data = request.get_json()
    result = ai.perform_analysis(data['input'])
    return jsonify({"user": user, "result": result})

