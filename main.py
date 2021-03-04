import sys
from helpers import lst_of_urls
from RecipeInfo import RecipeInfo
import sys

recipes = []
test_ingredients = []


def main():
    '''
    for i, url in enumerate(lst_of_urls[:10]):
        print("Checked {}/{} URLs".format(i+1, len(lst_of_urls)), end='\r')
        rcp = RecipeInfo(url)
        recipes.append(rcp)
        for ing in rcp.Ingredients:
            test_ingredients.append(ing)
    '''
    # copy & pasted the loop for testing
    for i, url in enumerate(lst_of_urls[:10]):
        print("Checked {}/{} URLs".format(i + 1, len(lst_of_urls)), end='\r')
        rcp = RecipeInfo(url)
        recipes.append(rcp)

def askForTransformation():
    print("Please enter the integer from the list below " +
          "corresponding to a transformation to apply to the recipe." +
          "\n1) Identity transformation (no transformation)" +
          "\n2) Double the quantity"
          "\n3) Halve the quantity"
          "\n4) Make it healthier")
    transformation = input()
    if transformation == "1":
        print(str(rcp))
    elif transformation == "2":
        rcp.double()
        print(str(rcp))
    elif transformation == "3":
        rcp.halve()
        print(str(rcp))
    elif transformation == "4":
        rcp.healthify()
        print(str(rcp))
    else:
        print("Sorry, that was an invalid option. Goodbye.")



if __name__ == "__main__":
    if len(sys.argv) == 0:
        # from Ingredient import Ingredient
        # Ingredient('2.00 ounces shredded extra-sharp white Cheddar cheese')
        main()
        print('\nBREAKPOINT HERE')
    elif sys.argv[1].startswith("https://www.allrecipes.com"):
        url = sys.argv[1]
        rcp = RecipeInfo(url)
        print("We received your recipe!")
        askForTransformation()
    else:
        print("Welcome. Please enter an AllRecipes url for us to parse.")
        url = input()
        rcp = RecipeInfo(url)
        print("Got it!")
        askForTransformation()
