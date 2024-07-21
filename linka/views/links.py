from flask import Blueprint, current_app, redirect, request, url_for
from flask.json import jsonify

from linka.hash_link import get_hash_link, get_original_link, get_short_link
from linka.model import Link, db

bp = Blueprint("links", __name__, url_prefix="/links")


@bp.route("/")
def index():
    return "Hello links"


@bp.route("/create", methods=["POST"])
def links_create():
    hash_link = get_hash_link(request.form["destination"])
    prefix = f"{current_app.config.get("PROTOCOL")}://{current_app.config.get("DOMAIN_NAME")}"
    suffix = url_for("links.redirect_to_original_link", short_link=hash_link)

    link = Link(name=request.form["name"], original_link=request.form["destination"], short_link=hash_link)
    db.session.add(link)
    db.session.commit()
    return jsonify(link.id, link.name, get_short_link(prefix, suffix))


@bp.route("/<short_link>", methods=["GET"])
def redirect_to_original_link(short_link):
    return redirect(get_original_link(short_link))
