from odoo import api, fields, models, _


class PioneerInvoice(models.Model):
    _inherit = 'account.move'

    def _get_dynamic_invoice_size_columns(self):
        size_columns = []
        for rec in self.invoice_line_ids:
            for attribute_line in rec.product_id.attribute_line_ids:
                if attribute_line.attribute_id.name.lower() == "size":
                    size_columns = [value.name for value in attribute_line.value_ids]
                    break
        return size_columns

    def pioneer_invoice_customization(self):
        grouped_data = {}
        all_types = set()
        column_totals = {}
        hsn_code = ()
        hsn_code_product = []
        
       
        
        

        for size in self._get_dynamic_invoice_size_columns():
            column_totals[size] = 0
            

        for rec in self.invoice_line_ids:
            product = rec.product_id.name.split('(')[0].strip()
            size_type = rec.name.split('(')[-1].replace(')', '').strip()
            size, type_ = size_type.split(', ')
            all_types.add(type_)
            hsn_code_product = self.line_ids.mapped('l10n_in_hsn_code')
            hsn_code = hsn_code_product[0]
          

            if product not in grouped_data:
                grouped_data[product] = {'product_name': product}

            if type_ not in grouped_data[product]:
                grouped_data[product][type_] = {
                    'sizes': {},
                    'price_subtotal': 0,
                    'taxes_id': rec.tax_ids,
                    'lst_price': rec.product_id.lst_price,
                    'rate': rec.price_unit,
                    'disc': rec.discount
                }
            if type_ not in grouped_data[product]:
                grouped_data[product][type_] = {'sizes': {}, 'price_subtotal': 0}

            # count quantity for each size and type
            grouped_data[product][type_]['sizes'][size] = rec.quantity
            # count subtotal for each product and type
            column_totals[size] += rec.quantity

            grouped_data[product][type_]['price_subtotal'] += rec.price_unit * rec.quantity

            

        prepared_data = []
        
        
        for product, data in grouped_data.items():
           

            for type_ in all_types:
                if type_ in data:  # Ensure the type exists in the data
                    sizes = data[type_].get('sizes', {})
                    sizes_sum = sum(sizes.values())
                    price_subtotal_type = data[type_].get('price_subtotal', 0)
                    
                    prepared_data.append({
                        'hsn_product_code':hsn_code,
                        'product_name': data.get('product_name', ''),
                        'taxes_id': data[type_].get('taxes_id', ''),
                        'lst_price': data[type_].get('lst_price', 0),
                        'type': type_,
                        'sizes': sizes,
                        'rate': data[type_].get('rate', 0),
                        'disc': data[type_].get('disc', 0),
                        'total_quantity': sizes_sum,
                        'sizes_sum': sizes_sum,
                        'price_subtotal_type': price_subtotal_type
                    })

        # Ensure prepared_data contains all records
        return prepared_data, column_totals

        