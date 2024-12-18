{
    'name': 'Pioneer Customer Customizations',
    'version': '18.0.1.0',
    'summary': 'Customizations for managing distributors and retailers.',
    'description': """
        Pioneer Customer Customizations
        =================================
        This module provides custom functionality for managing distributors and retailers.
        It is designed for training purposes and demonstrates how to extend Odoo's 
        capabilities in the sale and accounting modules.
    """,
    'category': 'Training',
    'author': 'Entrivis Tech Pvt. Ltd',
    'website': 'https://www.entrivistech.com',
    'depends': ['base', 'sale', 'accountant', 'stock'],
    'data': [
        'views/distributor_views.xml',
        'views/retailer_views.xml',
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
