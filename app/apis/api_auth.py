from flask import request, abort, jsonify, url_for, g
from flask_restful import Api, Resource, fields, marshal_with, marshal, reqparse

from app.models.sqlite import User
from app.myauth import http_basic_auth

api_auth = Api(prefix='/api/auth/')


fields_user_single_db = {
    'username': fields.String,
    'password': fields.String,
    'password_hash': fields.String,
}

fields_user_single_response = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.Nested(fields_user_single_db)
}

fields_user_list_response = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(fields_user_single_db))
}



class ResourceUserSingle(Resource):
    @marshal_with(fields_user_single_db)
    def get(self, id):
        return User.query.get(id)



class ResourceUserList(Resource):
    @marshal_with(fields_user_list_response)
    def get(self):
        users = User.query.all()
        response_obj = {
            'status': 201,
            'msg': 'all users data',
            'data': users
        }
        return response_obj

    @marshal_with(fields_user_single_response)
    def post(self):
        # username = request.json.get('username')
        # password = request.json.get('password')
        username = request.form.get('username')
        password = request.form.get('password')
        if username is None or password is None:
            abort(400)
        if User.query.filter_by(username = username).first() is not None:
            abort(400)
        user = User(username = username)
        user.hash_password(password)
        if not user.save():
            abort(400)
        # return jsonify({ 'username': user.username }), 201, {'Location': url_for('get_user', id = user.id, _external = True)}        
        response_obj = {
            'status': 201,
            'msg': 'user {} register success'.format(user.username),
            'data': user
        }
        return response_obj, 201, {'Location': url_for('get_user', id = user.id, _external = True)}        

class ResourceToken(Resource):
    @http_basic_auth.login_required
    def get(self):
        token = g.user.generate_auth_token()
        return {'token': token.decode('ascii')}
    
class ResourceLoginTest(Resource):
    @http_basic_auth.login_required
    def get(self):
        return "login as {}:{} test success".format(g.user.username, g.user.password)

api_auth.add_resource(ResourceUserSingle, '/user/<int:id>', endpoint='get_user')
api_auth.add_resource(ResourceUserList, '/users', '/register', endpoint='get_users')
api_auth.add_resource(ResourceToken, '/token')

api_auth.add_resource(ResourceLoginTest, '/logintest')

# api verification example by crul
# 1. get token
# curl -u user1:123456 -i -X GET http://10.30.30.101:4000/api/auth/token
# curl -X GET 'http://10.30.30.101:4000/api/auth/token' --header 'Authorization: Basic dXNlcjE6MTIzNDU2'
# "user1:123456" --base64--> "dXNlcjE6MTIzNDU2"
# 2. login test by token
# curl -u eyJhbGciOiJIUzUxMiIsImlhdCI6MTU4OTA1MTUzMiwiZXhwIjoxNTg5MDUyMTMyfQ.eyJpZCI6MX0.igadnHdP7lKHh311dEVF7lRVbdg3JwdgyUHBtWxwEEvAnT-0D2Lnd2rkktmkPxj_Zdob4XBi2bYoqPgwpcu05w:password -i -X GET http://10.30.30.101:4000/api/auth/logintest



