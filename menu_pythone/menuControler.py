
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

#===================================== DELETE =====================================

    def delIngrediente(self,id):
        url = "http://localhost:8069/menu_app/delIngridients"
        payload = {
            "id":id
        }
        response = requests.put(url,json=payload)
        data=response.json()
        print(data)
        return True

    def delCategory(self,id):
        url = "http://localhost:8069/menu_app/delCategory"
        payload = {
            "id":id
        }
        response = requests.put(url,json=payload)
        data=response.json()
        print(data)
        return True
    
    def delFood(self,id):
        url = "http://localhost:8069/menu_app/delFood"
        payload = {
            "id":id
        }
        response = requests.put(url,json=payload)
        data=response.json()
        print(data)
        return True

#===================================== SEARCH =====================================

    def getIng(self,id,send):
        # si id es "" da todos
        url = "http://localhost:8069/menu_app/getIngridients/"+id
        response = requests.get(url)
        data=response.json()
        if data["status"]!=200:
            return False
        if send:
            return data
        else:
            return True
    
    def getFood(self,id,send):
        url = "http://localhost:8069/menu_app/getFoods/"+id
        response = requests.get(url)
        data=response.json()
        if data["status"]!=200:
            return False
        if send:
            return data
        else:
            return True

    def getCat(self,id,send):
        url = "http://localhost:8069/menu_app/getCategory/"+id
        response = requests.get(url)
        data=response.json()
        if data["status"]!=200:
            return False
        if send:
            return data
        else:
            return True
    