from odoo import fields,models,api
class Classs(models.Model):
    _name = "ct.classs"
    _description = "Classs models"

    name = fields.Char(string='Class Name', required=True)
    school_id = fields.Many2one('ct.school', string='School')  # Mỗi lớp thuộc về một trường
    school_name = fields.Char(string='School Name', related='school_id.name', store=True)  # Tên trường
    student_ids = fields.One2many('ct.student', 'class_id', string="Students")  # Một lớp có nhiều học sinh
    average_age = fields.Float(string="Average Age", compute="_compute_average_age", store=True)  # Tuổi trung bình

    @api.depends('student_ids.age')
    def _compute_average_age(self):
        for classs in self:
            students = classs.student_ids
            if students:
                total_age = sum(student.age for student in students)
                classs.average_age = total_age / len(students)
            else:
                classs.average_age = 0