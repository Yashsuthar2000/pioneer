from odoo import api, fields, models


class ProductAttribute(models.Model):
    _inherit = 'product.attribute'

    is_size = fields.Boolean("Is Size")
    is_style = fields.Boolean("Is Style")
