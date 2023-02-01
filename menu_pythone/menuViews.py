import menuControler
#       Ingredients
#name:char  -- readtxt
#allergens:boolean  -- readBoolean
#description:html  -- a pelo
#foods:Many2many  -- readNumber

#       Food
#name:char  -- readtxt
#price:double  -- readNumber
#description:html  -- a pelo
#foods:Many2many (quantiti)  -- readNumber
#ingredients:Many2many  -- readNumber
#category:Many2one  -- readNumber

#       Category
#name:char  -- readtxt
#foods:One2many  -- readNumber
def readTable():
    while True:
        doble=(input("Table (int):"))
        try:
            doble=int(doble)
            if doble>0:
                bien=True
                data=contoler.getOrder("",True)
                if data!=False:
                    for a in data["data"]:
                        if str(a["table"])==str(doble) and a["table_active"]==True:
                            print("That table is occupied")
                            bien=False
                if bien:
                    return str(doble)
            else:
                print("Input a value > 0")
        except:
                print("Input a int value ")
def readNumber(txt,i):
    while True:
        doble=(input(txt+"("+i+"):"))
        if i=="Double":
            try:
                doble=float(doble)
                if doble>0:
                    return str(doble)
                else:
                    print("Input a value > 0")
            except:
                print("Input a double value ")
        else:
            try:
                doble=int(doble)
                if doble>0:
                    return str(doble)
                else:
                    print("Input a value > 0")
            except:
                print("Input a int value ")

def readtxt(txt):
    while True:
        Name=(input(txt+":"))
        if len(Name)>0:
            return Name
        else:
            print("Incorrect "+txt)


def readBoolean(txt):
    while True:
        Name=(input(txt+"(YES/NO):"))
        if Name=="YES":
            return True
        elif Name=="NO":
            return False
        else:
            print("Incorrect option, ONLY CAPS")
def questionAddCat(first=True):
    while True:
        if first: Name=(input("Do you want to add a Category?(YES/NO):")) 
        else: Name=(input("Do you want to change the Category?(YES/NO):")) 
        if Name=="YES":
            return True
        elif Name=="NO":
            return False
        else:
            print("Incorrect option, ONLY CAPS")
        pass
def questionAddIng(first=True):
    while True:
        if first: Name=(input("Do you want to add a ingedient?(YES/NO):")) 
        else: Name=(input("Do you want to add an other ingedient?(YES/NO):")) 
        if Name=="YES":
            return True
        elif Name=="NO":
            return False
        else:
            print("Incorrect option, ONLY CAPS")
        pass
def questionMod(txt):
    while True:
        Name=(input("You want to mod the "+txt+"(YES/NO):"))
        if Name=="YES":
            return True
        elif Name=="NO":
            return False
        else:
            print("Incorrect option, ONLY CAPS")
def questionShow(txt):
    while True:
        Name=(input("Do you want to see a specific "+txt+"?(YES/NO):"))
        if Name=="YES":
            return True
        elif Name=="NO":
            return False
        else:
            print("Incorrect option, ONLY CAPS")

def questionModDel(txt):
    while True:
        Name=(input("Do you want to MOD or DEL a "+txt+"?(MOD/DEL):"))
        if Name=="MOD":
            return True
        elif Name=="DEL":
            return False
        else:
            print("Incorrect option, ONLY CAPS")    
def questionAddDelModQuant():
    while True:
        Name=(input("Do you want to ADD, REPLACE or DEL the quantity of the product?(ADD/REPLACE/DEL):"))
        if Name=="ADD":
            return Name
        elif Name=="REPLACE":
            return Name
        elif Name=="DEL":
            return Name
        else:
            print("Incorrect option, ONLY CAPS") 
def questionAddQuant(first=True):
    while True:
        if first: Name=(input("Do you want to add a product to de list?(YES/NO):")) 
        else: Name=(input("Do you want to add an other product to de list?(YES/NO):")) 
        if Name=="YES":
            return True
        elif Name=="NO":
            return False
        else:
            print("Incorrect option, ONLY CAPS")
        pass
# ========================================== Ingrediente ==========================================
def addIngrediente():
    name=readtxt("NAME")
    allergens=readBoolean("Allergens")
    description=input("Description:")
    if contoler.addIngrediente(name,allergens,description):
        print("The ingredient has been added successfully")
    else:
        print("There has been an unexpected error or the ingredient already exists")
    
def modIngrediente():
    id=readNumber("ID","int")
    if contoler.getIng(id,False):
        name=""
        allergens=""
        description=""
        if questionMod("name"):
            name=readtxt("NAME")
        if questionMod("allergens"):
            allergens=readBoolean("Allergens")
        if questionMod("the description"):
            description=input("Description:")
        if name=="" and allergens=="" and description=="":
            print("Why")
        elif contoler.modIngrediente(id,name,allergens,description):
            print("The ingredient has been modified correctly")
        else:
            print("There has been an unexpected error")
    else:
        print("This ingredient dont exist")

def delIngrediente():
    id=readNumber("ID","int")
    if contoler.getIng(id,False):
        contoler.delIngrediente(id)
        print("The ingredient has been removed successfully")
    else:
        print("This ingredient dont exist")

def showIngrediente():
    if questionShow("ingredient"):
        id=readNumber("ID","int")
        if contoler.getIng(id,False):
            data = contoler.getIng(id,True)
            for a in data["data"]:
                print(a["name"]+":")
                print("\tID: "+str(a["id"]))
                if (a["allergens"]):
                    print("\tAllergens: YES")
                else:
                    print("\tAllergens: NO")
                print("\tDescription:"+str(a["description"]))
                if len(a["foods"])==0:
                    print("\tIs in "+str(len(a["foods"]))+" products")
                else:
                    print("\tProducts:")
                    for a in a["foods"]:
                        dataFood=contoler.getFood(id,True)
                        print("\t - "+dataFood["data"][0]["name"])
        else:
            print("This ingredient dont exist")
    else:
        data = contoler.getIng("",True)
        if data!=False:
            for a in data["data"]:
                print(a["name"]+":")
                print("\tID: "+str(a["id"]))
                if (a["allergens"]):
                    print("\tAllergens: YES")
                else:
                    print("\tAllergens: NO")
                print("\tDescription:"+str(a["description"]))
                print("\tIs in "+str(len(a["foods"]))+" products")
        else:
            print("There are no ingredients in the DB")

# ========================================== Category ==========================================
def showCategory():
    if questionShow("category"):
        id=readNumber("ID","int")
        if contoler.getCat(id,False):
            data = contoler.getCat(id,True)
            for a in data["data"]:
                print(a["name"]+":")
                print("\tID: "+str(a["id"]))
                if len(a["foods"])==0:
                    print("\tIs in "+str(len(a["foods"]))+" products")
                else:
                    print("\tProducts:")
                    for b in a["foods"]:
                        dataFood=contoler.getFood(str(b),True)
                        print("\t - "+dataFood["data"][0]["name"])
        else:
            print("This category dont exist")
    else:
        data = contoler.getCat("",True)
        if data!=False:
            for a in data["data"]:
                print(a["name"]+":")
                print("\tID: "+str(a["id"]))
                print("\tHas "+str(len(a["foods"]))+" foods")
        else:
            print("There are no category in the DB")


def addCategory():
    name=readtxt("NAME")
    if contoler.addCategory(name):
        print("The Category has been added successfully")
    else:
        print("There has been an unexpected error or the category already exists")

def modCategory():
    id=readNumber("ID","int")
    if contoler.getCat(id,False):
        if questionMod("name"):
            name=readtxt("NAME")
            contoler.modCategory(id,name)
            print("The Category has been modified correctly")
    else:
        print("This category dont exist")
        
def delCategory():
    id=readNumber("ID","int")
    if contoler.getCat(id,False):
        contoler.delCategory(id)
        print("The category has been removed successfully")

    else:
        print("This category dont exist")

# ========================================== Products/Foods ==========================================
def showFood():
    if questionShow("product"):
        id=readNumber("ID","int")
        if contoler.getFood(id,False):
            data = contoler.getFood(id,True)
            for a in data["data"]:
                print(a["name"]+":")
                print("\tID: "+str(a["id"]))
                print("\tPrecio: "+str(a["price"])+"€")
                if a["category"]==False:
                    print("\tThey dont have category")
                else:
                    print("\tCategory: "+a["category"][1])
                print("\tDescripcion: "+str(a["description"]))
                if len(a["ingridients"])==0:
                    print("\tThis product dont have ingredients")
                else:
                    print("\tIngredients:")
                    for b in a["ingridients"]:
                        dataFood=contoler.getFood(str(b),True)
                        print("\t - "+dataFood["data"][0]["name"])
        else:
            print("This ingredient dont exist")
    else:
        data = contoler.getFood("",True)
        if data!=False:
            for a in data["data"]:
                print(a["name"]+":")
                print("\tID: "+str(a["id"]))
                print("\tPrecio: "+str(a["price"])+"€")
                if a["category"]==False:
                    print("\tThey dont have category")
                else:
                    print("\tCategory: "+a["category"][1])
                print("\tDescripcion: "+str(a["description"]))
                if len(a["ingridients"])==0:
                    print("\tThis product dont have ingredients")
                else:
                    print("\tThis product have "+str(len(a["ingridients"]))+"ingredients")
        else:
            print("There are no products in the DB")

def addFood():
    name=readtxt("NAME")
    price=readNumber("Price","Double")
    description=input("Description:")
    ingredients=[]
    cat=0
    if questionAddIng():
        while True:
            ing=readNumber("ingredient","int")
            if contoler.getIng(ing,False):
                if ing in ingredients:
                    print("This ingredient alredy inside")
                else:
                    ingredients.append(ing)
                    if not questionAddIng(False):
                        break
            else:
                print("This ingredient dont exist")
    if questionAddCat():
        while True:
            cat=readNumber("ingredient","int")
            if contoler.getCat(cat,False):
                break
            else:
                print("This ingredient dont exist")
    if contoler.addFood(name,price,description,ingredients,cat):
        print("The product has been added successfully")
    else:
        print("There has been an unexpected error or the food already exists")


def modFood():
    id=readNumber("ID","int")
    if contoler.getFood(id,False):
        data=contoler.getFood(id,True)
        name=""
        precio=""
        description=""
        ingredients=[]
        if len(data["data"][0]["ingridients"])==0:
            a=True
        else:
            a=False
            for ingr in data["data"][0]["ingridients"]:
                ingredients.append(ingr)
        ingNum=len(ingredients)
        category=""
        if questionMod("name"):
            name=readtxt("NAME")
        if questionMod("precio"):
            precio=readNumber("precio","Double")
        if questionMod("the description"):
            description=input("Description:")
        if questionAddIng(a):
            while True:
                ing=readNumber("ingredient","int")
                if contoler.getIng(ing,False):
                    if ing in ingredients:
                        print("This ingredient alredy inside")
                    else:
                        ingredients.append(ing)
                        if not questionAddIng(False):
                            break
                else:
                    print("This ingredient dont exist")
        if data["data"][0]["category"]==False:
            a=True
        else:
            a=False
        if questionAddCat(a):
            while True:
                category=readNumber("category","int")
                if contoler.getCat(category,False):
                    break
                else:
                    print("This category dont exist")
        if name=="" and precio=="" and description=="" and category=="" and len(ingredients)>ingNum:
            print("Why")
        elif contoler.modFood(id,name,precio,description,ingredients,category):
            print("The Product has been modified correctly")
        else:
            print("There has been an unexpected error")
    else:
        print("This Product dont exist")

def delFood():
    id=readNumber("ID","int")
    if contoler.getFood(id,False):
        contoler.delFood(id)
        print("The Product has been removed successfully")

    else:
        print("This Product dont exist")

# ========================================== Order ==========================================
#table int
#customer char
#waiter char
#total only show
#description a pelo
#order_active boolean
#table_active boolean
#quantiti lista
#state PE-PO
#date SET DATETIME EN EL PAGO
def showOrder():
    if questionShow("order"):
        id=readNumber("ID","int")
        if contoler.getOrder(id,False):
            data = contoler.getOrder(id,True)
            for a in data["data"]:
                if a["state"]=="AC":
                    print("Table: "+str(a["table"])+" Active")
                elif a["state"]=="PE":
                    print("Table: "+str(a["table"])+" Pending")
                else:
                    print("Table: "+str(a["table"])+" Paid")
                print("\tID: "+str(a["id"]))
                print("\tCustomer name:"+a["customer"])
                print("\tWaiter name:"+a["waiter"])
                print("\tTotal actual: "+str(a["total"])+"€")
                print("\tDescripcion: "+str(a["description"]))
                if len(a["quantiti"])==0:
                    print("\tThis order dont have ordered products")
                else:
                    print("\tOrders:")
                    for b in a["quantiti"]:
                        dataFood=contoler.getQuantiti(str(b),True)
                        print("\t "+str(dataFood["data"][0]["quantiti"])+" x "+dataFood["data"][0]["foods"][1])
        else:
            print("This Order dont exist")
    else:
        data = contoler.getOrder("",True)
        if data!=False:
            for a in data["data"]:
                if a["state"]=="AC":
                    print("Table: "+str(a["table"])+" Active")
                elif a["state"]=="PE":
                    print("Table: "+str(a["table"])+" Pending")
                else:
                    print("Table: "+str(a["table"])+" Paid")
                print("\tID: "+str(a["id"]))
                print("\tCustomer name:"+a["customer"])
                print("\tWaiter name:"+a["waiter"])
                print("\tTotal actual: "+str(a["total"])+"€")
                print("\tDescripcion: "+str(a["description"]))
                if len(a["quantiti"])==0:
                    print("\tThis order dont have ordered products")
                else:
                    print("\tThis product has "+str(len(a["quantiti"]))+" products ordered")
        else:
            print("There are no orders in the DB")
def addOrder():
    table=readTable()
    customer=readtxt("customer name")
    waiter=readtxt("waiter name")
    description=input("Description:")
    quantiti={}
    if questionAddQuant():
        while True:
            while True:
                idFood=readNumber("product","int")
                if idFood in quantiti or contoler.getFood(idFood,False):
                    break
                else:
                    print("This product dont exist")
            if idFood in quantiti:
                res=questionAddDelModQuant()
                if res=="ADD":
                    quant=readNumber("quantity","int")
                    quantiti[idFood]=str(int(quantiti[idFood])+int(quant))
                elif res=="REPLACE":
                    quant=readNumber("quantity","int")
                    quantiti[idFood]=quant
                else:
                    quantiti.pop(idFood)
            else:
                quant=readNumber("quantity","int")
                quantiti[idFood]=quant
            if not questionAddQuant(False):
                break
    if contoler.addOrder(table,customer,waiter,description,quantiti):
        print("The Order has been added successfully")
    else:
        print("There has been an unexpected error or the food already exists")
def modOrder():
    id=readNumber("ID","int")
    if contoler.getOrder(id,False):
        data=contoler.getOrder(id,True)
        if data["data"][0]["state"]=="AC":
            customer=""
            waiter=""
            description=""
            quantiti={}
            if questionMod("customer"):
                customer=readtxt("customer")
            if questionMod("waiter"):
                waiter=readtxt("waiter")
            if questionMod("the description"):
                description=input("Description:")
            if questionMod("the products list"):
                quantitiboolean=True
                if len(data["data"][0]["quantiti"])==0:
                    a=True
                else:
                    a=False
                    for quantityid in data["data"][0]["quantiti"]:
                        dataquan=contoler.getQuantiti(str(quantityid),True)
                        quantiti[dataquan["data"][0]["foods"][0]]=dataquan["data"][0]["quantiti"]
                while True:
                    while True:
                        idFood=readNumber("product","int")
                        if idFood in quantiti or contoler.getFood(idFood,False):
                            break
                        else:
                            print("This product dont exist")
                    if idFood in quantiti:
                        res=questionAddDelModQuant()
                        if res=="ADD":
                            quant=readNumber("quantity","int")
                            quantiti[idFood]=str(int(quantiti[idFood])+int(quant))
                        elif res=="REPLACE":
                            quant=readNumber("quantity","int")
                            quantiti[idFood]=quant
                        else:
                            quantiti[idFood]="DEL"
                    else:
                        quant=readNumber("quantity","int")
                        quantiti[idFood]=quant
                    if not questionAddQuant(False):
                        break
            else:
                quantitiboolean=False
            if customer=="" and waiter=="" and description=="" and quantitiboolean==False:
                print("Why")
            elif contoler.modOrder(id,customer,waiter,description,quantiti):
                print("The Order has been modified correctly")
            else:
                print("There has been an unexpected error")
        else:
            print("Paid orders cannot be modified")
    else:
        print("This Order dont exist")
def delOrder():
    id=readNumber("ID","int")
    if contoler.getOrder(id,False):
        contoler.delOrder(id)
        print("The Order has been removed successfully")

    else:
        print("This Order dont exist")
def payOrder():
    id=readNumber("ID","int")
    if contoler.getOrder(id,False):
        data=contoler.getOrder(id,True)
        if data["data"][0]["table_active"]:
            contoler.payOrder(id)
            print("The order has been paid successfully")
        else:
            print("The order has already been paid")
    else:
        print("This Order dont exist")
# ========================================== Menu ==========================================
contoler=menuControler.MenuCtrl()
while(True):
    print("==================================================================== Menu ====================================================================")
    print("1.- Add Ingredient\t|\t4.- Add Category\t|\t7.- Add Product\t\t|\t10.- Add Order\t\t|\t13.- Pay Order")
    print("2.- Mod/Del Ingredients\t|\t5.- Mod/Del Category\t|\t8.- Mod/Del Product\t|\t11.- Mod/Del Order\t|\t14.- Exit")
    print("3.- Show Ingredient/s\t|\t6.- Show Category/s\t|\t9.- Show Product/s\t|\t12.- Show Order/s")
    print("==============================================================================================================================================")
    option=int(input("Chose an option:"))
    if option==1:
        addIngrediente()
    elif option==2:
        if questionModDel("Ingredient"):
            modIngrediente()
        else:
            delIngrediente()
    elif option==3:
        showIngrediente()


    elif option==4:
        addCategory()
    elif option==5:
        if questionModDel("Category"):
            modCategory()
        else:
            delCategory()
    elif option==6:
        showCategory()

    
    elif option==7:
        addFood()
    elif option==8:
        if questionModDel("Product"):
            modFood()
        else:
            delFood()
    elif option==9:
        showFood()
    elif option==10:
        addOrder()
    elif option==11:
        if questionModDel("Order"):
            modOrder()
        else:
            delOrder()
    elif option==12:
        showOrder()
    elif option==13:
        payOrder()
    elif option==14:
        print("Today "+contoler.getSaldo()+"€ has been obtained")
        break
