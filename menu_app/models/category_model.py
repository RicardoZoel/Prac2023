from odoo import models, fields, api
class CategoryModel(models.Model):
    _name = 'menu_app.category_model'
    _description = 'Category Model'

    name = fields.Char(string="Category Name", required=True)
    foods = fields.One2many("menu_app.foods_model", inverse_name="category",string="Foods")