"""

Personal project to help with fridge/pantry stock, choosing recipes, keeping
track of expiry dates, etc...

"""
import json

sorry = "Sorry, that input is not recognized."
bye = "Goodbye!"
not_yet = "This function is not implemented yet."

#Stock

current_ingredients = []
snack_list = []

#Recipes

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

#Start Function

def objective():
    """Takes user input and directs them to a new menu, asks for input again or exits."""
    user_input = input("Would you like to access 'ingredients', 'recipes' or 'exit'? ").lower()
    if user_input == "exit":
        exit()
    elif user_input == "ingredients" or user_input == "i":
        ingredients()
    elif user_input == "recipes" or user_input == "r":
        recipes()
    else:
        print(sorry)
        objective()

#Stop Function

def exit():
    """Exits the script and saves files."""
    if __name__ == "__main__":
        save_files()
    print(bye)

#File Functions

def save_files():
    """Saves current ingredients, breakfast, lunch and dinner."""
    print("Saving...")
    with open("ingredients.json", "w") as f:
        f.write(json.dumps(current_ingredients, indent=4))
    with open("breakfast.json", "w") as f:
        f.write(json.dumps(breakfast, indent=4))
    with open("lunch.json", "w") as f:
        f.write(json.dumps(lunch, indent=4))
    with open("dinner.json", "w") as f:
        f.write(json.dumps(dinner, indent=4))
    print("Saved\n")

def load_files():
    """Loads current ingredients, breakfast, lunch and dinner."""
    print("Loading...")
    with open("ingredients.json", "r") as f:
        global current_ingredients
        current_ingredients = json.load(f)
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
        
#Ingredients Section

def ingredients():
    """Takes user input and directs them to a new menu, asks for input again, returns to previous menu (objective) or exits. """
    user_input = input("Would you like to 'view', 'add' or 'remove' ingredients? back/exit ").lower()
    if user_input == "add":
        add_ingredient()
    elif user_input == "remove":
        remove_ingredient()
    elif user_input == "view":
        print(f"Current List of Ingredients:\n{current_ingredients}")
        ingredients()
    elif user_input == "back":
        print("Okay,")
        objective()
    elif user_input == "exit":
        exit()
    else:
        print(sorry)
        ingredients()

def remove_ingredient():
    """Takes user input on which ingredient to remove. Returns to previous menu (ingredients) or tries to remove ingredient from current_ingredients list, else raises error."""
    print(f"Current Ingredients:\n{current_ingredients}")
    user_input = input("What ingredient would you like to remove? input/back ").lower()       
    if user_input == "back":
        print("Okay,")
    else:
        try:
            current_ingredients.remove(user_input)
            print(f"Removed '{user_input}'!")
        except ValueError:
            print(f"'{user_input}' is not in the ingredients lists!")
    ingredients()
        
def add_ingredient():
    """Takes user input on which ingredient to add. Tries to append ingredient to current_ingredients list or returns to previous menu (ingredients)."""
    print(f"Current Ingredients:\n{current_ingredients}")
    user_input = input("What ingredient would you like to add? input/back ").lower()
    if user_input == "back":
        print("Okay,")
    else:
        current_ingredients.append(user_input)
        print(f"Added '{user_input}'!")
    ingredients()
    # sellByInput = input("Does this ingredient have a 'Sell By' date? ").lower() #Specify format mm/dd/yy
    # snackInput = input(f"Is '{userInput}' a snack?").lower() 
    
#Recipes Section  
    
def recipes():
    """Takes user input and directs them to a new menu, returns to previous menu (objective) or exits."""
    user_input = input("Would you like to access 'breakfast', 'lunch', 'dinner' or 'snacks'? Which menu would you like to access? add/remove/back/exit ").lower()
    if user_input == "breakfast" or user_input == "b":
        viewOrCheck = input("Would you like to 'view' the recipes or 'check' if any are available? /back ").lower()
        if viewOrCheck == "view":
            recipes_list(breakfast, "breakfast")
        elif viewOrCheck == "check":
            print_recipes(breakfast)
        elif viewOrCheck == "back":
            print("Okay,")
        else:
            print(sorry)
        recipes()
    elif user_input == "lunch" or user_input == "l":
        viewOrCheck = input("Would you like to 'view' the recipes or 'check' if any are available? /back ").lower()
        if viewOrCheck == "view":
            recipes_list(lunch, "lunch")
        elif viewOrCheck == "check":
            print_recipes(lunch)
        elif viewOrCheck == "back":
            print("Okay,")
        else:
            print(sorry)
        recipes()     
    elif user_input == "dinner" or user_input == "d":
        viewOrCheck = input("Would you like to 'view' the recipes or 'check' if any are available? /back ").lower()
        if viewOrCheck == "view":
            recipes_list(dinner, "dinner")
        elif viewOrCheck == "check":
            print_recipes(dinner)
        elif viewOrCheck == "back":
            print("Okay,")
        else:
            print(sorry)
        recipes()
    elif user_input == "snacks" or user_input == "s":
        snacks()
    elif user_input == "add":
        addRecipeInput = input("Would you like to add a recipe to 'breakfast', 'lunch' or 'dinner'? /back ").lower()
        if addRecipeInput == "breakfast" or addRecipeInput == "b":
            add_recipe(breakfast)
        elif addRecipeInput == "lunch" or addRecipeInput == "l":
            add_recipe(lunch)
        elif addRecipeInput == "dinner" or addRecipeInput == "d":
            add_recipe(dinner)
        elif addRecipeInput == "back":
            print("Okay,")
            recipes()
        else:
            print(sorry)
            recipes()
    elif user_input == "remove":
        meal = input("Would you like to remove a recipe from 'breakfast', 'lunch' or 'dinner'? /back ").lower()
        if meal == "breakfast" or meal == "b":
            remove_recipe(breakfast)
        elif meal == "lunch" or meal == "l":
            remove_recipe(lunch)
        elif meal == "dinner" or meal == "d":
            remove_recipe(dinner)
        elif meal == "back":
            print("Okay,")
            recipes()
        else:
            print(sorry)
            recipes()
    elif user_input == "back":
        print("Okay,")
        objective()
    elif user_input == "exit":
        exit()
    else:
        print(sorry)
        recipes()
    
def recipes_list(meal,meal_as_string = "meal"):
    """Takes in a meal dictionary and the name of the meal as a string, returns either a recipes list or prompt for no recipes."""
    if not meal:
        print("No recipes are available for " + meal_as_string)
    else:
        for k, v in meal.items():
            print(k, v)

def snacks():
    """Not yet implemented."""
    print(not_yet)
    recipes()
    
def add_recipe(meal):
    """Takes in a meal dictionary and asks the user for input on recipe_name and temp_ingredients. Displays temp_ingredients
     list after each ingredient is added. Once "done", creates a new recipe in the meal dictionary. Can return to previous menu (recipes)."""
    recipe_name = input("What is the name of the recipe? ")
    temp_ingredients = []
    while True:
        recipe_ingredients = input("What ingredients are needed? (input 1 ingredient at a time, enter 'done' when finished)/back ").lower()        
        if recipe_ingredients == "done":
            meal[recipe_name] = temp_ingredients
            print(f"Added {recipe_name} with {temp_ingredients}")
            break
        elif recipe_ingredients == "back":
            print("Okay,")
            break
        else:
            temp_ingredients.append(recipe_ingredients)
            print(f"Ingredients so far: {temp_ingredients}")
    recipes()

def remove_recipe(meal):
    """Takes in a meal dictionary and prints out recipes. Asks user for input on which recipe to remove and deletes it. Can return to previous menu (recipes)."""
    print("Current Recipes:")
    for k, v in meal.items():
        print(k, v)
    recipe_input = input("Which recipe would you like to remove? input/back ").lower()
    if recipe_input == "back":
        print("Okay,")
    else:
        try:
            del meal[recipe_input]
            print(f"Removed '{recipe_input}'")
        except KeyError:
            print(f"'{recipe_input}' is not in the recipes list!")
    recipes()

def get_available_recipes(meal):
    """Takes in a meal dictionary and checks if the current_ingredients list is a super set of any recipes in the meal. Returns the matching recipes."""
    return {
        r: i for r, i in meal.items()
        if set(current_ingredients).issuperset(set(i))
        }
    
def print_recipes(meal):
    """Prints out available recipes with current ingredients or no recipes available."""
    print("Recipes with in stock ingredients:")
    if not get_available_recipes(meal):
        print("No recipes available to make!")
    else:
        for r, i in get_available_recipes(meal).items():
            print(f"{r} with {i}")
    
#Script Start

if __name__ == "__main__":
    load_files()
    objective()