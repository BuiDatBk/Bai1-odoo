# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _


class ResPartnerInherit(models.Model):
    _inherit = "res.partner"

    customer_discount_code = fields.Text(string="Discount Code", groups="advanced_sale.group_advanced_sale")
    # , groups="advanced_sale.group_advanced_sale"
    discount_percentage = fields.Integer("Discount Percentage", compute="_discount_percentage")
    has_valid_code = fields.Boolean(compute="_compute_valid_code", store=True)

    @api.depends("customer_discount_code")
    def _compute_valid_code(self):
        for record in self:
            record.has_valid_code = record._is_valid_discount_code()

    def _is_valid_discount_code(self):
        self.ensure_one()
        if self.customer_discount_code :
            char_list = self.customer_discount_code.split("_")
            if len(char_list) == 2 and char_list[0] == "VIP":
                try:
                    discount_amount = int(char_list[1])
                    if 1 < discount_amount <= 100:
                        return True
                    else:
                        return False
                except ValueError:
                    return False
        else:
            return False
    @api.depends("customer_discount_code")
    def _discount_percentage(self):
        for rec in self:
            if rec._is_valid_discount_code():
                rec.discount_percentage = int(rec.customer_discount_code.split("_")[1])
            else:
                rec.discount_percentage = False
