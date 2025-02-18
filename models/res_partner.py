from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_student = fields.Boolean(string="Is Student", default=False)
    student_id = fields.Many2one('ct.student', string="Student", ondelete='set null')

    def action_open_student_form(self):
        """ Mở form student từ partner """
        self.ensure_one()
        return {
            'name': 'Student',
            'type': 'ir.actions.act_window',
            'res_model': 'ct.student',
            'view_mode': 'form',
            'res_id': self.student_id.id,
            'target': 'current',
        }
