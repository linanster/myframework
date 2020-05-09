from flask import request, abort
from flask_restful import Api, Resource, fields, marshal_with, marshal, reqparse

from app.models.sqlite import Student

api_db_student = Api(prefix='/api/db/student/')


#####################################################################
### 1.1 fields definition, for marshal (custom object serializing) ###
#####################################################################

fields_student_single_db = {
    'name': fields.String,
    'age': fields.Integer,
    'exampass': fields.Boolean,
    'updatetime': fields.DateTime(dt_format='iso8601')
}

fields_student_single_response = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.Nested(fields_student_single_db)
}

fields_student_list_response = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(fields_student_single_db))
}


#################################
### 1.2 parser initialization ###
#################################

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help='name required', location=['form', 'args'])
parser.add_argument('age', type=int, required=True, help='age required', location=['form', 'args'])
parser.add_argument('exampass', type=bool, required=True, help='exampass required', location=['form', 'args'])



####################################
### 2. resource class definition ###
####################################

class ResourceStudentSingle(Resource):

    @marshal_with(fields_student_single_response)
    def get(self, id):
        response_status = 200
        response_msg = 'student with id {}'.format(id)
        response_data = Student.query.get(id)
        response_obj = {
            'status': response_status,
            'msg': response_msg,
            'data': response_data
        }
        return response_obj      

    @marshal_with(fields_student_single_response)
    def delete(self, id):
        data = Student.query.get(id)
        if not data:
            abort(404)
        if not data.delete():
            abort(400)
        response_status = 200
        response_msg = 'delete student with id {} success'.format(id)
        response_obj = {
            'status': response_status,
            'msg': response_msg,
            'data': data
        }
        return response_obj 

    @marshal_with(fields_student_single_response)
    def put(self, id):
        data = Student.query.get(id)
        if not data:
            abort(404)
        # r_name = request.form.get('name', type=str)
        # r_age = request.form.get('age', type=int)
        # r_exampass = request.form.get('exampass', type=bool)
        args = parser.parse_args()
        r_name = args.get('name')
        r_age = args.get('age')
        r_exampass = args.get('exampass')
        data.name = r_name
        data.age = r_age
        data.exampass = r_exampass
        if not data.save():
            abort(400)
        response_status = 200
        response_msg = 'put student with id {} success'.format(id)
        response_obj = {
            'status': response_status,
            'msg': response_msg,
            'data': data
        }
        return response_obj         
        
    @marshal_with(fields_student_single_response)
    def patch(self, id):
        data = Student.query.get(id)
        if not data:
            abort(404)
        r_name = request.form.get('name', type=str)
        r_age = request.form.get('age', type=int)
        r_exampass = request.form.get('exampass', type=bool)
        data.name = r_name or data.name
        data.age = r_age or data.age
        data.exampass = r_exampass or data.exampass
        if not data.save():
            abort(400)
        response_status = 200
        response_msg = 'patch student with id {} success'.format(id)
        response_obj = {
            'status': response_status,
            'msg': response_msg,
            'data': data
        }
        return response_obj         


  
class ResourceStudentList(Resource):

    @marshal_with(fields_student_list_response)
    def get(self):
        response_status = 200
        response_msg = 'all student data'
        response_data = Student.query.all()
        response_obj = {
            'status': response_status,
            'msg': response_msg,
            'data': response_data
        }
        return response_obj      

    @marshal_with(fields_student_list_response)
    def post(self):
        r_name = request.form.get('name', type=str)
        r_age = request.form.get('age', type=int)
        r_exampass = request.form.get('exampass', type=bool)
        data = Student()
        data.name = r_name
        data.age = r_age
        data.exampass = r_exampass
        if not data.save():
            abort(400)
        response_status = 200
        response_msg = 'post student with name {} success'.format(r_name)
        response_obj = {
            'status': response_status,
            'msg': response_msg,
            'data': data
        }
        return response_obj
        


##############################
### 3. Resourceful Routing ###
##############################

api_db_student.add_resource(ResourceStudentSingle, '/<int:id>')
api_db_student.add_resource(ResourceStudentList, '/all', '/add')






