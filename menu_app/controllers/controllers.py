# -*- coding: utf-8 -*-
# from odoo import http
from odoo import http
from odoo.http import json,request

class MenuApp(http.Controller):

# ================================== Get ==================================

    @http.route('/menu_app/hello', auth='public', type="http")
    def indexHello(self, **kw):
        return "Hello, world"

    @http.route(['/menu_app/getFoods','/menu_app/getFoods/<int:foodid>'], auth='public', type="http")
    def indexTask(self,foodid=None, **kw):
        if foodid:
            domain=[("id","=", foodid)]
        else:
            domain=[]
        taskdata = http.request.env["menu_app.foods_model"].sudo().search_read(domain,["name","currency_id","price","category","ingridients","image","description"])
        data={  "status":200,
                "data":taskdata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")
        
    @http.route(['/menu_app/getIngridients','/menu_app/getIngridients/<int:ingridientsid>'], auth='public', type="http")
    def indexIngridients(self,ingridientsid=None, **kw):
        if ingridientsid:
            domain=[("id","=", ingridientsid)]
        else:
            domain=[]
        ingridientsdata = http.request.env["menu_app.ingridients_model"].sudo().search_read(domain,["name","allergens","foods","description"])
        data={  "status":200,
                "data":ingridientsdata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")
        
    @http.route(['/menu_app/getCategory','/menu_app/getCategory/<int:categoryid>'], auth='public', type="http")
    def indexCategory(self,categoryid=None, **kw):
        if categoryid:
            domain=[("id","=", categoryid)]
        else:
            domain=[]
        categorydata = http.request.env["menu_app.category_model"].sudo().search_read(domain,["name","foods"])
        data={  "status":200,
                "data":categorydata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")


# ================================== Post ==================================
    
    @http.route('/menu_app/addCategory', auth='public', type='json', method="POST")
    def addCategory(self, **kw):
        response=request.jsonrequest
        try:
            result=http.request.env["menu_app.category_model"].sudo().create(response)
            data={ "status":201,
                    "id":result.id}
            return data
        except Exception as e:
            data={ "status":404,
                    "error":e}
            return data

    @http.route('/menu_app/addIngridients', auth='public', type='json', method="POST")
    def addIngridients(self, **kw):
        response=request.jsonrequest
        try:
            result=http.request.env["menu_app.ingridients_model"].sudo().create(response)
            data={ "status":201,
                    "id":result.id}
            return data
        except Exception as e:
            data={ "status":404,
                    "error":e}
            return data
    
    @http.route('/menu_app/addFoods', auth='public', type='json', method="POST")
    def addFoods(self, **kw):
        response=request.jsonrequest
        try:
            result=http.request.env["menu_app.foods_model"].sudo().create(response)
            data={ "status":201,
                    "id":result.id}
            return data
        except Exception as e:
            data={ "status":404,
                    "error":e}
            return data

# ================================== PUT ==================================

    @http.route('/menu_app/updateCategory/<int:categoryid>', auth='public', type='json', method="PUT")
    def updateTask(self, categoryid, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["menu_app.category_model"].sudo().search([("id", "=", categoryid)])
            result.write(response)
            data = { "status": 200,
                    "id": result.id}
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e}
            return data

    @http.route('/menu_app/updateIngridients/<int:ingridientsid>', auth='public', type='json', method="PUT")
    def updateTask(self, ingridientsid, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["menu_app.ingridients_model"].sudo().search([("id", "=", ingridientsid)])
            result.write(response)
            data = { "status": 200,
                    "id": result.id}
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e}
            return data

    @http.route('/menu_app/updateFood/<int:foodid>', auth='public', type='json', method="PUT")
    def updateTask(self, foodid, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["menu_app.foods_model"].sudo().search([("id", "=", foodid)])
            result.write(response)
            data = { "status": 200,
                    "id": result.id}
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e}
            return data
        
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
