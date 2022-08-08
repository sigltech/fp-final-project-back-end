from flask import Blueprint, request, jsonify
from ..database.db import db
from ..models.tables import Clothing, User, Offers, Messages

main_routes = Blueprint("main", __name__)


# @main_routes.route("/")
# def index():
#     return jsonify({"message": "Hello World!"}) 

@main_routes.route("/", methods=["GET"])
def index():
    if request.method == "GET":
        all_clothing = Clothing.query.all()
        return jsonify(all_clothing)
    else: 
        pass

# @main_routes.route("/clothing")
# def clothing():
#     if request.method == "GET":
#         all_clothing = Clothing.query.all()
#         return jsonify(all_clothing)
#     else:
#         return jsonify({"message": "Method not allowed"})

    # elif request.method == "POST":
    #     clothing = Clothing(
    #         name=request.json["name"],
    #         description=request.json["description"],
    #         price=request.json["price"],
    #         image=request.json["image"],
    #         user_id=request.json["user_id"]
    #     )
    #     db.session.add(clothing)
    #     db.session.commit()
    #     return jsonify(clothing)

@main_routes.route("/user", methods=["GET","POST"])
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
        return jsonify(user)

        
