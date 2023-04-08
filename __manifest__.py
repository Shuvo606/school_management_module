# -*- coding: utf-8 -*-
{
    'name': 'School Application',
    'summary': """School Application.""",
    'description': """
App Name
========
Something about the App.
    """,
    'version': '16.0.1.0',
    'author': 'Company Name',
    'website': 'http://www.company.com',
    'category': 'Tools',
    'sequence': 1,
    'depends': [
        'base',
        'web',
    ],
    'data': [
        ## Data
        'data/ir_sequence.xml',

        ## Security
        'security/ir.model.access.csv',
        
        ## View
        'views/application_view.xml',
        'views/student_view.xml',

        # Menus
        'views/menus.xml',
    ],
    'qweb': [
        ## Template
        'static/src/xml/*.xml',
    ],
    'assets': {
        'web.assets_backend': [
            ('include', 'school_module/static/src/css/web_assets_backend.css'),
            ('include', 'school_module/static/src/js/web_assets_backend.js'),
        ],
        'web.assets_frontend': [
            ('include', 'school_module/static/src/css/web_assets_frontend.css'),
            ('include', 'school_module/static/src/js/web_assets_frontend.js'),
        ],
        'web.assets_common': [
            ('include', 'school_module/static/src/css/web_assets_common.css'),
            ('include', 'school_module/static/src/js/web_assets_common.js'),
        ],
    },
    'demo': [
        ## Demo Data
        'demo/my_model_name_demo.xml',
    ],
    'external_dependencies': {
        'python': [
            'werkzeug',
        ],
    },
    'icon': '/school_module/static/description/schoolicon.png',
    'images': [
        'static/description/schoolicon.png',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 0,
    'currency': 'EUR',
    'license': 'OPL-1',
    'contributors': [
        'Jeshad Khan <https://github.com/jeshadkhan>',
    ],
}
