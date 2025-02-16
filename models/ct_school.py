from odoo import fields,models

class School(models.Model):
    _name = "ct.school"
    _description = "School models"

    name = fields.Char('School Name', required=True)
    class_ids = fields.One2many('ct.classs', 'school_id', string="Classes")  # Một trường có nhiều lớp
    student_ids = fields.Many2many('ct.student', string="Students")  # Một trường có nhiều học sinh
