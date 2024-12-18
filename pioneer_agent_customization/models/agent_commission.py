from odoo import api, fields, models, _
from datetime import datetime


class AgentCommission(models.Model):
    _name = 'agent.commission'
    _description = 'Agent Commission Details'

    date = fields.Date("Date", readonly=True)
    amount = fields.Float("Amount")
    percentage = fields.Float("Percentage")
    from_date = fields.Date(string="From Date", required=True)
    to_date = fields.Date(string="To Date", required=True)
    name = fields.Many2one('res.partner', 'Agent', domain=[('is_agent', '=', True)], required=True)
    state = fields.Selection([('unpaid', 'Unpaid'), ('paid', 'Paid')], default='unpaid', string='state')
    reference_no = fields.Char(string='Order Reference', required=True, readonly=True, default=lambda self: _('New'))
    invoice_id = fields.Many2one("account.move", "Invoice")
    invoice_ids = fields.Many2many('account.move', 'rel_agent_account_move', 'agent_id',
                                  'account_id', 'Invoices', compute="compute_invoice_ids", store=True)

    all_invoices = fields.Many2many('account.move', 'rel_agent_commission_account_move', 'agent_commission_id',
                                  'account_move_id', 'Invoices', compute="all_compute_invoice_ids", store=True)

    @api.model
    def create(self, vals_list):
        if vals_list.get('reference_no', _('New')) == _('New'):
            vals_list['reference_no'] = self.env['ir.sequence'].next_by_code(
                'agent.commission') or _('New')
        res = super(AgentCommission, self).create(vals_list)
        return res

    @api.depends('from_date', 'to_date')
    def compute_invoice_ids(self):
        for rec in self:
            if rec.from_date and rec.to_date:
                filtered_invoices = self.env['account.move'].search([
                    ('invoice_date', '>=', rec.from_date),
                    ('invoice_date', '<=', rec.to_date),
                    ('is_commission_generated', '=', False),
                    ('state', '=', 'posted'),
                    ('agent_id', '=', self.name.id),
                    ('payment_state', 'in', ['in_payment', 'paid'])
                ])
                rec.invoice_ids = filtered_invoices

    @api.depends('from_date', 'to_date')
    def all_compute_invoice_ids(self):
        for rec in self:
            if rec.from_date and rec.to_date:
                filtered_invoices = self.env['account.move'].search([
                    ('invoice_date', '>=', rec.from_date),
                    ('invoice_date', '<=', rec.to_date),
                    ('is_commission_generated', '=', True),
                    ('state', '=', 'posted'),
                    ('agent_id', '=', self.name.id),
                    ('payment_state', 'in', ['in_payment', 'paid'])
                ])
                rec.all_invoices = filtered_invoices


    def generate_agent_commission(self):
        for rec in self:
            if not rec.from_date or not rec.to_date:
                raise ValueError(_("From Date and To Date must be specified."))
            if rec.percentage <= 0 or rec.percentage > 100:
                raise ValueError(_("Commission percentage must be between 0 and 100."))
            percentage = rec.percentage / 100
            total_commission = sum(invoice.amount_total_in_currency_signed * percentage for invoice in rec.invoice_ids)
            rec.amount += total_commission
            rec.date = fields.Datetime.now()
            for invoice in rec.invoice_ids:
                invoice.is_commission_generated = True
            rec.compute_invoice_ids()

    def pay_agent_commission(self):
        self.state = 'paid'


