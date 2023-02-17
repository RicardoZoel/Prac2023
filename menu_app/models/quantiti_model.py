from odoo import models, fields, api
class QuantitiModel(models.Model):
    _name = 'menu_app.quantiti_model'
    _description = 'Quantiti Model'

    quantiti = fields.Integer(string="Quantity of product", required=True, default=1)
    foods = fields.Many2one("menu_app.foods_model", required=True, string="Products")
    orders = fields.Many2one("menu_app.orders_model",string="Order")
    invoice = fields.Many2one("menu_app.invoice_model",string="Invoice")

    destination= fields.Char(string="Destination", compute="_compute_destination", store=True, readonly=True)
    ubicacion= fields.Char(string="Location", compute="_compute_ubicacion", store=True, readonly=True)

    state = fields.Selection(string="Status",selection=[('PE','Pending'),('RD','Ready'),('FI','finish')], default="PE")


    """ Botones """
    def ready(self):
        self.ensure_one()
        if self.state == "RD":
                self.state = "FI"
        elif self.state == "PE":
                self.state = "RD"
        return True

    def readyBackWaiter(self):
        if self.state == "RD":
                self.state = "FI"
        return {
               'name': ('Quantity Form Waiter'),
               'view_type': 'form',
               'view_mode': 'tree,form',
               'res_model': 'menu_app.quantiti_model',
               'domain': [('state', '=',  'RD')],
               'view_id': False,
               'views':[(self.env.ref('menu_app.quantiti_list').id,'tree'),(self.env.ref('menu_app.quantiti_model_form_inherit_camarero').id,'form')],
               'type': 'ir.actions.act_window',
          }
    def readyBackBarman(self):
        
        if self.state == "PE":
                self.state = "RD"
        return {
               'name': ('Quantity Form Barman'),
               'view_type': 'form',
               'view_mode': 'tree,form',
               'res_model': 'menu_app.quantiti_model',
               'domain': [('destination', '=',  'BARRA'),('state', '=',  'PE')],
               'view_id': False,
               'type': 'ir.actions.act_window',
               'views':[(self.env.ref('menu_app.quantiti_list').id,'tree'),(self.env.ref('menu_app.quantiti_model_form_inherit_barman').id,'form')],
          }
    def readyBackCooker(self):
        
        if self.state == "PE":
                self.state = "RD"
        return {
               'name': ('Quantity Form Cooker'),
               'view_type': 'form',
               'view_mode': 'tree,form',
               'res_model': 'menu_app.quantiti_model',
               'domain': [('destination', '=',  'COCINA'),('state', '=',  'PE')],
               'view_id': False,
               'type': 'ir.actions.act_window',
               'views':[(self.env.ref('menu_app.quantiti_list').id,'tree'),(self.env.ref('menu_app.quantiti_model_form_inherit_cocinero').id,'form')],
          }
    """ ======================== """
    @api.depends('orders','orders.table')
    def _compute_ubicacion(self):
        for algo in self:
            if len(algo.orders)==0:
                algo.ubicacion="BARRA"
            else:
                algo.ubicacion="MESA "+str(algo.orders.table)
    """ ======================== """
    @api.depends('foods','foods.preparation')
    def _compute_destination(self):
        for algo in self:
            if algo.foods.preparation=='BR':
                algo.destination="BARRA"
            else:
                algo.destination="COCINA"