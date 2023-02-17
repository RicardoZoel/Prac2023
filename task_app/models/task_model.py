
from xml.dom import ValidationErr
from odoo import models, fields, api
from datetime import datetime, timedelta

class TaskModel(models.Model):
    _name = 'task_app.task_model'
    _description = 'Task Model'

    _sql_constraints = [('task_name_uniq','UNIQUE (name, active)','There cannot be two tasks with the same name!!'),]

    name = fields.Char("Task Name", required=True)
    is_done = fields.Boolean('Is done?', default=False)
    active = fields.Boolean('Is active?', default=True)
    category = fields.Many2one("task_app.category_model", "Category")
    
    now = fields.Datetime(string='Date')
    user = fields.Char(string='User: ')
    description = fields.Html(string='Description: ',help="Actions for this task")
    lastUpdate = fields.Datetime("Last update", compute="_lastUpdate", store=True)
    criticalValue=fields.Integer("Critical Value")

    creationdate=fields.Datetime(string="Creation date", help="Create date to task",default=lambda self:datetime.now())




    @api.constrains("name")
    def _check_longitud(self):
        if len(self.name) < 3:
            raise ValidationErr("The name of the task must have at least 5 characters!")
        return True



    @api.depends("description")
    def _lastUpdate(self):
        self.lastUpdate = datetime.now() 
        return True
    
    
    @api.onchange("is_done")

    #def _changeActiveTask(self):
    def _changeActiveTask(self):
        self.active = not self.is_done
        self.is_done = not self.active
        if self.is_done:
            self.now =datetime.now() + timedelta(hours=1)
            self.user=self.env.user.name
            self.active=False
        

    def changeState(self):
        #self.ensure_one()                   
        self.is_done = not self.is_done
        self.active = not self.is_done
        

    def cleanFinished(self):
        records = self.search([("active","=",False)])
        for rec in records:
            rec.unlink()