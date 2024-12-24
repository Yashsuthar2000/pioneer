
{ 'name': 'Pioneer invoice report',
    'version': '18.0',
    'category': 'Sales',
    'summary': 'Customizations for managing Pioneer agents within the sales process.',
    'depends': ['account','sale','product'],
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
        'report/customization_invoice_report.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}