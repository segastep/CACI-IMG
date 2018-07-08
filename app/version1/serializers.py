from app.version1.api_object import api
from flask_restplus import fields


"""
Since the Spec did not say anything about required fields for the schema, it was assumed all fields are required.
The model below corresponds to the json layout from sample data.

"""

"""
   Person schema layout
   
   {
   "job":"Solicitor",
   "company":"Smith, Haynes and Hooper",
   "ssn":"ZZ376803T",
   "residence":"1 Bruce alley\/nNew Justin\/nL07 2TE",
   "current_location":[
      -66.491849,
      -69.512524
   ],
   "blood_group":"AB+",
   "website":[
      "https://www.holmes-saunders.com/",
      "http://foster-ford.com/",
      "https://www.farrell-evans.com/",
      "http://white-kelly.net/"
   ],
   "username":"test",
   "name":"Dr. Mohamed Newton",
   "sex":"F",
   "address":"09 Knight parkways\/nWest Yvonneshire\/nHD23 5NJ",
   "mail":"jshort@hotmail.com",
   "birthdate":"1989-07-07"
}
"""
test = api.model('Test', {'name': fields.String(description='FFF', required=True)})

person = api.model('Person Schema', {
                 "job": fields.String(description="Person's job", required=True),
                 "company": fields.String(descriprion="Company", required=True),
                 "ssn": fields.String(description="SSN", required=True),
                 "residence": fields.String(description="Residence", required=True),
                 "website": fields.List(fields.Url(), required=True, description='Websites associated with user'),
                 "blood_group": fields.String(description="User's blood group", required=True),
                 "username": fields.String(description="Username", required=True),
                 "name": fields.String(description="User's names", required=True),
                 "sex": fields.String(description="User's gender", required=True),
                 "address": fields.String(description="Address", required=True),
                 "mail": fields.String(description="Email address", required=True),
                 "birthdate": fields.Date(description="User's data of birth", required=True),
                 "location": fields.List(fields.Float(description="User's location", required=True), required=True)
                })


