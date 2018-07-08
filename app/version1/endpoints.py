import logging

from flask import request
from flask_restplus import Resource,reqparse

from . import serializers
from .api_object import api


log = logging.getLogger(__name__)

ns = api.namespace('people', description='Operations relating to people')



#auth = {
#    'Bearer': {
#        'type': 'apiKey',
#        'in': 'header',
#        'name': 'Authorization'
#    }
#}
## todo check how to do authentication
#v1 = Blueprint('v1', __name__, url_prefix='/api/v1')
#api = Api(v1, version='1.0', title="REST API", security='Bearer', authorizations=auth,
#          description="Demo RESTApi")
#


@ns.route('/')
class People(Resource):
    @api.marshal_with(serializers.person, as_list=True)
    def get(self):

        return  "z"





