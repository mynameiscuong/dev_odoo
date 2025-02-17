from odoo import models, fields, api

class Student(models.Model):
    _name = 'ct.student'
    _description = 'Student'

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age", required=True)
    class_id = fields.Many2one('ct.classs', string="Class")  # Mỗi học sinh thuộc về một lớp
    school_ids = fields.Many2many('ct.school', string="Schools")  # Một học sinh có thể học ở nhiều trường

    @api.constrains('class_id', 'school_ids')
    def _check_school_consistency(self):
        """ Kiểm tra nếu lớp thuộc một trường, nhưng học sinh chọn trường khác thì báo lỗi """
        for student in self:
            if student.class_id and student.class_id.school_id:
                valid_school = student.class_id.school_id  # Trường hợp pháp của lớp
                if valid_school not in student.school_ids:
                    raise ValidationError(f"Học sinh '{student.name}' đang thuộc lớp '{student.class_id.name}', "
                                          f"nhưng lớp này chỉ thuộc trường '{valid_school.name}'. "
                                          f"Vui lòng chọn đúng trường!")