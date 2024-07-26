from flask import Blueprint, abort, redirect, url_for

from flask.json import jsonify

from linka.helpers.auth_helper import get_user_token, is_user_exist
from linka.helpers.links_helper import create_link, get_original_link, get_short_link

bp = Blueprint("links", __name__, url_prefix="/links")


@bp.route("/")
def index():
    return "Hello links"


@bp.route("/create", methods=["POST"])
def links_create():
    if is_user_exist(get_user_token()):
        link = create_link()
        return jsonify(link.id, link.name, get_short_link())
    return abort(401)


@bp.route("/<short_link>", methods=["GET"])
def redirect_to_original_link(short_link):
    return redirect(get_original_link(short_link))
