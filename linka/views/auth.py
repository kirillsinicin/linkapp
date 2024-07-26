import uuid

from flask import Blueprint, abort, request
from flask.json import jsonify

from linka.model import User, db

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=["POST"])
def register():
    if request.form["login"] and request.form["password"]:
        user = User(id=uuid.uuid4(), login=request.form["login"], password=request.form["password"])
        db.session.add(user)
        db.session.commit()
        return jsonify(user.id)
    abort(401)
