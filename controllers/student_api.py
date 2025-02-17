from odoo import http
from odoo.http import request, Response
import json

class StudentAPI(http.Controller):

    # Lấy danh sách sinh viên
    @http.route('/api/students', type='json', auth='none', methods=['GET'], csrf=False)
    def get_students(self):
        students = request.env['ct.student'].sudo().search([])
        student_list = [{
            'id': student.id,
            'name': student.name,
            'age': student.age,
            'class': student.class_id.name if student.class_id else None,
            'school_ids': [school.name for school in student.school_ids]
        } for student in students]

        return student_list

    # Tạo sinh viên mới
    @http.route('/api/students', type='http', auth='none', methods=['POST'], csrf=False)
    def create_student(self):
            data = request.httprequest.get_json()

            # Lấy thông tin từ JSON
            name = data.get('name')
            age = data.get('age')
            class_name = data.get('class')  # Tên lớp
            school_names = data.get('school_ids', [])  # Danh sách tên trường

            # Kiểm tra dữ liệu đầu vào
            if not name or not age or not class_name:
                return Response(
                    json.dumps({"error": "Missing required fields (name, age, class)"}),
                    content_type='application/json', status=400
                )

            # Tìm class_id dựa trên tên lớp
            class_obj = request.env['ct.classs'].sudo().search([('name', '=', class_name)], limit=1)
            if not class_obj:
                return Response(
                    json.dumps({"error": f"Class '{class_name}' not found"}),
                    content_type='application/json', status=404
                )

            # Tìm danh sách school_id dựa trên tên trường
            school_objs = request.env['ct.school'].sudo().search([('name', 'in', school_names)])
            if not school_objs:
                return Response(
                    json.dumps({"error": f"Schools {school_names} not found"}),
                    content_type='application/json', status=404
                )

            # Tạo sinh viên mới
            new_student = request.env['ct.student'].sudo().create({
                'name': name,
                'age': int(age),
                'class_id': class_obj.id,  # Gán class_id từ class tìm được
                'school_ids': [(6, 0, school_objs.ids)],  # Gán danh sách school_id
            })

            # Trả về dữ liệu JSON của sinh viên vừa tạo
            student_data = {
                'id': new_student.id,
                'name': new_student.name,
                'age': new_student.age,
                'class': new_student.class_id.name,
                'school_ids': [school.name for school in new_student.school_ids]
            }

            return Response(json.dumps(student_data), content_type='application/json', status=201)

