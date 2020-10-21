from flask import request, Response
from flask_restful import Api, Resource
from werkzeug.utils import secure_filename
import os

from app.lib.mydecorator import viewfunclog
from app.lib.myauth import http_basic_auth, my_login_required, my_permission_required, my_pin1_required

from app.myglobals import uploadfolder, topdir

api_test = Api(prefix='/api/test/')

def read_file_binary_normal(filename):
    with open(filename, 'rb') as fileobj:
        mydata = fileobj.read()
    return mydata

def read_file_binary_stream(filename):
    with open(filename, 'rb') as filestream:
        while True:
            mydata = filestream.read(1024*1024) # 每次读取1M大小
            if not mydata:
                break
            yield mydata


# 1. request args parameter
class ResourceTest1(Resource):
    @viewfunclog
    def get(self):
        username = request.args.get('username')
        password = request.args.get('password')
        return {
            'username': username,
            'password': password
        }

# 2. request form parameter
class ResourceTest2(Resource):
    @viewfunclog
    def get(self):
        username = request.form.get('username')
        password = request.form.get('password')
        return {
            'username': username,
            'password': password
        }

# 3. request form text
class ResourceTest3(Resource):
    @viewfunclog
    def get(self):
        username = request.form.get('username')
        password = request.form.get('password')
        return {
            'username': username,
            'password': password
        }

# 4. request form file
class ResourceTest4(Resource):
    @viewfunclog
    def get(self):
        file1 = request.files.get('file1')
        file2 = request.files.get('file2')
        return {
            'file1': file1.filename,
            'file2': file2.filename,
        }

# 5. request text
class ResourceTest5(Resource):
    @viewfunclog
    def get(self):
        text = request.get_data(as_text=True)
        return {
            'text': text,
        }

# 6. request json
class ResourceTest6(Resource):
    @viewfunclog
    def get(self):
        username = request.json.get('username')
        password = request.json.get('password')
        alljson = request.get_json()
        return {
            'username': username,
            'password': password,
            'raw': alljson,
        }

# 7. request binary
class ResourceTest7(Resource):
    @viewfunclog
    def get(self):
        data = request.data
        filename = '/git/myframework/upload/test.binary'
        fileobj = open(filename, 'wb')
        fileobj.write(data)
        fileobj.close()        
        return {
            'datatype': str(type(data)),
            'datasize': len(data),
            'datasave': filename
        }

# 11. response text
# response.text
# scripts/apitest/api_test_test11.py
class ResourceTest11(Resource):
    @viewfunclog
    def get(self):
        mytext = "How are you?"
        # return mytext
        response = Response(mytext, content_type='text/plain')
        return response

# 12. response json
# response.json()
# scripts/apitest/api_test_test12.py
class ResourceTest12(Resource):
    @viewfunclog
    def get(self):
        myjson = {"username":"user1", "password":"123456"}
        # return myjson
        response = Response(myjson, content_type='application/json')
        return response

# 13. response binary
# response.content
# scripts/apitest/api_test_test13.py
class ResourceTest13(Resource):
    @viewfunclog
    def get(self):
        filename = '/git/myframework/upload/test.binary'
        # 1.1 普通读取文件为二进制数据
        mydata = read_file_binary_normal(filename)
        # 1.2 流式读取文件为二进制数据
        # mydata = read_file_binary_stream(filename)
        # 2.1 Content-Type: application/octet-stream, Postman成功接收response，但无法显示图片
        response = Response(mydata, content_type='application/octet-stream')
        # 2.2 Content-Type: image/png, Postman成功接收response，可以显示图片
        # response = Response(mydata, content_type='image/png')
        return response

# 14. list all files in upload folder
class ResourceTest14(Resource):
    @viewfunclog
    def get(self):
        filenamelist = os.listdir(uploadfolder)
        return {
            'status':202,
            'msg': 'all files',
            'filelist': filenamelist,
        }

# 15. download and upload file
# request.files
# request.files.get('file1')
class ResourceTest15(Resource):
    # 下载文件
    @viewfunclog
    def get(self):
        filename = request.args.get('filename') or request.form.get('filename')
        filename = os.path.join(uploadfolder, filename)
        mydata = read_file_binary_normal(filename)
        # below style is incorrect!
        # return mydata
        response = Response(mydata)
        # 如果约定文件类型，为response添加content_type消息头
        # response = Response(mydata, content_type='text/plain')
        # response = Response(mydata, content_type='image/png')
        return response
    # 上传文件
    # @my_login_required
    @viewfunclog
    def put(self):
        # 1.1 fetch multiple files from request
        # for myfiles in request.files.values()
        # type of myfiles is generator
        # 1.2 fetch single one file from request
        myfile = request.files.get('file1')
        if not myfile or myfile.filename == '':
            return {
                'status': 406,
                'msg':'no file found',
            }
        filename = secure_filename(myfile.filename)
        filename = os.path.join(uploadfolder, filename)
        location = filename.lstrip(topdir)
        myfile.save(filename)
        return {
            'status': 201,
            'msg': 'upload success',
            'location': location,
        }

# 101. 验证http_basic_auth.login_required
class ResourceTest101(Resource):
    @http_basic_auth.login_required
    @viewfunclog
    def get(self):
        return {
            'status': 'http_basic_auth login success'
        }
# 102. 验证my_login_required
class ResourceTest102(Resource):
    @my_login_required
    @viewfunclog
    def get(self):
        return {
            'status': 'my_login_required login success'
        }
# 103. 验证my_permission_required
class ResourceTest103(Resource):
    @my_login_required
    # user1 permission unsufficient
    # user2 and user3 permission sufficient
    @my_permission_required(3)
    @viewfunclog
    def get(self):
        return {
            'status': 'my_permission_required login success'
        }

class ResourceTest104(Resource):
    @my_pin1_required
    @viewfunclog
    def get(self):
        return {
            'msg': 'my_pin1_required success'
        }

api_test.add_resource(ResourceTest1, '/test1')
api_test.add_resource(ResourceTest2, '/test2')
api_test.add_resource(ResourceTest3, '/test3')
api_test.add_resource(ResourceTest4, '/test4')
api_test.add_resource(ResourceTest5, '/test5')
api_test.add_resource(ResourceTest6, '/test6')
api_test.add_resource(ResourceTest7, '/test7')
api_test.add_resource(ResourceTest11, '/test11')
api_test.add_resource(ResourceTest12, '/test12')
api_test.add_resource(ResourceTest13, '/test13')
api_test.add_resource(ResourceTest14, '/test14')
api_test.add_resource(ResourceTest15, '/test15')
api_test.add_resource(ResourceTest101, '/test101')
api_test.add_resource(ResourceTest102, '/test102')
api_test.add_resource(ResourceTest103, '/test103')
api_test.add_resource(ResourceTest104, '/test104')
