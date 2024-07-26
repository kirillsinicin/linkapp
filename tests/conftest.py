import pytest
from sqlalchemy import text

from linka import create_app
from linka.model import Link, User, db


@pytest.fixture()
def app(monkeypatch):
    monkeypatch.setenv(
        "FLASK_SQLALCHEMY_DATABASE_URI", "mysql+pymysql://kiruha:example@localhost:8900/testuha"
    )
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    with app.app_context():
        db.create_all()
        user = User(id="qwertyuiop2", login="qwertyuiop2", password="qwertyuiop")
        link = Link(
            user=user,
            name="yandex",
            original_link="https://ya.ru/",
            short_link="c4d5e705b99",
        )
        db.session.add_all([user, link])
        db.session.commit()

    yield app

    with app.app_context():
        sql1 = text("DELETE FROM user;")
        sql2 = text("DELETE FROM link;")
        db.session.execute(sql2)
        db.session.execute(sql1)
        db.session.commit()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


@pytest.fixture()
def user(app):
    with app.app_context():
        with db.session.begin():
            user = User(id="asdf", login="asdf", password="qwertyuiop")
            db.session.add(user)
        yield user


@pytest.fixture()
def link(app):
    with app.app_context():
        with db.session.begin():
            test_user = User(id="1111", login="2222", password="3333")
            link = Link(
                user=test_user,
                name="zxc",
                original_link="https://ya.ru/",
                short_link="c4d5e705b9",
            )
            db.session.add(link)
        yield link
