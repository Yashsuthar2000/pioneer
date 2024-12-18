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
                grouped_data[product] = {'product_name': product}

            if type_ not in grouped_data[product]:
                grouped_data[product][type_] = {'sizes': {}, 'price_subtotal': 0}

            # count quantity for each size and type
            grouped_data[product][type_]['sizes'][size] = rec.product_uom_qty
            # count subtotal for each product and type
            grouped_data[product][type_]['price_subtotal'] += rec.price_unit * rec.product_uom_qty

        prepared_data = []

        for product, data in grouped_data.items():
            for type_ in all_types:
                sizes = data[type_]['sizes']
                sizes_sum = sum(sizes.values())
                price_subtotal_type = data[type_]['price_subtotal']
                prepared_data.append({
                    'product_name': data['product_name'],
                    'type': type_,
                    'sizes': sizes,
                    'total_quantity': sizes_sum,
                    'sizes_sum': sizes_sum,
                    'price_subtotal_type': price_subtotal_type
                })

        return prepared_data




