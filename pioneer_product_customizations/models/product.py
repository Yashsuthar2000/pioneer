from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.template'
    _description = 'Product Inherit'

    season_id = fields.Many2one("season.master", string="Season")
    brand_id = fields.Many2one("brand.master", string="Brand")
