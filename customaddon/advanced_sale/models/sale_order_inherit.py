from odoo import models, fields, api


class SaleOrderInherit(models.Model):
    _inherit = "sale.order"

    sale_order_discount_estimated = fields.Float(string="Discount Total",
                                                 compute="_compute_discount_total"
                                                 )

    @api.depends('partner_id.discount_percentage')
    def _compute_discount_total(self):
        for customer in self:
            if customer.partner_id.discount_percentage:
                customer.sale_order_discount_estimated = \
                    (customer.amount_untaxed * customer.partner_id.discount_percentage) / 100
            else:
                customer.sale_order_discount_estimated = 0

    def _amount_all(self):
        super(self._amount_all())
        amount_total = 0
        for customer in self:
            amount_total = customer.amount_total - customer.sale_order_discount_estimated
            customer.update({
                'amount_total': amount_total
            })
