{
    'name': 'School Manage',
    'description': 'SChool Management By Cuong',
    'version': '1.0',
    'author': 'Cuong',
    'category': 'Basic',
    'sequence':-1,
    'depends': ['web','base'],
    'data': [
        'data/ct.student.csv',
        'security/ir.model.access.csv',
        'views/student_view.xml',
        'views/menus.xml',
        # 'views/school_view.xml',
        
        # 'views/headers.xml',
        # 'views/portal_my_home_dashboard.xml',
        # 'views/shop.xml',
        # 'data/theme_data.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}