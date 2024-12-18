from odoo import models, fields


class BrandMaster(models.Model):
    _name = 'brand.master'
    _description = 'Brand Master'

    name = fields.Char(string='Brand Name', required=True, help="Name of the Brand, e.g., PIONEER")
    code = fields.Char(string='Brand Code', required=True, help="Unique code for the Brand, e.g., PIO")
