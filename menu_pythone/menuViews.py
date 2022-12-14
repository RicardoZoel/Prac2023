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
#ingridients:Many2many  -- readNumber
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
        Name=(input(txt+":"))
        if Name=="TRUE":
            return True
        elif Name=="FALSE":
            return False
        else:
            print("Incorrect option, ONLY CAPS")

def question(txt):
    while True:
        Name=(input("You want to mod the "+txt+"(YES/NO):"))
        if Name=="YES":
            return True
        elif Name=="NO":
            return False
        else:
            print("Incorrect option, ONLY CAPS")

# ========================================== Ingrediente ==========================================
def addIngrediente():
    name=readtxt("NAME")
    allergens=readBoolean("Allergens")
    description=input("Description:")
    contoler.addIngrediente(name,allergens,description)
    
def modIngrediente():
    id=readNumber("ID","int")
    if contoler.getIng(id,False):
        name=""
        allergens=""
        description=""
        if question("name"):
            name=readtxt("NAME")
        if question("allergens"):
            allergens=readBoolean("Allergens")
        if question("the description"):
            description=input("Description:")
        contoler.modIngrediente(name,allergens,description)
    else:
        print("This ingridient dont exist")

def delIngrediente():
    id=readNumber("ID","int")
    if contoler.getIng(id,False):
        contoler.delIngrediente(id)
    else:
        print("This ingridient dont exist")
# ========================================== Category ==========================================
def addCategory():
    name=readtxt("NAME")
    contoler.addCategory(name)

def modCategory():
    id=readNumber("ID","int")
    if contoler.getIng(id,False):
        if question("name"):
            name=readtxt("NAME")
            contoler.modCategory(name)
    else:
        print("This ingridient dont exist")
        
def delCategory():
    id=readNumber("ID","int")
    if contoler.getCat(id,False):
        contoler.delCategory(id)
    else:
        print("This category dont exist")

contoler=menuControler.MenuCtrl()
while(True):
    print("========= Menu =========")
    print("1.- Add Ingrediente")
    print("2.- Mod/Del Ingredients")
    print("3.- Show Ingredients")
    print("")
    print("4.- Add Category")
    print("5.- Mod/Del Category") #(Al borrar la categoria los productos la pierde. No se borran los productos y lo pierden automaticamente)
    print("6.- Show Category")
    print("")
    print("7.- Add Product")
    print("8.- Mod/Del Product")
    print("9.- Show Product")
    print("")
    print("10.- Add Order")
    print("11.- Mod/Del Order")
    print("12.- Show Order")
    print("")
    print("13.- Pay Order ")
    print("14.- Exit")