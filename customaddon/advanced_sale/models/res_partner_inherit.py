# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartnerInherit(models.Model):
    _inherit = "res.partner"
    _description = ""

    customer_discount_code = fields.Text('Discount Code')
