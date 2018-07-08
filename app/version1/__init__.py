from flask import jsonify, Blueprint
from flask_restplus import Resource, Api, fields, reqparse
from . import api_schema_model

auth = {
    'Bearer': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}
# todo check how to do authentication
v1 = Blueprint('v1', __name__, url_prefix='/api/v1')
api = Api(v1, version='1.0', title="REST API", security='Bearer', authorizations=auth,
          description="Demo RESTApi")

schema = api_schema_model.get_model(v1,api)



website = api.model('Website', {})
res =  {"job": "Solicitor", "company": "Smith, Haynes and Hooper", "ssn": "ZZ376803T", "residence": "1 Bruce alley\nNew Justin\nL07 2TE", "current_location": [-66.491849, -69.512524],
  "blood_group": "AB+",
  "website":
      ["https://www.holmes-saunders.com/", "http://foster-ford.com/", "https://www.farrell-evans.com/", "http://white-kelly.net/"],
  "username": "mauriceharris",
  "name": "Dr. Mohamed Newton",
  "sex": "F",
  "address": "09 Knight parkways\nWest Yvonneshire\nHD23 5NJ",
  "mail": "jshort@hotmail.com",
  "birthdate": "1989-07-07"
  }

res_list = [res, res, res, res]
@api.route('/people')
class People(Resource):
    def get(self):
        return res



