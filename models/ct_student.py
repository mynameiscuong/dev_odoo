from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
from datetime import datetime, timedelta

_logger = logging.getLogger(__name__)

class Student(models.Model):
    _name = 'ct.student'
    _description = 'Student'

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age", required=True)
    class_id = fields.Many2one('ct.classs', string="Class", required=True)  
    school_ids = fields.Many2many('ct.school', string="Schools", required=True)
    email = fields.Char(string="Email", required=True)  
    state = fields.Selection([
        ('studying', 'Đang học'),
        ('graduated', 'Tốt nghiệp'),
        ('dropout', 'Bỏ học'),
    ], string="Trạng thái", default='studying')
    enrollment_date = fields.Date(string="Enrollment Date (Mặc định 4 năm tốt nghiệp)", required=True, default=lambda self: datetime.today().date()) 

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
    @api.model
    def create(self, vals):
        student = super(Student, self).create(vals)
        
        # Kiểm tra dữ liệu
        _logger.info("Creating student: %s", student.name)

        # Gửi email
        template = self.env.ref('school_management.email_template_student_welcome', raise_if_not_found=False)
        if template:
            _logger.info("Found email template, sending email to: %s", student.email)
            template.sudo().send_mail(student.id, force_send=True)
        else:
            _logger.warning("Email template not found!")

        return student
    
    def auto_update_student_status(self):
        graduation_date = datetime.today() - timedelta(days=4*365)
        students = self.search([('state', '=', 'studying'), ('enrollment_date', '<=', graduation_date.date())])

        for student in students:
            student.state = 'graduated'
            _logger.info(f"Đã cập nhật sinh viên {student.name} sang trạng thái 'Tốt nghiệp'")
