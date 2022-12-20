
from datetime import datetime
import requests

class MenuCtrl():
    def __init__(self):
        self.saldo=0

    def getSaldo(self):
        return str(self.saldo)
#=====================================  ADD  =====================================

    def addIngrediente(self,name,allergens,description):
        url = "http://localhost:8069/menu_app/addIngridients/"
        payload = {
        "name": name,
        "allergens": allergens,
        "description": description
        }
        response = requests.post(url,json=payload)
        data=response.json()
        if data["result"]["status"]!=201:
            return False
        else:
            return True

    def addCategory(self,name):
        url = "http://localhost:8069/menu_app/addCategory/"
        payload = {
        "name": name
        }
        response = requests.post(url,json=payload)
        data=response.json()
        if data["result"]["status"]!=201:
            return False
        else:
            return True

    def addFood(self,name,precio,description,ingredients,category):
        url = "http://localhost:8069/menu_app/addFoods/"
        payload = {
        "name": name,
        "price": precio,
        "description": description
        }
        if len(ingredients)>0:
            payload["ingridients"]=ingredients
        if category!=0:
            payload["category"]=category
        response = requests.post(url,json=payload)
        data=response.json()
        if data["result"]["status"]!=201:
            return False
        else:
            return True

    def addOrder(self,table,customer,waiter,description,quantiti):
        url = "http://localhost:8069/menu_app/addOrder/"
        payload = {
        "table": table,
        "customer": customer,
        "waiter": waiter,
        "description":description
        }
        response = requests.post(url,json=payload)
        data=response.json()
        if data["result"]["status"]!=201:
            return False
        else:
            if len(quantiti)>0:
                listaq=[]
                total=0
                for a in quantiti:
                    listaq.append(self.addQantiti(data["result"]["id"],a,quantiti[a]))
                    pd=self.getFood(a,True)
                    total+=(float(pd["data"][0]["price"])*int(quantiti[a]))
                self.modOrderList(data["result"]["id"],listaq,total)
            return True
    def addQantiti(self,idorder,idproduct,quantiti):
        url = "http://localhost:8069/menu_app/addQuantiti/"
        payload = {
        "orders": idorder,
        "foods": idproduct,
        "quantiti":quantiti
        }
        response = requests.post(url,json=payload)
        data=response.json()
        if data["result"]["status"]!=201:
            return False
        else:
            return data["result"]["id"]


#===================================== MODIFI =====================================

    def modIngrediente(self,id,name,allergens,description):
        url = "http://localhost:8069/menu_app/updateIngridients/"+id
        payload = {}
        if name!="":
            payload["name"]=name
        if allergens!="":
            payload["allergens"]=allergens
        if description!="":
            payload["description"]=description

        response = requests.put(url,json=payload)
        data=response.json()
        if data["result"]["status"]!=200:
            return False
        else:
            return True

    def modCategory(self,id,name):
        url = "http://localhost:8069/menu_app/updateCategory/"+id
        payload = {
            "name":name
        }
        response = requests.put(url,json=payload)
        data=response.json()
        if data["result"]["status"]!=200:
            return False
        else:
            return True

    def modFood(self,id,name,precio,description,ingredients,category):
        url = "http://localhost:8069/menu_app/updateFood/"+id
        payload = {}
        if name!="":
            payload["name"]=name
        if precio!="":
            payload["price"]=precio
        if description!="":
            payload["description"]=description
        if category!="":
            payload["category"]=category
        payload["ingridients"]=ingredients

        response = requests.put(url,json=payload)
        data=response.json()
        if data["result"]["status"]!=200:
            return False
        else:
            return True

    def modOrderList(self,id,lista,total):
        url = "http://localhost:8069/menu_app/updateOrder/"+str(id)
        payload={
            "quantiti":lista,
            "total":total
        }
        response = requests.put(url,json=payload)
        data=response.json()

    def modOrder(self,id,customer,waiter,description,quantiti):
        url = "http://localhost:8069/menu_app/updateOrder/"+id
        payload = {}
        if customer!="":
            payload["customer"]=customer
        if waiter!="":
            payload["waiter"]=waiter
        if description!="":
            payload["description"]=description
        if len(quantiti)>0:
            listaq=[]
            total=0
            for a in quantiti:
                if self.exist(id,a):
                    if quantiti[a]=="DEL":
                        self.delQuantiti(self.exist(id,a,True))
                    else:
                        idq=self.exist(id,a,True)
                        listaq.append(self.modQuantiti(id,idq,quantiti[a]))
                else:
                    listaq.append(self.addQantiti(id,a,quantiti[a]))
                pd=self.getFood(a,True)
                total+=(float(pd["data"][0]["price"])*int(quantiti[a]))
            payload["quantiti"]=listaq
            payload["total"]=total

        response = requests.put(url,json=payload)
        data=response.json()
        if data["result"]["status"]!=200:
            return False
        else:
            return True
    def modQuantiti(self,idq,quantiti):
        url = "http://localhost:8069/menu_app/updateQuantiti/"+idq
        payload = {
            "quantiti":quantiti
        }
        response = requests.put(url,json=payload)
        data=response.json()
        if data["result"]["status"]!=200:
            return False
        else:
            return True
#===================================== DELETE =====================================

    def delIngrediente(self,id):
        url = "http://localhost:8069/menu_app/delIngridients"
        payload = {
            "id":id
        }
        response = requests.put(url,json=payload)
        data=response.json()
        return True

    def delCategory(self,id):
        url = "http://localhost:8069/menu_app/delCategory"
        payload = {
            "id":id
        }
        response = requests.put(url,json=payload)
        data=response.json()
        return True
    
    def delFood(self,id):
        url = "http://localhost:8069/menu_app/delFood"
        payload = {
            "id":id
        }
        response = requests.put(url,json=payload)
        data=response.json()
        return True

    def delOrder(self,id):
        url = "http://localhost:8069/menu_app/delOrder"
        payload = {
            "id":id
        }
        a=self.getOrder(id,True)
        self.delVincualtedQantitt(a["data"][0]["quantiti"])
        response = requests.put(url,json=payload)
        data=response.json()
        return True
    
    def delQuantiti(self,id):
        url = "http://localhost:8069/menu_app/delQuantiti"
        payload = {
            "id":id
        }
        response = requests.put(url,json=payload)
        data=response.json()
        return True
#===================================== SEARCH =====================================

    def getIng(self,id,send):
        # si id es "" da todos
        url = "http://localhost:8069/menu_app/getIngridients/"+id
        response = requests.get(url)
        data=response.json()
        if data["status"]!=200 or len(data["data"])==0:
            return False
        if send:
            return data
        else:
            return True
    
    def getFood(self,id,send):
        url = "http://localhost:8069/menu_app/getFoods/"+id
        response = requests.get(url)
        data=response.json()
        if data["status"]!=200 or len(data["data"])==0:
            return False
        if send:
            return data
        else:
            return True

    def getCat(self,id,send):
        url = "http://localhost:8069/menu_app/getCategory/"+id
        response = requests.get(url)
        data=response.json()
        if data["status"]!=200 or len(data["data"])==0:
            return False
        if send:
            return data
        else:
            return True

    def getOrder(self,id,send):
        url = "http://localhost:8069/menu_app/getOrder/"+id
        response = requests.get(url)
        data=response.json()
        if data["status"]!=200 or len(data["data"])==0:
            return False
        if send:
            return data
        else:
            return True

    def getQuantiti(self,id,send):
        url = "http://localhost:8069/menu_app/getQuantiti/"+id
        response = requests.get(url)
        data=response.json()
        if data["status"]!=200 or len(data["data"])==0:
            return False
        if send:
            return data
        else:
            return True

    
    def exist(self,idorder,idfood,returne=False):
        data = self.getOrder(idorder,True)
        for a in data["data"][0]["quantiti"]:
            data2=self.getQuantiti(a,True)
            if data2["data"][0]["foods"][0]==idfood:
                if returne:
                    return data2["data"][0]["id"]
                else:
                    return True
        return False

    def delVincualtedQantitt(self,listaborrar):
        for i in listaborrar:
            self.delQuantiti(i)

    def payOrder(self,id):
        url = "http://localhost:8069/menu_app/updateOrder/"+id
        payload = {
            "order_active":"order_active",
            "table_active":"table_active",
            "state":"PO"
        }
        response = requests.put(url,json=payload)
        data=response.json()
        if data["result"]["status"]!=200:
            return False
        else:
            data = self.getOrder(id,True)
            self.saldo+=float(data["data"][0]["total"])
            return True
