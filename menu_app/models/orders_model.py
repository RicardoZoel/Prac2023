from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError

class OrdersModel(models.Model):
    _name = 'menu_app.orders_model'
    _description = 'Orders Model'
    _sql_constraints = [('orders_unique_ref','UNIQUE (table)','active and table must be unique!!')]

    table = fields.Integer(string="Table", required=True, index=True)
    customer = fields.Char(string="Client", required=True, default="Client")
    """waiter=camarero"""
    #waiter automatico al usuario registrado
    waiter = fields.Char(string="Waiter", required=True, default=lambda self: self.env.user.name)
    currency_id=fields.Many2one("res.currency", string="Currency", default=lambda self:self.env.user.company_id.currency_id)
    total = fields.Monetary(string="Price", readonly=True, default=0)
    description= fields.Html(string="Description")
    order_active=fields.Boolean(default=True)
    active=fields.Boolean(default=True)
    quantiti=fields.One2many("menu_app.quantiti_model","orders",string="Products")
    state = fields.Selection(string="Status",selection=[('AC','Active'),('PE','Pending'),('FI','finish')], default="AC")
    #Cambiar los estados entre: 
    #   - Activo: mesa en uso y pidiendo / danger verde
    #   - Pendiente: mesa finalizada y pendiente de facturación / danger amarillo
    #   - Finalizada: mesa finalizada y se han facturado todos los pagos / danger gris
    date = fields.Datetime(string="Date finish",help="Date finish",readonly=True)
    orders_pending=fields.Boolean(default=True, invisible=True, compute="changeStatus", store=True)
    @api.constrains("table")
    def checkTabel(self):
        if self.table==0:
            raise ValidationError("The table cannot be 0 !!!!")
    
    @api.constrains("table","active")
    def noRepeat(self):
        for a in self:
            for b in self:
                if a.table == b.table and a.id != b.id:
                    if a.active == True:
                        raise ValidationError("The cannot be 2 active tables with the same numbers")
    def finalizar(self):
        self.ensure_one()
        for a in self.quantiti:
            if a.state!="FI":
                raise ValidationError("There are products to deliver !!!!")
        self.order_active = False
        if self.state == "AC":
               self.state = "PE"
               self.date=datetime.now()
        invoice = {
                'client': self.customer,
                'lines': self.quantiti,
            }
        self.env['menu_app.invoice_model'].create(invoice)
        return True

    @api.onchange("quantiti")
    def chageTotal(self):
        self.total=0
        for i in self.quantiti:
            self.total+=(i.foods.price*i.quantiti)

    @api.depends("quantiti","quantiti.state")
    def changeStatus(self):
        for i in self.quantiti:
            if i.state != 'FI':
                self.orders_pending=True
                return True
        self.orders_pending=False
        