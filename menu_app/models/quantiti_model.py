from odoo import models, fields, api
class QuantitiModel(models.Model):
    _name = 'menu_app.quantiti_model'
    _description = 'Quantiti Model'

    quantiti = fields.Integer(string="Quantity of product", required=True, default=1)
    foods = fields.Many2one("menu_app.foods_model", required=True, string="Products")
    orders = fields.Many2one("menu_app.orders_model",string="Order")
    invoice = fields.Many2one("menu_app.invoice_model",string="Invoice")

    ubicacion= fields.Char(string="Location", compute="_compute_ubicacion", store=True, onlyread=True)


    @api.depends('orders','orders.table')
    def _compute_ubicacion(self):
        for algo in self:
            if len(algo.orders)==0:
                algo.ubicacion="BARRA"
            else:
                algo.ubicacion="MESA "+str(algo.orders.table)