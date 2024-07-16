from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://kiruha:example@localhost:8877/kiruha"

    from linka.model import db

    db.init_app(app)

    from linka.views import links

    app.register_blueprint(links.bp)

    return app
