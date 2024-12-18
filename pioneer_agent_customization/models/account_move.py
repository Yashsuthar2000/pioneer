from odoo import api, fields, models, _
from datetime import datetime


class AccountMove(models.Model):
    _inherit = 'account.move'

    agent_id = fields.Many2one(comodel_name='res.partner', domain=[('is_agent', '=', True)], readonly=True,
                               string="Agent")
    is_commission_generated = fields.Boolean(string="Commission Generated", default=False)