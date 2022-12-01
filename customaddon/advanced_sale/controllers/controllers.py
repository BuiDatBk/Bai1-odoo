# -*- coding: utf-8 -*-
# from odoo import http


# class Customaddon/advancedSale(http.Controller):
#     @http.route('/customaddon/advanced_sale/customaddon/advanced_sale', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customaddon/advanced_sale/customaddon/advanced_sale/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('customaddon/advanced_sale.listing', {
#             'root': '/customaddon/advanced_sale/customaddon/advanced_sale',
#             'objects': http.request.env['customaddon/advanced_sale.customaddon/advanced_sale'].search([]),
#         })

#     @http.route('/customaddon/advanced_sale/customaddon/advanced_sale/objects/<model("customaddon/advanced_sale.customaddon/advanced_sale"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customaddon/advanced_sale.object', {
#             'object': obj
#         })
