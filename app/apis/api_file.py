from flask_restful import Api, Resource, reqparse, fields
from flask import request
import os
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

from app.myglobals import uploadfolder
from app.lib.mydecorator import viewfunclog

api_file = Api(prefix='/api/file/')



# fields_filenames = {}


parser = reqparse.RequestParser()
# parser.add_argument('filename', type=str, required=True, help='download filename required', location=['args', 'form'])
parser.add_argument('file', type=FileStorage, required=True, help='upload file required', location=['files'])

class ResourceFile(Resource):

    @viewfunclog
    def get(self):
        pass

    @viewfunclog
    def put(self):
        # file = request.files.get('file')
        args = parser.parse_args()
        file = args.get('file')

        if not file:
            return {
                'status': 401,
                'msg':'no file found',
            }
        if file.filename == '':
            return {
                'status': 401,
                'msg': 'no file seleted',
            }
        filename = secure_filename(file.filename)
        destfile = os.path.join(uploadfolder, filename)
        file.save(destfile)
        return {
            'status': 200,
            'msg': 'upload success',
            'location': destfile,
        }

class ResourceFiles(Resource):
    @viewfunclog
    def get(self):
        filenamelist = os.listdir(uploadfolder)
        return {
            'status':200,
            'msg': 'all files',
            'filelist': filenamelist,
        }


api_file.add_resource(ResourceFile, '/file/upload')
api_file.add_resource(ResourceFiles, '/files/view')
