from helpers import lst_of_urls
from RecipeInfo import RecipeInfo
import sys

recipes = []

def main():
    for i, url in enumerate(lst_of_urls[:2]):
        print("Checked {}/{} URLs".format(i+1, len(lst_of_urls)), end='\r')
        recipes.append(RecipeInfo(url))
    


if __name__ == "__main__":
    main()
    print('\nBREAKPOINT HERE')
