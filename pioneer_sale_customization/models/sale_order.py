from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _get_dynamic_size_columns(self):
        size_columns = []
        for rec in self.order_line:
            for attribute_line in rec.product_template_id.attribute_line_ids:
                if attribute_line.attribute_id.name.lower() == "size":
                    size_columns = [value.name for value in attribute_line.value_ids]
                    break
        return size_columns

    def pioneer_sale_customization(self):
        grouped_data = {}
        all_types = set()

        for rec in self.order_line:
            product = rec.product_id.name.split('(')[0].strip()
            size_type = rec.name.split('(')[-1].replace(')', '').strip()
            size, type_ = size_type.split(', ')
            all_types.add(type_)

            if product not in grouped_data:
                grouped_data[product] = {'product_name': product, 'price_subtotal': 0}

            if type_ not in grouped_data[product]:
                grouped_data[product][type_] = {}

            grouped_data[product][type_][size] = rec.product_uom_qty

        for product, data in grouped_data.items():
            for type_ in all_types:
                if type_ not in data:
                    data[type_] = {}
                if type_ + '_total_quantity' not in data:
                    data[type_ + '_total_quantity'] = 0
                if 'price_subtotal' not in data:
                    data['price_subtotal'] = 0

                sizes = data.get(type_, {})
                data[type_ + '_total_quantity'] = sum(sizes.values())

        prepared_data = []

        for product, data in grouped_data.items():
            for type_ in all_types:
                sizes = data.get(type_, {})
                sizes_sum = sum(sizes.values())
                prepared_data.append({
                    'product_name': data['product_name'],
                    'type': type_,
                    'sizes': sizes,
                    'total_quantity': data[type_ + '_total_quantity'],
                    'sizes_sum': sizes_sum,
                    'price_subtotal': data['price_subtotal']
                })
        return prepared_data




