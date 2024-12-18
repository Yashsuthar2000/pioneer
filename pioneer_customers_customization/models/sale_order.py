from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'sale details'

    distributor_id = fields.Many2one(comodel_name='res.partner', string="Distributor")

    @api.onchange('partner_id')
    def onchange_distributor(self):
        for rec in self:
            rec.distributor_id = rec.partner_id.parent_id.id

    @api.depends('distributor_id', 'partner_id')
    def _compute_partner_invoice_id(self):
        res = super(SaleOrder, self)._compute_partner_invoice_id()
        for order in self:
            if order.distributor_id:
                order.partner_invoice_id = order.distributor_id.id
        return res

    @api.depends('distributor_id', 'partner_id')
    def _compute_partner_shipping_id(self):
        res = super(SaleOrder, self)._compute_partner_shipping_id()
        for order in self:
            if order.distributor_id:
                order.partner_shipping_id = order.distributor_id.id
        return res


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    _description = 'sale line details'

    @api.onchange('product_uom_qty')
    def _apply_dynamic_tax(self):
        tax_5_percent = self.env['account.tax'].search([('name', '=', '5% GST')], limit=1)
        tax_12_percent = self.env['account.tax'].search([('name', '=', '12% GST S')], limit=1)
        if self.product_uom_qty < 1000:
            self.tax_id = [(6, 0, [tax_5_percent.id])] if tax_5_percent else False
        else:
            self.tax_id = [(6, 0, [tax_12_percent.id])] if tax_12_percent else False
