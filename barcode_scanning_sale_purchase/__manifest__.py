# -*- coding: utf-8 -*-
{
    'name': 'Barcode Scanning Support For Sale and Purchase',
    'version': '18.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'This module will help you to use barcode scanner in sales '
               'and purchase.',
    'description': 'Barcode field is added to order lines where you can use '
                   'scanner to search product with their barcode.',
    'author': 'Entrivis Tech Pvt. Ltd',
    'company': 'Entrivis Tech Pvt. Ltd',
    'maintainer': 'Entrivis Tech Pvt. Ltd',
    'website': 'https://www.entrivistech.com',
    'depends': ['purchase', 'sale_management', 'stock'],
    'data': ['views/sale_order_line_views.xml',
             'views/purchase_order_line_views.xml',
             'views/stock_picking_views.xml',
             'views/account_move_views.xml'],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
