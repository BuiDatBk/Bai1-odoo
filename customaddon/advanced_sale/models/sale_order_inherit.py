from odoo import models, fields, api


class SaleOrderInherit(models.Model):
    _inherit = "sale.order"

    sale_order_discount_estimated = fields.Monetary(string="Discount Total",
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

    @api.depends('order_line.price_total')
    def _amount_all(self):
        """
        Compute the total amounts of the SO.
        """
        for order in self:
            amount_untaxed = amount_tax = discount_no_warranty = 0.0
            for line in order.order_line:
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax

            discount_no_warranty = order.sale_order_discount_estimated

            order.update({
                'amount_untaxed': amount_untaxed,
                'amount_tax': amount_tax,
                'amount_total': amount_untaxed + amount_tax - discount_no_warranty,
            })

    # @api.depends('order_line.price_total')
    # def _amount_all(self):
    #     super(self._amount_all())
    #     amount_total = 0
    #     for customer in self:
    #         amount_total = customer.amount_total - customer.sale_order_discount_estimated
    #         customer.update({
    #             'amount_total': amount_total
    #         })
