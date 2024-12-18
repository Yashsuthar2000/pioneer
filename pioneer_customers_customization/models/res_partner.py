from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    company_type = fields.Selection([('person', 'Retailer'), ('company', 'Distributor')], string="company Type",
                                    default="person")

    type = fields.Selection(
        selection_add=[('delivery', 'Retailer Address')],
        help="- Contact: Use this to organize the contact details of employees of a given company (e.g. CEO, CFO, ...).\n"
             "- Invoice Address : Preferred address for all invoices. Selected by default when you invoice an order that belongs to this company.\n"
             "- Delivery Address : Preferred address for all deliveries. Selected by default when you deliver an order that belongs to this company.\n"
             "- Private: Private addresses are only visible by authorized users and contain sensitive data (employee home addresses, ...).\n"
             "- Other: Other address for the company (e.g. subsidiary, ...)\n"
             "- Retailer Address: A new address type for retailer-specific deliveries or contacts.")

    retailer_type = fields.Selection([('distributor', 'Distributor'), ('direct', 'Direct')], string="Retailer Type",
                                    default="direct")


