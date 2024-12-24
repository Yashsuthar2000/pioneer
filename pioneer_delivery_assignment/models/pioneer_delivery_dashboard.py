from odoo import api, fields, models
from bs4 import BeautifulSoup
from odoo.exceptions import UserError


class PioneerDeliveryDashboard(models.Model):
    _name = 'pioneer.delivery.dashboard'

    order_id = fields.Many2one("stock.picking", "Delivery Order")

    @api.model
    def get_dashboard_data(self, record_id=None):
        delivery_assignment = self.env['delivery.assignment'].search([], limit=1)
        grid_data = self.convert_html_to_dict(delivery_assignment.grid_data)
        print("\n\n\n\n\n grid_data::::::::::::::::::::::::::::::::::::::", grid_data)
        delivery_order_data = self.get_delivery_order_details()
        return {
            "grid_data": grid_data,
            "delivery_order_data": delivery_order_data,
        }

    def get_delivery_order_details(self):
        delivery_order_line_rec = self.env['stock.move'].search([], limit=10)
        print("delivery_order_line_rec::::::::::::::::::::::::::", delivery_order_line_rec)
        delivery_order_line_data = []
        for line in delivery_order_line_rec:
            delivery_order_line_data.append({
                'barcode_scan': line.barcode_scan or '',
                'customer': line.picking_id.partner_id.name,
                'origin': line.origin or '',
                'product_id': line.product_id.id if line.product_id else None,
                'product_uom_qty': line.product_uom_qty or 0,
                'state': line.state,
                'quantity': line.quantity or 0,
            })
        print("\n\n\n\n Final delivery_order_line_data:::::::::::", delivery_order_line_data)
        return delivery_order_line_data

    def convert_html_to_dict(self, html_data):
        soup = BeautifulSoup(html_data, "html.parser")
        table = soup.find("table")

        if not table:
            raise UserError("No table found in the provided HTML data.")

        headers = [th.text.strip() for th in table.find_all("th")]

        rows = []
        for tr in table.find_all("tr")[1:]:
            row = [td.text.strip() for td in tr.find_all("td")]
            rows.append(row)

        data_dict = {}
        for row in rows:
            row_dict = dict(zip(headers, row))
            data_dict[row[0]] = row_dict

        return data_dict
