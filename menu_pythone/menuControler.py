
import requests

class MenuCtrl():
    def __init__(self):
        self.saldo=0
#=====================================  ADD  =====================================
    def addIngrediente(name,allergens,description):
        return True
    def addCategory(name):
        return True

#===================================== MODIFI =====================================
#===================================== DELETE =====================================
#===================================== SEARCH =====================================
    def getIng(id,send):
        # si id es "" da todos
        url = "https://http://localhost:8069/menu_app/getIngridients/"+id
        response = requests.post(url)
        data=response.json()
        if data["status"]!=200:
            return False
        if send:
            return data
        else:
            return True
    
    def getFood(id,send):
        url = "https://http://localhost:8069/menu_app/getFoods/"+id
        response = requests.post(url)
        data=response.json()
        if data["status"]!=200:
            return False
        if send:
            return data
        else:
            return True

    def getCat(id,send):
        url = "https://http://localhost:8069/menu_app/getCategory/"+id
        response = requests.post(url)
        data=response.json()
        if data["status"]!=200:
            return False
        if send:
            return data
        else:
            return True
    