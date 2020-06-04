from flask import request, redirect
from flask_restful import Api, Resource
import subprocess as s

from app.lib.mydecorator import viewfunclog
from app.lib.socketioutils import send_msg_hello

api_cmd = Api(prefix='/api/cmd/')

def my_check_output(cmd):
    try:
        output = s.check_output([cmd, ])
    except s.CalledProcessError as e:
        return str(e)
    except Exception as e:
        return str(e)
    else:
        # return output.decode('utf-8')
        return output.decode()

class ResourceCmd1(Resource):
    @viewfunclog
    def post(self):
        send_msg_hello()
        return {
            'msg': 'ok',
            'status': 200,
        }

class ResourceCmd2(Resource):
    @viewfunclog
    def get(self):
        return {
            'msg': 'ok',
            'method': 'get',
        }
    @viewfunclog
    def post(self):
        # cmd = request.json.get('cmd')
        cmd = request.form.get('cmd')
        output = my_check_output(cmd)
        print('==cmd==', cmd)
        print('==output==', output)
        return {
            'msg': 'ok',
            'method': 'post',
            'output': output,
        }


api_cmd.add_resource(ResourceCmd1, '/send_msg_hello', endpoint='api_cmd_sendmsg')
api_cmd.add_resource(ResourceCmd2, '/onlinecmd', endpoint='api_cmd_onlinecmd')
