from helpers import lst_of_urls
from RecipeInfo import RecipeInfo
import sys

recipes = []
test_ingredients = []

def main():
    for i, url in enumerate(lst_of_urls[:10]):
        print("Checked {}/{} URLs".format(i+1, len(lst_of_urls)), end='\r')
        rcp = RecipeInfo(url)
        recipes.append(rcp)
        for ing in rcp.Ingredients:
            test_ingredients.append(ing)
    


if __name__ == "__main__":
    # from Ingredient import Ingredient
    # Ingredient('2.00 ounces shredded extra-sharp white Cheddar cheese')
    main()
    print('\nBREAKPOINT HERE')
