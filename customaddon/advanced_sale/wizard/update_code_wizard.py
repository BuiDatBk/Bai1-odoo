from odoo import fields, models, api


class UpdateCodeWizard(models.TransientModel):
    _name = 'update.code.wizard'

    discount_code = fields.Char(string="Enter Discount Code")
    customer_ids = fields.Many2many('res.partner', string="Customers")

    def add_discount_code(self):
        for customer in self.customer_ids:
            customer.customer_discount_code = self.discount_code

