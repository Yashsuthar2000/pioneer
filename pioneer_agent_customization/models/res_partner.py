from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_agent = fields.Boolean("Is Agent")
    agent_id = fields.Many2one('res.partner', string="Agent")
    retailer_type = fields.Selection(selection_add=[('agent', 'Agent')])