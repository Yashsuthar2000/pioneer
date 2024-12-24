{
    'name': 'Pioneer Delivery Assignment',
    'version': '18.0',
    'summary': 'Module for assigning deliveries efficiently',
    'description': """
        This module enables users to assign deliveries to drivers or teams 
        efficiently, track assignment statuses, and manage logistics workflows 
        effectively.
    """,
    'author': 'Entrivis Tech Pvt. Ltd',
    'website': 'https://www.entrivistech.com',
    'license': 'LGPL-3',
    'category': 'Logistics/Delivery',
    'depends': ['base', 'sale_management', 'stock', 'delivery', 'pioneer_product_customizations', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/delivery_assignment_view.xml',
        'views/pioneer_dashboard_menus.xml',
    ],
    'assets': {
        'web.assets_backend': {
            'pioneer_delivery_assignment/static/src/js/pioneer_delivery_dashboard.js',
            'pioneer_delivery_assignment/static/src/xml/pioneer_dashboard_template_views.xml',
        }
    },

    'installable': True,
    'application': True,
    'auto_install': False,
}
