from flask_restful import Api, Resource

api_test = Api(prefix='/api/test/')

class ResourceTest(Resource):
    def get(self):
        return {'msg':'hello api get'}
    def post(self):
        return {'msg':'hello api post'}


api_test.add_resource(ResourceTest, '/')
