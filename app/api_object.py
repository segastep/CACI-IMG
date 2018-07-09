import logging

from flask_restplus import Api

log = logging.getLogger(__name__)

# todo add security
api = Api(version='1.0', title="REST API", description="Demo RESTApi")
