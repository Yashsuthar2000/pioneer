from odoo import api, fields, models

class StockMove(models.Model):
    _inherit = 'stock.move'

    delivery_assignment_id = fields.Many2one("delivery.assignment", 'Delivery Assignment')
