from flask import Blueprint, redirect, request

from linka.hash_link import get_original_link, get_short_link
from linka.model import Link, db

bp = Blueprint("links", __name__, url_prefix="/links")


@bp.route("/")
def index():
    return "Hello links"


@bp.route("/create", methods=["POST"])
def links_create():
    link = Link(
        name=request.form["name"],
        original_link=request.form["destination"],
        short_link=get_short_link(request.form["destination"]),
    )
    db.session.add(link)
    db.session.commit()


@bp.route("/<short_link>", methods=["GET"])
def redirect_to_original_link(short_link):
    return redirect(get_original_link(short_link))
