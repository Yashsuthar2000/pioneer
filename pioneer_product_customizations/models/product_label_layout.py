from odoo import api, fields, models



class ProductLabelLayout(models.TransientModel):
    _inherit = 'product.label.layout'
    _description = 'Choose the sheet layout to print the labels'

    print_format = fields.Selection(selection_add=[('custom', 'Pioneer Label')], ondelete={'custom': 'set default'}, default='custom')

    def _prepare_report_data(self):
        xml_id, data = super(ProductLabelLayout, self)._prepare_report_data()
        if self.print_format == 'custom':
            xml_id = 'pioneer_product_customizations.report_product_template_label_custom'
            product_template_id = next(iter(data.get('quantity_by_product', {})), None)
            quantity = data['quantity_by_product'].get(product_template_id)
            data.update({
                'product_template_id': product_template_id,
                'quantity': quantity,
            })
        return xml_id, data
