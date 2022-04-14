"""

Personal project to help with fridge/pantry stock, choosing recipes, keeping track of expiry dates, etc...

"""
import json

sorry = "Sorry, that input is not recognized."
bye = "Goodbye!"
notYet = "This function is not implemented yet."

###Stock###

currentIngredients = []
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
    userInput = input("Would you like to access 'ingredients', 'recipes' or 'exit'? ").lower()
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
    if __name__ == "__main__":
        save()
    print(bye)

###File Functions###

def save():
    print("Saving...")
    with open("ingredients.json", "w") as f:
        f.write(json.dumps(currentIngredients, indent=4))
    with open("breakfast.json", "w") as f:
        f.write(json.dumps(breakfast, indent=4))
    with open("lunch.json", "w") as f:
        f.write(json.dumps(lunch, indent=4))
    with open("dinner.json", "w") as f:
        f.write(json.dumps(dinner, indent=4))
    print("Saved\n")

def load_files():
    print("Loading...")
    with open("ingredients.json", "r") as f:
        global currentIngredients
        currentIngredients = json.load(f)
    with open("breakfast.json", "r") as f:
        global breakfast
        breakfast = json.load(f)
    with open("lunch.json", "r") as f:
        global lunch
        lunch = json.load(f)
    with open("dinner.json", "r") as f:
        global dinner
        dinner = json.load(f)
    print("Loaded Files\n")
        
###Ingredients Section###

def Ingredient():
    userInput = input("Would you like to 'view', 'add' or 'remove' ingredients? back/exit ").lower()
    if userInput == "add":
        addIngredient()
    elif userInput == "remove":
        removeIngredient()
    elif userInput == "view":
        print(f"Current List of Ingredients:\n{currentIngredients}")
        Ingredient()
    elif userInput == "back":
        print("Okay,")
        Objective()
    elif userInput == "exit":
        Exit()
    else:
        print(sorry)
        Ingredient()

def removeIngredient():
    print(f"Current Ingredients:\n{currentIngredients}")
    userInput = input("What ingredient would you like to remove? input/back ").lower()       
    if userInput == "back":
        print("Okay,")
    else:
        try:
            currentIngredients.remove(userInput)
            print(f"Removed '{userInput}'!")
        except ValueError:
            print(f"'{userInput}' is not in the ingredients lists!")
    Ingredient()
        
def addIngredient():
    print(f"Current Ingredients:\n{currentIngredients}")
    userInput = input("What ingredient would you like to add? input/back ").lower()
    if userInput == "back":
        print("Okay,")
    else:
        currentIngredients.append(userInput)
        print(f"Added '{userInput}'!")
    Ingredient()
    # sellByInput = input("Does this ingredient have a 'Sell By' date? ").lower() #Specify format mm/dd/yy
    # snackInput = input(f"Is '{userInput}' a snack?").lower() 
    
###Recipes Section###  
    
def Recipes():
    userInput = input("Would you like to access 'breakfast', 'lunch', 'dinner' or 'snacks'? Which menu would you like to access? add/remove/back/exit ").lower()
    if userInput == "breakfast" or userInput == "b":
        viewOrCheck = input("Would you like to 'view' the recipes or 'check' if any are available? /back ").lower()
        if viewOrCheck == "view":
            recipesList(breakfast, "breakfast")
        elif viewOrCheck == "check":
            printRecipes(breakfast)
        elif viewOrCheck == "back":
            print("Okay,")
        else:
            print(sorry)
        Recipes()
    elif userInput == "lunch" or userInput == "l":
        viewOrCheck = input("Would you like to 'view' the recipes or 'check' if any are available? /back ").lower()
        if viewOrCheck == "view":
            recipesList(lunch, "lunch")
        elif viewOrCheck == "check":
            printRecipes(lunch)
        elif viewOrCheck == "back":
            print("Okay,")
        else:
            print(sorry)
        Recipes()     
    elif userInput == "dinner" or userInput == "d":
        viewOrCheck = input("Would you like to 'view' the recipes or 'check' if any are available? /back ").lower()
        if viewOrCheck == "view":
            recipesList(dinner, "dinner")
        elif viewOrCheck == "check":
            printRecipes(dinner)
        elif viewOrCheck == "back":
            print("Okay,")
        else:
            print(sorry)
        Recipes()
    elif userInput == "snacks" or userInput == "s":
        snacks()
    elif userInput == "add":
        addRecipeInput = input("Would you like to add a recipe to 'breakfast', 'lunch' or 'dinner'? /back ").lower()
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
    elif userInput == "remove":
        meal = input("Would you like to remove a recipe from 'breakfast', 'lunch' or 'dinner'? /back ").lower()
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
    elif userInput == "back":
        print("Okay,")
        Objective()
    elif userInput == "exit":
        Exit()
    else:
        print(sorry)
        Recipes()
    
def recipesList(meal,mealAsString = "meal"):
    if not meal:
        print("No recipes are available for " + mealAsString)
    else:
        for k, v in meal.items():
            print(k, v)

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
    else:
        try:
            del meal[recipeInput]
            print(f"Removed '{recipeInput}'")
        except KeyError:
            print(f"'{recipeInput}' is not in the recipes list!")
    Recipes()

def scanRecipes(meal):
    return {
        r: i for r, i in meal.items()
        if set(currentIngredients).issuperset(set(i))
        }
    
def printRecipes(meal):
    print("Recipes with in stock ingredients:")
    if not scanRecipes(meal):
        print("No recipes available to make!")
    else:
        for r, i in scanRecipes(meal).items():
            print(f"{r} with {i}")
    
###Script Start###

if __name__ == "__main__":
    load_files()
    Objective()