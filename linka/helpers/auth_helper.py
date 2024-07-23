from flask import request

from linka.model import User


def get_user_token() -> str:
    auth_header_value = request.headers.get("Authorization")
    if auth_header_value is not None:
        user_token = auth_header_value.split()[1]
        return user_token


def is_user_exist(user_token: str) -> bool:
    user_entry = User.query.filter_by(id=user_token).first()
    if user_entry:
        return True
    return False
