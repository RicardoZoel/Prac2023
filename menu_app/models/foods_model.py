from odoo import models, fields, api
class FoodsModel(models.Model):
    _name = 'menu_app.foods_model'
    _description = 'Foods Model'

    name = fields.Char(string="Food Name", required=True)
    currency_id=fields.Many2one("res.currency", string="Currency", default=lambda self:self.env.user.company_id.currency_id)
    price = fields.Monetary(string="Food price", required=True)
    category = fields.Many2one("menu_app.category_model", "Category")
    ingridients = fields.Many2many("menu_app.ingridients_model",relation="menu_app_ingridients_model2foods_model", required=True, string="Ingridients")
    foods = fields.Many2many("menu_app.quantiti_model",relation="menu_app_foods_model2quantiti_model",readonly=True)
    image=fields.Image(string="Image of food")
    description= fields.Html(string="Description")