from odoo import fields,models,api
class SchoolManager(models.Model):
    _name = "ct.classs"
    _description = "classs models"

    name = fields.Char('School Name', required=True)