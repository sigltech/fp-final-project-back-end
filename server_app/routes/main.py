from flask import Blueprint, request, jsonify
from ..database.db import db
from ..models.tables import Clothing

main_routes = Blueprint("main", __name__)

@main_routes.route("/", methods=["GET"])
def index():
    if request.method == "GET":
        all_clothing = Clothing.query.all()
        return jsonify(all_clothing)
    else: 
        pass

@main_routes.route("/clothing", methods=["GET", "POST", "PUT", "DELETE"])
def clothing():
    if request.method == "GET":
        all_clothing = Clothing.query.all()
        return jsonify(all_clothing)
    elif request.method == "POST":
        clothing = Clothing(
            name=request.json["name"],
            description=request.json["description"],
            price=request.json["price"], 
            image=request.json["image"],
            user_id=request.json["user_id"]
        )
        db.session.add(clothing)
        db.session.commit()
        return jsonify(clothing)


