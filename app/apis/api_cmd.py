from flask import request, redirect
from flask_restful import Api, Resource, reqparse
import subprocess as s

from app.lib.mydecorator import viewfunclog
from app.lib.socketioutils import send_msg_hello

api_cmd = Api(prefix='/api/cmd/')


parser = reqparse.RequestParser()
parser.add_argument('cmd', type=str, location=['args', 'form'])



def my_check_output(cmd):
    try:
        cmd_list = cmd.split(' ')
        # print('==cmd_list==', cmd_list)
        output = s.check_output(cmd_list, stderr=s.STDOUT)
    # todo: subprocess.CalledProcessError can't be captured, don't know why it happen
    except s.CalledProcessError as e:
        # print('==CalledProcessError==')
        return e.output.decode()
    except Exception as e:
        # print('==Exception==')
        # print(type(e))
        try:
            return e.output.decode()
        except:
            return str(e)
    else:
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
        # cmd = request.form.get('cmd')
        args = parser.parse_args()
        cmd = args.get('cmd')
        output = my_check_output(cmd)
        return {
            'msg': 'ok',
            'method': 'post',
            'output': output,
        }


api_cmd.add_resource(ResourceCmd1, '/send_msg_hello', endpoint='api_cmd_sendmsg')
api_cmd.add_resource(ResourceCmd2, '/onlinecmd', endpoint='api_cmd_onlinecmd')
