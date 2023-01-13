from datetime import datetime
from odoo import models, fields, api
class InvoiceModel(models.Model):
    _name = 'menu_app.invoice_model'
    _description = 'Invoice Model'

    ref=fields.Integer(string="REF",readonly=True, default=lambda self: self._computeRef(), index=True)
    date=fields.Datetime(string="Date",readonly=True, default=datetime.now())
    base=fields.Float(string="Base", readonly=True)
    vat=fields.Selection(string="VAT",selection=[("0",'0'),("21",'21')], default="21")
    total=fields.Float(string="Total",readonly=True)
    lines=fields.One2many("menu_app.quantiti_model","invoice",string="Lines")
    client= fields.Char(string="Client:", required=True)
    state= fields.Selection(string="Status",selection=[('DR','Draft'),('CO','Confirmed')], default="DR")

    def _computeRef(self):
        if len(self.env["menu_app.invoice_model"].search([]))==0:
            return 1
        else:
            return (self.env["menu_app.invoice_model"].search([])[-1].id + 1)

    @api.onchange("vat","base","lines")
    def chageTotal(self):
        self.base=0
        for line in self.lines:
            self.base+=(line.foods.price*line.quantiti)
        self.total=self.base+(self.base/100*int(self.vat))

    def finalizar(self):
        self.ensure_one()
        self.state = "CO"
        return True