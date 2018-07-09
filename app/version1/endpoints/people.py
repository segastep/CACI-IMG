import logging

from flask import request
from flask_restplus import Resource, reqparse

from app.version1 import serializers
from app.api_object import api
from database.model import Person
from database import db


log = logging.getLogger(__name__)

ns = api.namespace('people', description='Operations relating to people')

#  Serialize request
paginate = reqparse.RequestParser()
paginate.add_argument('page', type=int, required=False, default=1, help='Page number')
paginate.add_argument('per_page', type=int, required=False, choices=[2, 5, 20, 30, 40, 50, 100, 200, 300],
                      default=2, help='Results per page {error_msg}')


@ns.route('/')
class People(Resource):

    @api.expect(paginate)
    @api.marshal_with(serializers.page_of_people)
    def get(self):

        """Returns list of people details"""
        args = paginate.parse_args(request)
        page = args.get('page', 1)
        pages = args.get('pages', 500)
        result = Person.query.paginate(per_page=pages, page=page, error_out=False)
        return result

    @api.expect(serializers.person)
    @api.response(201, 'Person details were successfully created.')
    def post(self):

        """
        Creates a new person details record
        """

        person_record = Person(**request.json)
        db.session.add(person_record)
        #print(str(request.json))
        db.session.commit()
        return None, 201

@ns.route('/people/<string:username>')
class DeleteRecord(Resource):

    @api.response(204, 'Record deleted successfully.')
    def delete(self, username):

        """Deletes user record"""

        record = Person.query.filter(Person.username == username).one()
        db.session.delete(record)
        db.session.commit()

        return None, 204









