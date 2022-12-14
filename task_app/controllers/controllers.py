# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import json
from requests import request


class TaskApp(http.Controller):
    @http.route('/task_app/hello', auth='public', type='http')
    def hello(self, **kw):
        return "Hello, world"

    @http.route(['/task_app/getTask',"/task_app/getTask/<int:taskid>"], auth='public', type='http')
    def getTask(self, taskid=None, **kw):
        if taskid:
            domain=[("id","=", taskid)]
        else:
            domain=[]
        taskdata=http.request.env["task_app.task_model"].sudo().search_read(domain,["name","is_done","active","category","user","description","criticalValue"])
        data={"status":200,
               "data":taskdata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")
    
    @http.route(['/task_app/getCat',"/task_app/getCat/<int:catid>"], auth='public', type='http')
    def getCat(self, catid=None, **kw):
        if catid:
            domain=[("id","=", catid)]
        else:
            domain=[]
        catdata=http.request.env["task_app.category_model"].sudo().search_read(domain,["name","description","tasks","exampleHtml","totalCriticalValue","totalTasks"])
        data={"status":200,
               "data":catdata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")
        
    @http.route('/task_app/addCat', auth='public', type='json', method="POST")
    def addCat(self, **kw):
        response=request.jsonrequest
        try:
            result=http.request.env["task_app.category_model"].sudo().create(response)
            data={ "status":201,
                    "id":result.id}
            return data
        except Exception as e:
            data={ "status":404,
                    "error":e}
            return data
    
    @http.route('/task_app/updateTask/<int:taskid>', auth='public', type='json', method="PUT")
    def updateTask(self, taskid, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["task_app.task_model"].sudo().search([("id", "=", taskid)])
            result.write(response)
            data = { "status": 200,
                    "id": result.id}
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e}
            return data