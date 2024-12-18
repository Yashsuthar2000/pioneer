{
    'name': 'Pioneer Product Customizations',
    'version': '18.0',
    'category': 'Sales',
    'summary': 'Enhancements and customizations for product management in Pioneer.',
    'description': """
        **Pioneer Product Customizations**  
        This module introduces advanced features and configurations for product management. 
        Key Features:  
        - Seamless integration with the default product module.  
        - Tailored options to enhance product-related workflows.  
        - Scalable and user-friendly design for sales operations.
    """,
    'depends': ['sale_management', 'purchase', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/row_material_views.xml',
        'views/season_views.xml',
        'views/brand_views.xml',
        'report/product_label_reports.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
