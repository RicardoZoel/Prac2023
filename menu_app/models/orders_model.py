from odoo import models, fields, api
from datetime import datetime
class OrdersModel(models.Model):
    _name = 'menu_app.orders_model'
    _description = 'Orders Model'
    _sql_constraints = [ ('orders_unique_ref','UNIQUE (table,table_active)','table_active and table must be unique!!'), ]

    table = fields.Integer(string="Table", required=True, index=True)
    customer = fields.Char(string="Client", required=True)
    """waiter=camarero"""
    
    waiter = fields.Char(string="Waiter", required=True)
    currency_id=fields.Many2one("res.currency", string="Currency", default=lambda self:self.env.user.company_id.currency_id)
    total = fields.Monetary(string="Price", readonly=True, default=0)
    description= fields.Html(string="Description")
    order_active=fields.Boolean(default=True, readonly=True)
    table_active=fields.Boolean(default=True, readonly=True)
    quantiti=fields.One2many("menu_app.quantiti_model","orders",string="Products")
    state = fields.Selection(string="Status",selection=[('AC','Active'),('PE','Pending'),('FI','finish')], default="ACS")
    #Cambiar los estados entre: 
    #   - Activo: mesa en uso y pidiendo 
    #   - Pendiente: mesa finalizada y pendiente de facturación 
    #   - Finalizada: mesa finalizada y se han facturado todos los pagos
    date = fields.Datetime(string="Date finish",help="Date finish",readonly=True)

    def finalizar(self):
        self.ensure_one()
        self.order_active = False
        self.table_active = False
        if self.state == "AC":
               self.state = "PE"
               self.date=datetime.now()
        return True

    @api.onchange("quantiti")
    def chageTotal(self):
        self.total=0
        for i in self.quantiti:
            self.total+=(i.foods.price*i.quantiti)