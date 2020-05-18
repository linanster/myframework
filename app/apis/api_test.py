from flask_restful import Api, Resource

from app.lib.mydecorator import viewfunclog

api_test = Api(prefix='/api/test/')

class ResourceTest(Resource):

    @viewfunclog
    def get(self):
        return {'msg':'hello api get'}

    @viewfunclog
    def post(self):
        return {'msg':'hello api post'}


api_test.add_resource(ResourceTest, '/')
