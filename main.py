import sys
from helpers import lst_of_urls
from RecipeInfo import RecipeInfo
import sys

recipes = []
test_methods = []


def main():

    for i, url in enumerate(lst_of_urls[:]):
        print("Checked {}/{} URLs".format(i+1, len(lst_of_urls)), end='\r')
        rcp = RecipeInfo(url)
        recipes.append(rcp)
        #for ing in rcp.Methods: Methods field is a list of methods at the moment
        #    test_methods.append(ing.methods)
        print(str(rcp))

def askForTransformation():
    print("Please enter the integer from the list below " +
          "corresponding to a transformation to apply to the recipe." +
          "\n1) Identity transformation (no transformation)" +
          "\n2) Double the quantity"+
          "\n3) Halve the quantity"+
          "\n4) Make it healthier"+
          "\n5) Make it less healthy"+
          "\n6) Make it vegetarian"+
          "\n7) Make it un-vegetarian"+
          "\n8) Convert to Asian cuisine"+
          "\n9) Quit")
    transformation = input()
    if transformation == "1":
        print(str(rcp))
    elif transformation == "2":
        rcp.transformQuantities(2)
        print("We halved the quantity. Here you go!")
    elif transformation == "3":
        rcp.transformQuantities(.5)
        print("We doubled the quantity. Here you go!")
    elif transformation == "4":
        rcp.healthify()
        print("We made the recipe healthier. Here you go!")
    elif transformation == "5":
        rcp.unHealthify()
        print("We made the recipe less healthy. Here you go!")
    elif transformation == "6":
        rcp.makeVegetarian()
        print("We made the recipe vegetarian. Here you go!")
    elif transformation == "7":
        rcp.makeUnVegetarian()
        print("We made the recipe un-vegetarian. Here you go!")
    elif transformation == "8":
        rcp.makeAsian()
        print("We made the recipe Asian style. Here you go!")
    elif transformation == "9":
        print("Goodbye.")
        quit()
    else:
        print("Sorry, that was an invalid option. Goodbye.")
        quit()
    print(str(rcp))
    print("Would you like to apply another transformation? If so...")



if __name__ == "__main__":
    if len(sys.argv) <= 1:
        rcp = RecipeInfo("https://www.allrecipes.com/recipe/45856/avocado-steak/")
        rcp.makeAsian()
        print(str(rcp))

        # main()
        print("hey")
    elif sys.argv[1].startswith("https://www.allrecipes.com"):
        url = sys.argv[1]
        rcp = RecipeInfo(url)
        print("We received your recipe!")
        print(str(rcp))
        while True:
            askForTransformation()
    else:
        print("Welcome. Please enter an AllRecipes url for us to parse.")
        url = input()
        rcp = RecipeInfo(url)
        print("Got it!")
        print(str(rcp))
        while True:
            askForTransformation()
