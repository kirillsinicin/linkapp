from hashlib import blake2b

from flask import current_app, request, url_for

from linka.helpers.auth_helper import get_user_token
from linka.model import Link, db


def get_hash_link(link: str) -> str:
    hash_link = blake2b(link.encode(), digest_size=5).hexdigest()
    return hash_link


def get_short_link() -> str:
    prefix = f"{current_app.config.get("PROTOCOL")}://{current_app.config.get("DOMAIN_NAME")}"
    suffix = url_for(
        "links.redirect_to_original_link", short_link=get_hash_link(request.form["destination"])
    )
    return f"{prefix}{suffix}"


def get_original_link(short_link: str) -> str:
    link_entry = Link.query.filter_by(short_link=short_link).first()
    return link_entry.original_link


def create_link() -> Link:
    link = Link(
        user_id=get_user_token(),
        name=request.form["name"],
        original_link=request.form["destination"],
        short_link=get_hash_link(request.form["destination"]),
    )
    db.session.add(link)
    db.session.commit()
    return link
