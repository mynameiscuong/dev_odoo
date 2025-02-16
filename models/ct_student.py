from odoo import models, fields, api

class Student(models.Model):
    _name = 'ct.student'
    _description = 'Student'

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age", required=True)
    class_id = fields.Many2one('ct.classs', string="Class")  # Mỗi học sinh thuộc về một lớp
    school_ids = fields.Many2many('ct.school', string="Schools")  # Một học sinh có thể học ở nhiều trường