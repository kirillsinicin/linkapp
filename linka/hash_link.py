from hashlib import blake2b

from linka.model import Link


def get_hash_link(link: str) -> str:
    hash_link = blake2b(link.encode(), digest_size=5).hexdigest()
    return hash_link


def get_short_link(link: str) -> str:
    # return 'kiruha.ly/' + get_hash_link(link)
    return get_hash_link(link)


def get_original_link(short_link: str) -> str:
    link_entry = Link.query.filter_by(short_link=short_link).first()
    return link_entry.original_link


# link1 = 'https://flask.palletsprojects.com/'
# link2 = 'https://flask.palletsprojects.com/en/3.0.x/tutorial/database/'
#
# print(get_short_link(link1))
# print(get_short_link(link2))
