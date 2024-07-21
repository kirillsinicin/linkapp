from hashlib import blake2b

from flask import current_app

from linka.model import Link


def get_hash_link(link: str) -> str:
    hash_link = blake2b(link.encode(), digest_size=5).hexdigest()
    return hash_link


def get_short_link(prefix: str, suffix: str) -> str:
    return f"{prefix}{suffix}"


def get_original_link(short_link: str) -> str:
    link_entry = Link.query.filter_by(short_link=short_link).first()
    return link_entry.original_link
