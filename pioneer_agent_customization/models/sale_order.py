from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'sale details'

    agent_id = fields.Many2one(comodel_name='res.partner', domain=[('is_agent', '=', True)], string="Agent")

    # def _action_confirm(self):
    #     result = super(SaleOrder, self)._action_confirm()
    #     for order in self:
    #         agent_id = order.agent_id.id
    #         order.picking_ids.write({'agent_id': agent_id})
    #     return result


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = 'sale.advance.payment.inv'
    _description = 'sale advance payment inv details'

    def _create_invoices(self, sale_orders):
        invoices = super(SaleAdvancePaymentInv, self)._create_invoices(sale_orders)
        agent_id = sale_orders.agent_id.id
        invoices.write({'agent_id': agent_id})
        return invoices
