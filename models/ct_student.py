from odoo import models, fields, api

class Student(models.Model):
    _name = 'ct.student'
    _description = 'Student'

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age", required=True)
    student_class = fields.Char(string="Class")
    average_age = fields.Float(string="Average Age", compute="_compute_average_age")

    @api.depends('age')
    def _compute_average_age(self):
        students = self.search([])
        if students:
            total_age = sum(student.age for student in students)
            for student in students:
                student.average_age = total_age / len(students)
        else:
            for student in students:
                student.average_age = 0