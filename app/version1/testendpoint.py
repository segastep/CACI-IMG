import logging

from flask import request
from database import db
from database.model import Test as rep
from flask_restplus import Resource,reqparse

from . import serializers
from .api_object import api


log = logging.getLogger(__name__)

ns = api.namespace('test', description='Fck')


@ns.route('/')
class Test(Resource):
    @api.marshal_with(serializers.test)
    def get(self):
        return rep.query.all()


    @api.expect(serializers.test)
    def put(self):
        """
        Creates a new blog category.
        """
        data = request.json
        print(data)
        test1 = rep(data.get('name'))
        print(test1)
        db.session.add(test1)
        db.session.commit()
        return None, 201