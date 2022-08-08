from flask import Blueprint, request, jsonify
from ..database.db import db
from ..models.tables import User

auth_routes = Blueprint("auth", __name__)

@auth_routes.get("/login")
def login():
    return "This could be a login page."

@auth_routes.route('/users', methods=['GET'])
def user():
    if request.method == "GET":
        all_user = User.query.all()
        return jsonify(all_user)
    else:
        user = User(
            username=request.json["username"],
            password=request.json["password"],
            location=request.json["location"],
            email=request.json["email"]
        )
        db.session.add(user)
        db.session.commit()
        return 'user added'
