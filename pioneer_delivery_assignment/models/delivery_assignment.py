from odoo import models, fields, api
from odoo import http


class DeliveryAssignment(models.Model):
    _name = 'delivery.assignment'
    _description = 'Delivery Assignment'
    _rec_name = 'product_id'

    product_id = fields.Many2one(comodel_name="product.template", string="Design", required=True)
    product_tmpl_id = fields.Many2one(comodel_name="product.product", string="Variant", required=True)
    season_id = fields.Many2one(comodel_name="season.master", string="Season")
    brand_id = fields.Many2one(comodel_name="brand.master", string="Brand")
    date_from = fields.Date(string="Order From", required=True)
    date_to = fields.Date(string="Order To", required=True)
    style = fields.Many2one(comodel_name="product.attribute.value", domain=[('attribute_id.name', '=', 'style')], string="Style")
    grid_data = fields.Html(string="Grid Data", compute="_compute_grid_data")
    move_line_ids = fields.One2many('stock.move', 'delivery_assignment_id', string="Stock Moves")

    def delivery_assignment_grid(self):
        return {
            'type': 'ir.actions.client',
            'name': 'Delivery Dashboard',
            'tag': 'delivery_dashboard',
            'target': 'current',
        }

    @api.onchange('product_id')
    def _onchange_product_id(self):
        """
        Reset the product variant (product_tmpl_id) when the product is changed.
        """
        for rec in self:
            rec.product_tmpl_id = False

    @api.onchange('product_tmpl_id', 'date_from', 'date_to')
    def _onchange_stock_move_lines(self):
        """
        Update stock move lines based on the selected product, date range, and stock move criteria.
        """
        for rec in self:
            if rec.product_tmpl_id and rec.date_from and rec.date_to:
                filtered_lines = self.env['stock.move'].search([
                    ('product_id', '=', rec.product_tmpl_id.id),
                    ('sale_line_id.order_id.date_order', '>=', rec.date_from),
                    ('sale_line_id.order_id.date_order', '<=', rec.date_to),
                    ('picking_id.state', 'not in', ['done', 'cancel'])
                ])
                rec.move_line_ids = filtered_lines
            else:
                rec.move_line_ids = False

    @api.depends('product_id', 'style', 'move_line_ids',
                 'product_id.valid_product_template_attribute_line_ids',
                 'product_id.valid_product_template_attribute_line_ids.value_ids')
    def _compute_grid_data(self):
        """
        Compute grid data for the selected product and style, displaying available quantities in a table format.
        """
        for record in self:
            if not record.product_id:
                record.grid_data = '<p>No product selected.</p>'
                continue

            filtered_variants = self.env['product.product'].search([
                ('product_tmpl_id', '=', record.product_id.id),
                ('product_template_variant_value_ids.attribute_id.name', '=', 'style'),
                ('product_template_variant_value_ids.name', '=', record.style.name)
            ])

            qty_available_list = [variant.qty_available for variant in filtered_variants]
            assigned_qty_list = [getattr(variant, 'quantity', 0) for variant in self.move_line_ids]
            remaining_qty_list = [available - assigned for available, assigned in
                                  zip(qty_available_list, assigned_qty_list)]
            attribute_names = [
                value.name
                for line in record.product_id.valid_product_template_attribute_line_ids
                if line.attribute_id.name == 'size'
                for value in line.value_ids
            ]

            rows = [
                {'name': 'Available Quantity', 'data': qty_available_list},
                {'name': 'Assigned Quantity', 'data': assigned_qty_list},
                {'name': 'Remaining Quantity', 'data': remaining_qty_list},
            ]

            inline_css = """style="border-collapse: collapse; width: 100%; text-align: center; font-size: 14px;" """
            th_css = "style='border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;'"
            td_css = "style='border: 1px solid #ddd; padding: 8px;'"

            html = f'<table {inline_css}>'
            html += '<tr>' + ''.join(f'<th {th_css}>{attr}</th>' for attr in ['Description'] + attribute_names) + '</tr>'
            for row in rows:
                html += f"<tr><td {td_css}>{row['name']}</td>"
                html += ''.join(f"<td {td_css}>{value}</td>" for value in row['data'])
                html += '</tr>'
            html += '</table>'

            record.grid_data = html
