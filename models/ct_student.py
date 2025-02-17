from odoo import models, fields, api
from odoo.exceptions import ValidationError  # Import lỗi validation

class Student(models.Model):
    _name = 'ct.student'
    _description = 'Student'

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age", required=True)
    class_id = fields.Many2one('ct.classs', string="Class", required=True)  
    school_ids = fields.Many2many('ct.school', string="Schools", required=True)  

    @api.constrains('class_id', 'school_ids')
    def _check_school_consistency(self):
        """ Kiểm tra nếu lớp thuộc một trường, nhưng học sinh chọn trường khác thì báo lỗi """
        for student in self:
            if student.class_id and student.class_id.school_id:
                valid_school = student.class_id.school_id  # Trường của lớp
                selected_schools = student.school_ids  # Trường mà học sinh được chọn

                # Kiểm tra học sinh chỉ có thể thuộc đúng trường của lớp
                if any(school.id != valid_school.id for school in selected_schools):
                    raise ValidationError(
                        f"Lỗi: Học sinh '{student.name}' thuộc lớp '{student.class_id.name}', "
                        f"nhưng lớp này chỉ thuộc trường '{valid_school.name}'. "
                        f"Vui lòng chọn đúng trường!"
                    )