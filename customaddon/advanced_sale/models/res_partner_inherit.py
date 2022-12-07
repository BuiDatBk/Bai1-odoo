# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _


class ResPartnerInherit(models.Model):
    _inherit = "res.partner"
    _description = ""

    customer_discount_code = fields.Text('Discount Code', groups="advanced_sale.group_advanced_sale")
    discount_percentage = fields.Integer("Discount Percentage", compute="_discount_percentage")

    def _is_valid_discount_code(self):
        self.ensure_one()
        char_list = self.customer_discount_code.split("_")
        if len(char_list) == 2 and char_list[0] == "VIP":
            try:
                discount_amount = int(char_list[1])
                if 1 < discount_amount < 100:
                    return True
                else:
                    return False
            except ValueError:
                return False

    @api.depends("customer_discount_code")
    def _discount_percentage(self):
        for rec in self:
            if rec._is_valid_discount_code():
                rec.discount_percentage = int(rec.customer_discount_code.split("_")[1])
            else:
                rec.discount_percentage = False
