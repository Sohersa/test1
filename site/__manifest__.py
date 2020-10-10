# -*- coding: utf-8 -*-
{
    'name': "site",
    'summary': 'web site, you can see my totorials',
    'description': """
    TUTORIALS
    ------------------------------------------------------------------
        PYTHON:
            - FUNCTIONAL PROGRAMMING
            - POO
            - SCANNER
            - SCRAPPING
        ANGULAR 8:
            - MODULES
            - SERVICES
            - OBSERVERS
    -------------------------------------------------------------------
    MORE ABOUT US:
        WEB SITE: www.odoo.com
        EMAIL: car@gmil.com
    """,
    'author': "Sohersa",
    'website': "http://www.odoo.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services/site',
    'version': '0.2',
    # any module necessary for this one to work correctly
    'depends': [],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
