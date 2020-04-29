from flask_restful import Api, Resource

apitest = Api(prefix='/api/test/')

class ResourceTest(Resource):
    def get(self):
        return {'msg':'hello api get'}
    def post(self):
        return {'msg':'hello api post'}


apitest.add_resource(ResourceTest, '/')
