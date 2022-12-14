# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import json


class TaskApp(http.Controller):
    # ================================== Get ==================================

    @http.route('/task_app/hello', auth='public', type="http")
    def GetHello(self, **kw):
        return "Hello, world"

    @http.route('/task_app/task', auth='public', type="http")
    def GetTask(self, **kw):
        taskdata = http.request.env["task_app.task_model"].sudo().search_read([],["name","is_done","active","category","now","user","description","lastUpdate","criticalValue","creationdate"])
        data={  "status":200,
                "data":taskdata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")
        
    @http.route('/task_app/category', auth='public', type="http")
    def GetCategory(self, **kw):
        categorydata = http.request.env["task_app.category_model"].sudo().search_read([],["name","description","tasks","totalCriticalValue","totalTasks"])
        data={  "status":200,
                "data":categorydata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")
# ================================== Post ==================================
    @http.route('/task_app/task', auth='public', type="http")
    def PostTask(self, **kw):
        taskdata = http.request.env["task_app.task_model"].sudo().create([],["name","is_done","active","category","now","user","description","lastUpdate","criticalValue","creationdate"])
        data={  "status":200,
                "data":taskdata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")
        
    @http.route('/task_app/category', auth='public', type="http")
    def PostCategory(self, **kw):
        categorydata = http.request.env["task_app.category_model"].sudo().search_read([],["name","description","tasks","totalCriticalValue","totalTasks"])
        data={  "status":200,
                "data":categorydata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")


#     @http.route('/task_app/task_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('task_app.listing', {
#             'root': '/task_app/task_app',
#             'objects': http.request.env['task_app.task_app'].search([]),
#         })

#     @http.route('/task_app/task_app/objects/<model("task_app.task_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('task_app.object', {
#             'object': obj
#         })
