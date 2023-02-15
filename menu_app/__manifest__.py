# -*- coding: utf-8 -*-
{
    'name': "menu_app",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/menu_security.xml',
        'security/ir.model.access.csv',
        'views/orders_views.xml',
        'views/foods_views.xml',
        'views/ingridients_views.xml',
        'views/category_views.xml',
        'views/invoice_views.xml',
        'views/quantiti_views.xml',
        'views/menu.xml',
        'report/report_invoice.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}
