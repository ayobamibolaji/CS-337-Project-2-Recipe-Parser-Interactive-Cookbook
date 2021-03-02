import os.path
from os import path
import json
import urllib.request
from bs4 import BeautifulSoup
from RecipeInfo import RecipeInfo
from helpers import lst_of_urls
from collections import OrderedDict


def loadIngredientsDict():
    if path.exists("IngredientsDict.json"):
        return json.load(open("IngredientsDict.json", "r"))
    else:
        return {}

def saveIngredientsDict():
    out_file = open("IngredientsDict.json", "w")
    json.dump(ID, out_file)


ID = loadIngredientsDict()

def addIngredient(name, properties=[]):
    if name not in ID:
        ID[name] = {
            'tally': 1
        }
    else:
        ID[name]['tally'] += 1
        
    for property in properties:
        if property not in ID[name]:
            ID[name][property] = 1
        else:
            ID[name][property] += 1
    
    saveIngredientsDict()


def analyzeIngredientsInRecipes(urls_list, properties=[]):
    for i, url in enumerate(urls_list):
        print(f"Analyzed ingredients in {i+1}/{len(urls_list)} urls.", end='\r')
        rcp = RecipeInfo(url)
        for ing in rcp.Ingredients:
            addIngredient(ing.name, properties)
    print("\nFinished analyzing urls.")


def getListOfRecipeUrls(main_url, numPages, startingPage=1):
    startingPage = startingPage - 1
    recipe_urls = []
    for page in range(numPages):
        print(f"Fetched recipe urls from {page+1}/{numPages} pages.", end='\r')
        try:
            fetch_response = urllib.request.urlopen(main_url + f"?page={2 + startingPage + page}")
            html_doc = (fetch_response.read()).decode("utf-8")
            parser = BeautifulSoup(html_doc, 'html.parser')
            for imageLink in parser.find_all("a", {"class":"tout__imageLink"}):
                if "/recipe/" in imageLink.attrs['href']:
                    recipe_urls.append("https://www.allrecipes.com" + imageLink.attrs['href'])
        except:
            print("\nInvalid url. Continuing...")
            continue
    
    print("\nFinished fetching recipe urls.")
    print(f"Ending page: {startingPage + numPages}")
    return recipe_urls

def filterDictBy(a_dict, included_properties, excluded_properties=[]):
    main_set = set(['tally'] + included_properties)
    return { ing:val for ing,val in OrderedDict(a_dict).items() if main_set.issubset(set(a_dict[ing].keys())) and (exc not in a_dict[ing].keys() for exc in excluded_properties) }

def sortDictBy(sub_dict, property):
    return OrderedDict(sorted(sub_dict.items(), key=lambda x: (x[1][property]**1.3)/(x[1]['tally']), reverse=True))

def filterAndSortDictBy(a_dict, property):
    return sortDictBy(filterDictBy(a_dict, [property]), property)

print('wow')

# import time
# start = time.time()

# To continue getting more recipes from a certain category, change the starting page to the end page so far + 1
# I.e., if a category has scanned 8 pages of reipes so far and you want to scan 3 more, the new starting page would
# be 9. Make sure to update the new ending page to be the new starting page + number of pages scanned.

# # End page so far: 8
# asian_rcps = getListOfRecipeUrls("https://www.allrecipes.com/recipes/227/world-cuisine/asian/", 8, 1)
# analyzeIngredientsInRecipes(asian_rcps, ['asian'])

# # End page so far: 8
# italian_rcps = getListOfRecipeUrls("https://www.allrecipes.com/recipes/723/world-cuisine/european/italian/", 8, 1)
# analyzeIngredientsInRecipes(italian_rcps, ['italian'])

# # End page so far: 8
# veg_rcps = getListOfRecipeUrls("https://www.allrecipes.com/recipes/87/everyday-cooking/vegetarian/", 8, 1)
# analyzeIngredientsInRecipes(veg_rcps, ['vegetarian'])

# # End page so far: 8
# seafood_rcps = getListOfRecipeUrls("https://www.allrecipes.com/recipes/93/seafood/", 8, 1)
# analyzeIngredientsInRecipes(seafood_rcps, ['seafood'])


# # End page so far: 8
# meat_rcps = getListOfRecipeUrls("https://www.allrecipes.com/recipes/92/meat-and-poultry/", 8, 1)
# analyzeIngredientsInRecipes(meat_rcps, ['meat'])

# # End page so far: 8
# healthy_rcps = getListOfRecipeUrls("https://www.allrecipes.com/recipes/84/healthy-recipes/", 8, 1)
# analyzeIngredientsInRecipes(healthy_rcps, ['healthy'])

# # End page so far: 8
# mexican_rcps = getListOfRecipeUrls("https://www.allrecipes.com/recipes/728/world-cuisine/latin-american/mexican/", 8, 1)
# analyzeIngredientsInRecipes(mexican_rcps, ['mexican'])


# print(f"Total extraction took {time.time() - start} seconds.")
# print(f"Each category takes about {(time.time() - start)/7} seconds on average.")
