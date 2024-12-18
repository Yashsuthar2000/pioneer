{
    'name': 'Pioneer Sales Customizations',
    'version': '18.0.1.0',
    'category': 'Sales/Customization',
    'author': 'Entrivis Tech Pvt. Ltd.',
    'website': 'https://www.entrivistech.com',
    'summary': 'Enhancements and custom features for sales operations in Odoo.',
    'description': """
        Pioneer Sales Customizations
        =============================
        This module provides customizations and additional features to enhance the sales workflow in Odoo, tailored for Pioneer Enterprises. Key features include:
        - Custom product labels
        - Enhanced report designs
        - Additional fields and logic in the sales process 
        - Entrivis Tech Pvt. Ltd is committed to delivering robust Odoo solutions for your business needs.
        """,
    'depends': ['base', 'sale'],
    'data': [
        "report/ir_actions_report_templates.xml",
        "views/product_attribute_views.xml"
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
