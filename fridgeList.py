print(input("What would you like to do?"))
#Breakfast/lunch/dinner recipes
#Ingredients in stock that link to recipes

currentIngredients = ["milk", "bread", "rice"]

breakfast = {
    "cerealBowl" : ["milk", "cereal"],
    "toast" : ["bread", "butter"],
}

lunch = {

}

dinner = {
    "friedRice" : ["rice", "egg", "soySauce", "veggies"]
}

def removeIngredient():
    print(input("What ingredient would you like to remove?"))
    
def addIngredient():
    print(input("What ingredient would you like to add?"))
    print(input("Does this ingredient have a 'Sell By' date?"))

def breakfast_recipes():
    print("Recipes with in stock ingredients: ")
    
def lunch_recipes():
    print("Recipes with in stock ingredents: ")
    
def dinner_recipes():
    print("Recipes with in stock ingredients: ")

def snacks():
    print("Snacks available: ")