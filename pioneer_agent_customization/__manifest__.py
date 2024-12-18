{
    'name': 'Pioneer Agent Customizations',
    'version': '18.0',
    'category': 'Sales',
    'summary': 'Customizations for managing Pioneer agents within the sales process.',
    'depends': ['pioneer_customers_customization'],
    'description': """
        Pioneer Agent Customizations
        ============================
        This module provides custom features and enhancements tailored for managing Pioneer agents, streamlining their workflows,
         and improving sales process efficiency. Key features include:
        
        - Enhanced agent management
        - Improved sales tracking specific to agents
        - Custom fields and workflows for agents
        """,
    'author': 'Entrivis Tech Pvt. Ltd',
    'website': 'https://www.entrivistech.com',
    'data': [
        'data/ir_sequence.xml',
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
        'views/agent_views.xml',
        'views/sale_order_views.xml',
        'views/account_move_views.xml',
        'views/agent_commission_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
