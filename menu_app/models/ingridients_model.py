from odoo import models, fields, api
class IngridientsModel(models.Model):
    _name = 'menu_app.ingridients_model'
    _description = 'Ingridients Model'

    name = fields.Char(string="Ingridient Name", required=True)
    allergens = fields.Boolean(string="allergens?", default=False, required=True)
    foods = fields.Many2many("menu_app.foods_model",relation="menu_app_ingridients_model2foods_model",string="Foods")
    description= fields.Html(string="Description")