# -*- coding: utf-8 -*-
# from odoo import http
from odoo import http
from odoo.http import json,request

# ================================== Get ==================================
class MenuApp(http.Controller):
    @http.route('/menu_app/hello', auth='public', type="http")
    def indexHello(self, **kw):
        return "Hello, world"

    @http.route('/menu_app/foods', auth='public', type="http")
    def indexTask(self, **kw):
        taskdata = http.request.env["menu_app.foods_model"].sudo().search_read([],["name","currency_id","price","category","ingridients","image","description"])
        data={  "status":200,
                "data":taskdata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")
        
    @http.route('/menu_app/ingridients', auth='public', type="http")
    def indexIngridients(self, **kw):
        ingridientsdata = http.request.env["menu_app.ingridients_model"].sudo().search_read([],["name","allergens","foods","description"])
        data={  "status":200,
                "data":ingridientsdata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")
        
    @http.route('/menu_app/category', auth='public', type="http")
    def indexCategory(self, **kw):
        categorydata = http.request.env["menu_app.category_model"].sudo().search_read([],["name","foods"])
        data={  "status":200,
                "data":categorydata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")


# ================================== Post ==================================

# class MenuApp(http.Controller):
#     @http.route('/menu_app/menu_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/menu_app/menu_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('menu_app.listing', {
#             'root': '/menu_app/menu_app',
#             'objects': http.request.env['menu_app.menu_app'].search([]),
#         })

#     @http.route('/menu_app/menu_app/objects/<model("menu_app.menu_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('menu_app.object', {
#             'object': obj
#         })
