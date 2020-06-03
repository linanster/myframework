from flask import request, redirect
from flask_restful import Api, Resource

from app.lib.mydecorator import viewfunclog
from app.lib.socketioutils import send_msg_hello

api_cmd = Api(prefix='/api/cmd/')

class ResourceCmd1(Resource):
    @viewfunclog
    def post(self):
        send_msg_hello()
        return {
            'msg': 'ok',
            'status': 200,
        }


api_cmd.add_resource(ResourceCmd1, '/send_msg_hello', endpoint='api_send_msg_hello')
