from flask_restful import Api, Resource, reqparse, fields
from flask import request, send_from_directory, Response
import os
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

from app.myglobals import uploadfolder, topdir
from app.lib.mydecorator import viewfunclog
from app.lib.myauth import my_login_required

api_file = Api(prefix='/api/file/')



# fields_filenames = {}


parser1 = reqparse.RequestParser()
parser1.add_argument('filename', type=str, required=True, help='download filename required', location=['args', 'form'])
parser2 = reqparse.RequestParser()
parser2.add_argument('file', type=FileStorage, required=True, help='upload file required', location=['files'])

def send_file(filepath):
    with open(filepath, 'rb') as filestream:
        while True:
            data = filestream.read(1024*1024) # 每次读取1M大小
            if not data:
                break
            yield data


class ResourceFile(Resource):

    @viewfunclog
    def get(self):
        # args = parser1.parse_args()
        # filename = args.get('filename')
        filename = request.args.get('filename')
        downloadfile = os.path.join(uploadfolder, filename)
        # response = Response(send_file(sourcefile), content_type='application/octet-stream')
        response = Response(send_file(downloadfile), content_type='image/png')
        # response.headers["Content-disposition"] = 'attachment; filename=%s' % filename
        return response

    @my_login_required
    @viewfunclog
    def put(self):
        # file = request.files.get('file')
        # args = parser2.parse_args()
        # file = args.get('file')
        # type of files is generator
        locations = list()
        # for myfile in request.files.values():
        for fileparam, myfile in request.files.items():
            if not myfile:
                return {
                    'status': 406,
                    'msg':'no file found',
                }
            if myfile.filename == '':
                return {
                    'status': 406,
                    'msg': 'no file seleted',
                }
            filename = secure_filename(myfile.filename)
            filename = os.path.join(uploadfolder, filename)
            myfile.save(filename)
            locations.append(filename.lstrip(topdir))
        return {
            'status': 201,
            'msg': 'upload success',
            'location': locations,
        }

class ResourceFiles(Resource):
    @viewfunclog
    def get(self):
        filenamelist = os.listdir(uploadfolder)
        return {
            'status':202,
            'msg': 'all files',
            'filelist': filenamelist,
        }

class ResourceImage(Resource):

    # postman send request: body->form data,key 'image' type is 'File', and then select file
    @viewfunclog
    def put(self):
        token = request.args.get('token') or 'None'
        userid = request.form.get('locationid')
        locationid = request.form.get('locationid')
        homeid = request.form.get('homeid')
        loadid = request.form.get('loadid')
        on  = request.form.get('on')

        filename = os.path.join(uploadfolder, 'upload.png')

        image = request.files.get('image')
        image.save(filename)

        return {
            'code':0,
            'msg': 'upload success',
            'token': token,
            'userid': userid,
            'locationid': locationid,
            'homeid': homeid,
            'loadid': loadid,
            'on': on,
        }

    # python request to handle response:
    # with open('./1.png', 'wb') as myfile:
    #     myfile.save(response.content)
    @viewfunclog
    def get(self):
        token = request.args.get('token')
        userid = request.form.get('userid')
        locationid = request.form.get('locationid')
        homeid = request.form.get('homeid')
        loadid = request.form.get('loadid')
        on  = request.form.get('on')

        filename = '/git/myframework/upload/upload.png'

        response = Response(send_file(filename), content_type='image/png')
        return response

    @viewfunclog
    def delete(self):
        token = request.args.get('token')
        userid = request.form.get('userid')
        locationid = request.form.get('locationid')
        homeid = request.form.get('homeid')
        loadid = request.form.get('loadid')
        on  = request.form.get('on')

        filename = '/git/myframework/upload/upload.png'

        os.remove(filename)
        return {
            'code': 0,
            'msg':'delete success',
            'token': token,
            'userid': userid,
            'locationid': locationid,
            'homeid': homeid,
            'loadid': loadid,
            'on': on,
        }

class ResourceBinary(Resource):

    # postman send request: body->binary,select file
    @viewfunclog
    def put(self):
        filename = os.path.join(uploadfolder, 'upload.binary')
        data = request.get_data()
        fileobj = open(filename, 'wb')
        fileobj.write(data)
        fileobj.close()
        return {
            'code': 0,
            'msg': 'upload success',
        }

    # python request to handle response:
    # with open('./1.data', 'wb') as myfile:
    #     myfile.write(response.content)
    @viewfunclog
    def get(self):
        filename = os.path.join(uploadfolder, 'upload.binary')
        response = Response(send_file(filename), content_type='application/octet-stream')
        return response

    @viewfunclog
    def delete(self):

        filename = os.path.join(uploadfolder, 'upload.binary')

        os.remove(filename)
        return {
            'code': 0,
            'msg':'delete success',
        }


api_file.add_resource(ResourceFile, '/file/upload', '/file/download')
api_file.add_resource(ResourceFiles, '/files/view')
api_file.add_resource(ResourceImage, '/image')
api_file.add_resource(ResourceBinary, '/binary')
