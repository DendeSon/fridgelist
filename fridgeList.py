""" 
    Issues so far:
        - 'exit' does not always stop the program
        - add/removeIngredient needs an exception for 'exit' input(changing flag bool and loop)
"""

sorry = "Sorry, that input is not recognized."
bye = "Goodbye!"
notYet = "This function is not implemented yet."

currentIngredients = ["milk", "bread", "rice"]
snackList = []

###Recipes###

breakfast = {
    "cerealBowl" : ["milk", "cereal"],
    "toast" : ["bread", "butter"],
    "eggsBacon" : ["eggs", "bacon"]
}

lunch = {}

dinner = {
    "friedRice" : ["rice", "egg", "soySauce", "veggies", "chicken"],
    "eggsBacon" : ["eggs", "bacon"],
    "butterNoodles" : ["noodles", "butter", "parmesan"],
    "frenchToast" : ["bread", "eggs"],
    "ramenNoodles" : "ramen"
}

def Objective():
    userInput = input("What would you like to do? ingredients/recipes/exit ").lower()
    if userInput == "exit":
        print(bye)
        global flag
        flag = False
    elif userInput == "ingredients":
        Ingredient()
    elif userInput == "recipes":
        Recipes()
    else:
        print(sorry)
        Objective()        
        
###Ingredients Section###

def Ingredient():
    userIngredientsInput = input("Would you like to view the 'list', 'add' or 'remove' ingredients? add/remove/list/back/exit ").lower()
    if userIngredientsInput == "add":
        addIngredient()
        Ingredient()
    elif userIngredientsInput == "remove":
        removeIngredient()
        Ingredient()
    elif userIngredientsInput == "list":
        print(currentIngredients)
        Ingredient()
    elif userIngredientsInput == "back":
        Objective()
    elif userIngredientsInput == "exit":
        print(bye)
        global flag
        flag = False
    else:
        print(sorry)
        Ingredient()

def removeIngredient():
    removeInput = input("What ingredient would you like to remove? ").lower()
    try:
        currentIngredients.remove(removeInput)
        print(f"Removed '{removeInput}'!")
    except ValueError:
        print(f"'{removeInput}' is not in the ingredients lists!")
    finally:
        Ingredient()
        
def addIngredient():
    addInput = input("What ingredient would you like to add? ").lower()
    # sellByInput = input("Does this ingredient have a 'Sell By' date? ").lower() #Specify format mm/dd/yy
    # snackInput = input(f"Is '{addInput}' a snack?").lower() 
    currentIngredients.append(addInput)
    print(f"Added '{addInput}'!")
    Ingredient()
    
###Recipes Section###  
    
def Recipes():
    userRecipeInput = input("Which meal would you like to view? breakfast/lunch/dinner/snacks/back/exit ").lower()
    if userRecipeInput == "breakfast":
        breakfast_recipes()
    elif userRecipeInput == "lunch":
        lunch_recipes()
    elif userRecipeInput == "dinner":
        dinner_recipes()
    elif userRecipeInput == "snacks":
        snacks()
    elif userRecipeInput == "back":
        Objective()
    elif userRecipeInput == "exit":
        print(bye)
        global flag
        flag = False
    else:
        print(sorry)
        Recipes()
    

def breakfast_recipes():
    print(notYet)
    Recipes()
    
def lunch_recipes():
    print(notYet)
    Recipes()
    
def dinner_recipes():
    print(notYet)
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
    
"""
    In progress, function to check if a recipe has all required ingredients
"""

def scanRecipes(): #meal = breakfast/lunch/dinner
        print(notYet)
        Recipes()
#     for item in currentIngredients:
#         print(item)
#         if item in breakfast.values():
            
    
###General Loops###

flag = True   
 
while flag:
    Objective()