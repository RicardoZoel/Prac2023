from datetime import datetime
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class InvoiceModel(models.Model):
    _name = 'menu_app.invoice_model'
    _description = 'Invoice Model'
    _rec_name='ref'

    ref=fields.Integer(string="REF",readonly=True, default=lambda self: self._computeRef(), index=True)
    date=fields.Datetime(string="Date",readonly=True, default=datetime.now())
    base=fields.Float(string="Base", compute="chageTotal",readonly=True)
    vat=fields.Selection(string="VAT",selection=[("0",'0'),("4",'4'),("10",'10'),("21",'21')], default="10")
    total=fields.Float(string="Total",readonly=True)
    lines=fields.One2many("menu_app.quantiti_model","invoice",string="Lines")
    client= fields.Char(string="Client:", required=True)
    state= fields.Selection(string="Status",selection=[('DR','Draft'),('CO','Confirmed')], default="DR")

    def _computeRef(self):
        if len(self.env["menu_app.invoice_model"].search([]))==0:
            return 1
        else:
            return (self.env["menu_app.invoice_model"].search([])[-1].id + 1)

    @api.depends("vat","base","lines")
    def chageTotal(self):
        for aa in self:
            aa.base=0
            for line in aa.lines:
                aa.base+=(line.foods.price*line.quantiti)
            aa.total=aa.base+(aa.base/100*int(aa.vat))

    def finalizar(self):
        self.ensure_one()
        for a in self.lines:
            if a.state!="FI":
                raise ValidationError("There are products to deliver !!!!")
        self.state = "CO"
        for line in self.lines:
            if line.orders.state=="PE":
                line.orders.state=="FI"
        return True

    def print_report(self):
        return self.env.ref('menu_app.report_invoice').report_action(self)
    