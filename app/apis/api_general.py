from flask import request, redirect
from flask_restful import Api, Resource, reqparse

from app.lib.mydecorator import viewfunclog

api_general = Api(prefix='/api/general/')


parser = reqparse.RequestParser()
# parser.add_argument('cmd', type=str, location=['args', 'form'])



class ResourceMyIP(Resource):
    @viewfunclog
    def get(self):
        myip = request.remote_addr
        return {
            'msg': 'ok',
            'myip': myip,
        }


api_general.add_resource(ResourceMyIP, '/myip', endpoint='api_general_myip')
