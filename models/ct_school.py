from odoo import fields,models

class SchoolManager(models.Model):
    _name = "ct.school"
    _description = "school models"

    name = fields.Char('School Name', required=True)