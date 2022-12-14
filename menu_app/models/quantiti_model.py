from odoo import models, fields, api
class QuantitiModel(models.Model):
    _name = 'menu_app.quantiti_model'
    _description = 'Quantiti Model'

    quantiti = fields.Integer(string="Quantiti of product", required=True, default=1)
    foods = fields.Many2one("menu_app.foods_model", required=True, string="Foods")
    orders = fields.Many2one("menu_app.orders_model")