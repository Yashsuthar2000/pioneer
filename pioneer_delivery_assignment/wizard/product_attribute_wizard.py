from odoo import models, fields, api

class ProductSizeWizard(models.TransientModel):
    _name = 'product.size.wizard'
    _description = 'Product Size Wizard'

    product_id = fields.Many2one('product.product', string="Product", required=True)
    table_lines = fields.One2many('product.size.line', 'wizard_id', string="Size Table")
    size_columns = fields.Many2many('product.attribute.value', string="Size Attributes", compute="_compute_size_columns")

    @api.depends('product_id')
    def _compute_size_columns(self):
        """
        Fetch all size-related attribute values and dynamically set the columns.
        """
        for wizard in self:
            # Fetch all size attributes
            size_attribute = self.env['product.attribute'].search([('name', 'ilike', 'size')], limit=1)
            if size_attribute:
                wizard.size_columns = size_attribute.value_ids

    @api.onchange('product_id')
    def _onchange_product_id(self):
        """
        Populate rows for the table based on the selected product.
        """
        if self.product_id:
            self.table_lines = [(5, 0, 0)]  # Clear previous lines

            # Populate rows with size-related attributes
            for size in self.size_columns:
                self.table_lines = [(0, 0, {
                    'size_id': size.id,
                    'product_name': self.product_id.name,
                })]

class ProductSizeLine(models.TransientModel):
    _name = 'product.size.line'
    _description = 'Product Size Line'

    wizard_id = fields.Many2one('product.size.wizard', string="Wizard")
    product_name = fields.Char(string="Product Name")
    size_id = fields.Many2one('product.attribute.value', string="Size")
