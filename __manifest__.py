{
    'name': 'school_management',
    'description': 'SChool Management By Cuong',
    'version': '1.0',
    'author': 'Cuong',
    'category': 'Basic',
    'sequence':-1,
    'depends': ['web','base'],
    'data': [
        'security/ir.model.access.csv',
        # 'data/school_data.xml',
        # 'data/classs_data.xml',
        # 'data/student_data.xml',
        'data/ct.school.csv',
        'data/ct.classs.csv',
        'data/ct.student.csv',

        

        'report/report_student_list.xml',
        'report/student_report.xml',

        'views/student_view.xml',
        'views/menus.xml',
        # 'views/school_view.xml',


    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}