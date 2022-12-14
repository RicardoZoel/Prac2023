from odoo import models, fields, api


class CategoryModel(models.Model):
    _name = 'task_app.category_model'
    _description = 'Category Model'

    name = fields.Char("Category Name", required=True)
    description = fields.Html('Description')

    #Relacion uno a muchos (entre parentesis el "modelo","relacionUno","Nombre")
    tasks = fields.One2many("task_app.task_model","category","Tasks")
    exampleHtml=fields.Html('Example html')
    totalCriticalValue=fields.Integer("Total critical Value",compute="_total", store=True)
    totalTasks=fields.Integer("Total tasks",compute="_totalTasks", store=True)


    @api.depends("tasks.criticalValue")
    def _total(self):
        self.totalCriticalValue=0
        for rec in self.tasks:
            self.totalCriticalValue += rec.criticalValue

    @api.depends("tasks")
    def _totalTasks(self):
        self.totalTasks=0
        for rec in self.tasks:
            self.totalTasks += 1
    """
    @api.multi
    def action_print(self):
        return self.env.ref('report_name').report_action(self)
        
    """
    