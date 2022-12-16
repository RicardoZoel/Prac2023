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
def readNumber(txt,i):
    while True:
        doble=(input(txt+"("+i+"):"))
        if len(doble)>0:
            if doble.isdecimal():
                return doble
        else:
            print("Input a correct value ")

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
        elif contoler.modIngrediente(name,allergens,description):
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
                if (a["name"]):
                    print("\tAllergens: YES")
                else:
                    print("\tAllergens: NO")
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
        for a in data["data"]:
            print(a["name"]+":")
            print("\tID: "+str(a["id"]))
            if (a["name"]):
                print("\tAllergens: YES")
            else:
                print("\tAllergens: NO")
            print("\tIs in "+str(len(a["foods"]))+" products")

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
                    for a in a["foods"]:
                        dataFood=contoler.getFood(id,True)
                        print("\t - "+dataFood["data"][0]["name"])
        else:
            print("This category dont exist")
    else:
        data = contoler.getCat("",True)
        print(data)
        for a in data["data"]:
            print(a["name"]+":")
            print("\tID: "+str(a["id"]))
            print("\tHas "+str(len(a["foods"]))+" foods")


def addCategory():
    name=readtxt("NAME")
    if contoler.addCategory(name):
        print("The Category has been added successfully")
    else:
        print("There has been an unexpected error or the category already exists")

def modCategory():
    id=readNumber("ID","int")
    if contoler.getIng(id,False):
        if questionMod("name"):
            name=readtxt("NAME")
            contoler.modCategory(id,name)
            print("The Category has been modified correctly")
    else:
        print("This ingredient dont exist")
        
def delCategory():
    id=readNumber("ID","int")
    if contoler.getCat(id,False):
        contoler.delCategory(id)
        print("The ingredient has been removed successfully")

    else:
        print("This category dont exist")

# ========================================== Products/Foods ==========================================
def addFood():
    name=readtxt("NAME")
    price=readNumber("Price","Double")
    description=input("Description:")
    ingredients=[]
    if questionAddIng():
        while True:
            ing=readNumber("ingredient","int")
            if showIngrediente(id,False):
                ingredients.append(ing)
                if not questionAddIng(False):
                    break
            else:
                print("This ingredient dont exist")
    if questionAddCat():
        cat=readNumber("ingredient","int")
    if contoler.addCategory(name):
        print("The Category has been mod successfully")
    else:
        print("There has been an unexpected error or the category already exists")
contoler=menuControler.MenuCtrl()
while(True):
    print("========= Menu =========")
    print("1.- Add Ingredient")
    print("2.- Mod/Del Ingredients")
    print("3.- Show Ingredient/s")
    print("")
    print("4.- Add Category")
    print("5.- Mod/Del Category") #(Al borrar la categoria los productos la pierde. No se borran los productos y lo pierden automaticamente)
    print("6.- Show Category/s")
    print("")
    print("7.- Add Product")
    print("8.- Mod/Del Product")
    print("9.- Show Product/s")
    print("")
    print("10.- Add Order")
    print("11.- Mod/Del Order")
    print("12.- Show Order/s")
    print("")
    print("13.- Pay Order ")
    print("14.- Exit")
    option=int(input("chose an option:"))
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
        pass
    elif option==11:
        pass
    elif option==12:
        pass
    elif option==13:
        pass
    elif option==14:
        print("Today "+contoler.getSaldo()+"€ has been obtained")
        break
