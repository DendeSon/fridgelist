"""

Personal project to help with fridge/pantry stock, choosing recipes, keeping track of expiry dates, etc...

"""


sorry = "Sorry, that input is not recognized."
bye = "Goodbye!"
notYet = "This function is not implemented yet."

###Stock###

currentIngredients = ["milk", "bread", "rice", "butter", "eggs"]
snackList = []

###Recipes###

breakfast = {
    "cerealBowl" : ["milk", "cereal"],
    "toast" : ["bread", "butter"],
    "eggsBacon" : ["eggs", "bacon"],
    "frenchToast" : ["bread", "eggs"]
}

lunch = {}

dinner = {
    "friedRice" : ["rice", "egg", "soySauce", "veggies", "chicken"],
    "eggsBacon" : ["eggs", "bacon"],
    "butterNoodles" : ["noodles", "butter", "parmesan"],
    "frenchToast" : ["bread", "eggs"],
    "ramenNoodles" : "ramen"
}

###Start Function###

def Objective():
    userInput = input("What would you like to do? ingredients/recipes/exit ").lower()
    if userInput == "exit":
        Exit()
        # print(bye)
        # global flag
        # flag = False
    elif userInput == "ingredients" or userInput == "i":
        Ingredient()
    elif userInput == "recipes" or userInput == "r":
        Recipes()
    else:
        print(sorry)
        Objective()

###Stop Function###

def Exit():
    print(bye)
    global flag
    flag = False
    return flag
        
###Ingredients Section###

def Ingredient():
    userIngredientsInput = input("Would you like to 'view', 'add' or 'remove' ingredients? add/remove/list/back/exit ").lower()
    if userIngredientsInput == "add":
        addIngredient()
    elif userIngredientsInput == "remove":
        removeIngredient()
    elif userIngredientsInput == "view":
        print(f"Current List of Ingredients:\n{currentIngredients}")
        Ingredient()
    elif userIngredientsInput == "back":
        print("Okay,")
        Objective()
    elif userIngredientsInput == "exit":
        Exit()
    else:
        print(sorry)
        Ingredient()

def removeIngredient():
    removeInput = input("What ingredient would you like to remove? ").lower()       
    if removeInput == "back":
        print("Okay,")
        Ingredient()
    elif removeInput == "exit":
        Exit()
    else:
        try:
            currentIngredients.remove(removeInput)
            print(f"Removed '{removeInput}'!")
        except ValueError:
            print(f"'{removeInput}' is not in the ingredients lists!")
        finally:
            Ingredient()
        
def addIngredient():
    addInput = input("What ingredient would you like to add? ").lower()
    if addInput == "back":
        print("Okay,")
        Ingredient()
    elif addInput == "exit":
        Exit()
    else:
        currentIngredients.append(addInput)
        print(f"Added '{addInput}'!")
        Ingredient()
    # sellByInput = input("Does this ingredient have a 'Sell By' date? ").lower() #Specify format mm/dd/yy
    # snackInput = input(f"Is '{addInput}' a snack?").lower() 
    
###Recipes Section###  
    
def Recipes():
    userRecipeInput = input("Which meal would you like to access? breakfast/lunch/dinner/snacks/back/exit ").lower()
    if userRecipeInput == "breakfast" or userRecipeInput == "b":
        breakfast_recipes()
    elif userRecipeInput == "lunch" or userRecipeInput == "l":
        lunch_recipes()
    elif userRecipeInput == "dinner" or userRecipeInput == "d":
        dinner_recipes()
    elif userRecipeInput == "snacks" or userRecipeInput == "s":
        snacks()
    elif userRecipeInput == "back":
        print("Okay,")
        Objective()
    elif userRecipeInput == "exit":
        Exit()
    else:
        print(sorry)
        Recipes()
    

def breakfast_recipes():
    printRecipes(breakfast)
    Recipes()
    
def lunch_recipes():
    printRecipes(lunch)
    Recipes()
    
def dinner_recipes():
    printRecipes(dinner)
    Recipes()

def snacks():
    print(notYet)
    Recipes()
    
def addRecipe():
    print(notYet)
    Recipes()

def removeRecipe():
    print(notYet)
    Recipes()

def scanRecipes(meal): #meal = breakfast/lunch/dinner
    return {
        r: i for r, i in meal.items()
        if set(currentIngredients).issuperset(set(i))
        }
    
def printRecipes(meal):
    print("Recipes with in stock ingredients:")
    for r, i in scanRecipes(meal).items():
        print(f"{r} with {i}")
    
            
    
###Program Loop###

flag = True

while flag:
    Objective()