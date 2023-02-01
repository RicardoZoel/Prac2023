from odoo import models, fields, api
class CategoryModel(models.Model):
    _name = 'menu_app.category_model'
    _rec_name='complete_name'
    _description = 'Category Model'

    name = fields.Char(string="Category Name", required=True)
    complete_name=fields.Char('Complete name', compute="_computeCoplete_name",recursive=True,store=True)
    foods = fields.Many2many("menu_app.foods_model",relation="menu_app_category_model2foods_model",string="Foods")
    parent_id=fields.Many2one("menu_app.category_model",string="Parent Category", index=True, ondelete="cascade")
    #child_id=fields.One2many("menu_app.category_model", "parent_id", string="Childs category")

    @api.depends('name','parent_id.complete_name')
    def _computeCoplete_name(self):
        for category in self:
            if category.parent_id:
                category.complete_name= '%s / %s' % (category.parent_id.complete_name, category.name)
            else:
                category.complete_name=category.name