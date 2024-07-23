from dotenv import load_dotenv
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    load_dotenv()
    app.config.from_prefixed_env()

    from linka.model import db

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from linka.views import auth, links

    app.register_blueprint(links.bp)
    app.register_blueprint(auth.auth_bp)

    return app
