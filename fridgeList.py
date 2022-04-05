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
    removeInput = input("What ingredient would you like to remove? input/back ").lower()       
    if removeInput == "back":
        print("Okay,")
        Ingredient()
    else:
        try:
            currentIngredients.remove(removeInput)
            print(f"Removed '{removeInput}'!")
        except ValueError:
            print(f"'{removeInput}' is not in the ingredients lists!")
        finally:
            Ingredient()
        
def addIngredient():
    addInput = input("What ingredient would you like to add? input/back ").lower()
    if addInput == "back":
        print("Okay,")
        Ingredient()
    else:
        currentIngredients.append(addInput)
        print(f"Added '{addInput}'!")
        Ingredient()
    # sellByInput = input("Does this ingredient have a 'Sell By' date? ").lower() #Specify format mm/dd/yy
    # snackInput = input(f"Is '{addInput}' a snack?").lower() 
    
###Recipes Section###  
    
def Recipes():
    userRecipeInput = input("Which menu would you like to access? breakfast/lunch/dinner/snacks/add/remove/back/exit ").lower()
    if userRecipeInput == "breakfast" or userRecipeInput == "b":
        listOrAvailable = input("Would you like to 'list' the recipes or 'check' if they are available? list/check/back ").lower()
        if listOrAvailable == "list":
            recipesList(breakfast)
            Recipes()
        elif listOrAvailable == "check":
            printRecipes(breakfast)
            Recipes()
        elif listOrAvailable == "back":
            print("Okay,")
            Recipes()
        else:
            print(sorry)
            Recipes()
    elif userRecipeInput == "lunch" or userRecipeInput == "l":
        listOrAvailable = input("Would you like to 'list' the recipes or 'check' if they are available? list/check/back ").lower()
        if listOrAvailable == "list":
            recipesList(lunch)
            Recipes()
        elif listOrAvailable == "check":
            printRecipes(lunch)
            Recipes()
        elif listOrAvailable == "back":
            print("Okay,")
            Recipes()
        else:
            print(sorry)
            Recipes()        
    elif userRecipeInput == "dinner" or userRecipeInput == "d":
        listOrAvailable = input("Would you like to 'list' the recipes or 'check' if they are available? list/check/back ").lower()
        if listOrAvailable == "list":
            recipesList(dinner)
            Recipes()
        elif listOrAvailable == "check":
            printRecipes(dinner)
            Recipes()
        elif listOrAvailable == "back":
            print("Okay,")
            Recipes()
        else:
            print(sorry)
            Recipes()
    elif userRecipeInput == "snacks" or userRecipeInput == "s":
        snacks()
    elif userRecipeInput == "add":
        addRecipeInput = input("Which meal would you like to add a recipe to? breakfast/lunch/dinner/back ").lower()
        if addRecipeInput == "breakfast" or addRecipeInput == "b":
            addRecipe(breakfast)
        elif addRecipeInput == "lunch" or addRecipeInput == "l":
            addRecipe(lunch)
        elif addRecipeInput == "dinner" or addRecipeInput == "d":
            addRecipe(dinner)
        elif addRecipeInput == "back":
            print("Okay,")
            Recipes()
        else:
            print(sorry)
            Recipes()
    elif userRecipeInput == "remove":
        meal = input("Which meal would you like to remove a recipe from? breakfast/lunch/dinner/back ").lower()
        if meal == "breakfast" or meal == "b":
            removeRecipe(breakfast)
        elif meal == "lunch" or meal == "l":
            removeRecipe(lunch)
        elif meal == "dinner" or meal == "d":
            removeRecipe(dinner)
        elif meal == "back":
            print("Okay,")
            Recipes()
        else:
            print(sorry)
            Recipes()
    elif userRecipeInput == "back":
        print("Okay,")
        Objective()
    elif userRecipeInput == "exit":
        Exit()
    else:
        print(sorry)
        Recipes()
    

def recipesList(meal):
    for k, v in meal.items():
        print(k, v)
    Recipes()

def snacks():
    print(notYet)
    Recipes()
    
def addRecipe(meal):
    recipeName = input("What is the name of the recipe? ")
    tempIngredients = []
    while True:
        recipeIngredients = input("What ingredients are needed? (input 1 ingredient at a time, enter 'done' when finished)/back ").lower()        
        if recipeIngredients == "done":
            meal[recipeName] = tempIngredients
            print(f"Added {recipeName} with {tempIngredients}")
            break
        elif recipeIngredients == "back":
            print("Okay,")
            Recipes()
            break
        else:
            tempIngredients.append(recipeIngredients)
            print(f"Ingredients so far: {tempIngredients}")
    Recipes()

def removeRecipe(meal):
    print("Current Recipes:")
    for k, v in meal.items():
        print(k, v)
    recipeInput = input("Which recipe would you like to remove? input/back ").lower()
    if recipeInput == "back":
        print("Okay,")
        Recipes()
    else:
        try:
            del meal[recipeInput]
            print(f"Removed {recipeInput}")
        except KeyError:
            print(f"{recipeInput} is not in the recipes list!")
    Recipes()

def scanRecipes(meal):
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