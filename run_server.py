import os
import logging
import logging.config
import settings

from flask import Flask, Blueprint
from database import db

from app.version1.api_object import api
#from app.version1.endpoints import ns as people_namespace
from app.version1.testendpoint import ns as test_ns

logging.config.fileConfig(settings.LOGGING_CONFIG_FILE)
log = logging.getLogger(__name__)

def init():

    app = Flask(__name__)
    app.config['TRAP_BAD_REQUESTS'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = settings.DB_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS

    v1 = Blueprint('api/v1', __name__, url_prefix='/api/v1')
    api.init_app(v1)
    api.add_namespace(test_ns)
    #api.add_namespace(people_namespace)
    app.register_blueprint(v1)
    with app.app_context():
        db.init_app(app)
        db.drop_all()
        db.create_all()

    return app


if __name__ == '__main__':
    init().run(debug=True)