# -*- coding: utf-8 -*-
{
    'name': "proyectoOdoo",

    'summary': """
        Proyecto final odoo""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'security/reglas_registro.xml',
        'reports/empresas_contratadoras_report.xml',
        'reports/empresas_contratadoras_report_view.xml',
        'data/tipo_pago_data.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
     'application':'True',

         'assets': {
        'web.assets_common': [
            'proyecto_odoo/static/src/scss/style1.scss',
        ]
    }
}
