import logging.config
import settings

from flask import Flask, Blueprint
from database import db

from app.api_object import api
from app.version1.endpoints.people import ns as people_namespace


logging.config.fileConfig(settings.LOGGING_CONFIG_FILE)
log = logging.getLogger(__name__)


def init():

    app = Flask(__name__)

    # Configuration
    app.config['TRAP_BAD_REQUESTS'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = settings.DB_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS

    v1 = Blueprint('api/v1', __name__, url_prefix='/api/v1')
    api.init_app(v1)
    api.add_namespace(people_namespace)
    app.register_blueprint(v1)
    with app.app_context():
        db.init_app(app)

        @app.before_first_request
        def create_tables():
            db.create_all()

    return app


if __name__ == '__main__':
    init().run(debug=True)
