from flask import request
from flask_restful import Api, Resource

from app.lib.mydecorator import viewfunclog

api_test = Api(prefix='/api/test/')

class ResourceTest1(Resource):
    @viewfunclog
    def get(self):
        username = request.form.get('username')
        password = request.form.get('password')
        return {
            'username': username,
            'password': password
        }

    @viewfunclog
    def post(self):
        return {'msg':'hello api post'}


class ResourceTest2(Resource):
    @viewfunclog
    def get(self):
        username = request.json.get('username')
        password = request.json.get('password')
        return {
            'username': username,
            'password': password
        }


class ResourceTest3(Resource):
    @viewfunclog
    def get(self):
        payload = request.get_data(as_text=True)
        return {
            'payload': payload
        }

api_test.add_resource(ResourceTest1, '/test1')
api_test.add_resource(ResourceTest2, '/test2')
api_test.add_resource(ResourceTest3, '/test3')
