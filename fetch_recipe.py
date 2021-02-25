import sys
import json
import re
import urllib.request  # for fetching the html content of a url
# documentation: https://docs.python.org/3/howto/urllib2.html

from bs4 import BeautifulSoup  # for parsing the html content
# documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

'''
Parser Must Recognize:
    Ingredients
          Ingredient name
          Quantity
          Measurement (cup, teaspoon, pinch, etc.)
          (optional) Descriptor (e.g. fresh, extra-virgin)
          (optional) Preparation (e.g. finely chopped)
      Tools – pans, graters, whisks, etc.
      Methods
        Primary cooking method (e.g. sauté, broil, boil, poach, etc.)
        (optional) Other cooking methods used (e.g. chop, grate, stir, shake, mince, crush, squeeze, etc.)
    Steps – parse the directions into a series of steps that each consist of ingredients, tools, methods, and time
'''

def get_ingred_and_instr(url):
    '''
    This function fetches html doc/content from the recipe url.
    It then uses BeautifulSoup to extract a JSON object that
    contains the recipe ingredients and instructions
    :param url: url of recipe to fetch
    :return: a JSON object containing the recipe ingredients and instructions
    '''
    fetch_response = urllib.request.urlopen(url)

    html_doc = (fetch_response.read()).decode("utf-8")  # we use decode here because .read() returns bytes

    html_doc_parser = BeautifulSoup(html_doc, 'html.parser')
    # returns a BeautifulSoup object that we can then use functions like
    # find_all(tag name here), get_text(), etc
    # documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#navigating-the-tree

    recipe_json_as_tag = html_doc_parser.find_all('script')[0]
    # extracts the json information from the HTML content,
    # which contains the recipe ingredients and cooking directions

    recipe_json_as_str = (recipe_json_as_tag.contents[0].replace("\n", ""))
    # contents returns a list of strings, in which the 0th element
    # is the entire json content, the 1st element is the JavaScript code
    # newlines are replaced to aid the conversion of this string into a json object

    recipe_json_array_as_str = re.sub("^<.script", '', recipe_json_as_str)
    # uses regex to get rid of the <script ... > tags with empty strings

    recipe_json = json.loads(recipe_json_array_as_str)
    # converts the json array into a json object

    recipe_ingredients = recipe_json[1]["recipeIngredient"]
    # recipe_json is a list of two dictionaries
    recipe_instructions = recipe_json[1]["recipeInstructions"]

    recipe_info = dict()
    # dictionary to store the ingredients and instructions
    recipe_info["ingredients"] = recipe_ingredients
    recipe_info["instructions"] = recipe_instructions

    # uncomment this line to visually see the final json object
    # from: https://www.journaldev.com/33302/python-pretty-print-json
    # print(json.dumps(recipe_json, indent=2))

    return recipe_info

if __name__ == "__main__":
    lst_of_urls = ["https://www.allrecipes.com/recipe/279984/air-fryer-sweet-and-spicy-roasted-carrots/",
                   "https://www.allrecipes.com/recipe/18344/cheese-and-bacon-potato-rounds/",
                   "https://www.allrecipes.com/recipe/230695/cheddar-bacon-ranch-pulls/",
                   "https://www.allrecipes.com/recipe/21061/bacon-and-cheddar-stuffed-mushrooms/",
                   "https://www.allrecipes.com/recipe/81038/worlds-best-bacon-cheese-dip/",
                   "https://www.allrecipes.com/recipe/23947/bacon-crackers/",
                   "https://www.allrecipes.com/recipe/246256/bacon-jalapeno-popper-puffs/",
                   "https://www.allrecipes.com/recipe/230646/bacon-wrapped-tater-tots/",
                   "https://www.allrecipes.com/recipe/69919/bacon-wrapped-smokies/",
                   "https://www.allrecipes.com/recipe/69084/bacon-cheddar-deviled-eggs/",
                   "https://www.allrecipes.com/recipe/240583/cheesy-ham-and-corn-chowder/",
                   "https://www.allrecipes.com/recipe/245774/bucatini-allamatriciana/",
                   "https://www.allrecipes.com/recipe/262225/instant-pot-baby-back-ribs/",
                   "https://www.allrecipes.com/recipe/14746/mushroom-pork-chops/",
                   "https://www.allrecipes.com/recipe/139603/slow-cooker-carnitas/",
                   "https://www.allrecipes.com/recipe/237501/spam-fries-with-spicy-garlic-sriracha-dipping-sauce/",
                   "https://www.allrecipes.com/recipe/247371/pork-loin-roast-with-baby-bellas/",
                   "https://www.allrecipes.com/recipe/261472/easy-maple-bacon-monkey-bread/",
                   "https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/",
                   "https://www.allrecipes.com/recipe/92462/slow-cooker-texas-pulled-pork/",
                   "https://www.allrecipes.com/recipe/10656/irish-soda-bread-cookies/",
                   "https://www.allrecipes.com/recipe/278882/triple-chocolate-chunk-cookies/",
                   "https://www.allrecipes.com/recipe/15324/ginger-touched-oatmeal-peanut-butter-cookies/",
                   "https://www.allrecipes.com/recipe/246328/french-macarons/",
                   "https://www.allrecipes.com/recipe/277919/salted-chocolate-cookies/",
                   "https://www.allrecipes.com/recipe/261865/gluten-free-magic-cookie-bars/",
                   "https://www.allrecipes.com/recipe/278832/italian-cookies-with-anise/",
                   "https://www.allrecipes.com/recipe/10118/rainbow-cookies/",
                   "https://www.allrecipes.com/recipe/242366/easy-chewy-flourless-peanut-butter-cookies/",
                   "https://www.allrecipes.com/recipe/260575/chef-johns-almond-biscotti/",
                   "https://www.allrecipes.com/recipe/10661/oatmeal-peanut-butter-bars/",
                   "https://www.allrecipes.com/recipe/166081/deep-fried-oreos/",
                   "https://www.allrecipes.com/recipe/277700/instant-pot-filipino-chicken-adobo/",
                   "https://www.allrecipes.com/recipe/281604/simple-instant-pot-mashed-potatoes/",
                   "https://www.allrecipes.com/recipe/276655/instant-pot-sweet-and-sour-pork/",
                   "https://www.allrecipes.com/recipe/276654/instant-pot-loaded-baked-potato-soup/",
                   "https://www.allrecipes.com/recipe/273522/instant-pot-green-chili-chicken-and-rice/",
                   "https://www.allrecipes.com/recipe/274921/instant-pot-crispy-chicken-carnitas/",
                   "https://www.allrecipes.com/recipe/269030/instant-pot-yankee-pot-roast/",
                   "https://www.allrecipes.com/recipe/267986/instant-pot-pan-juice-gravy/",
                   "https://www.allrecipes.com/recipe/268026/instant-pot-corned-beef/",
                   "https://www.allrecipes.com/recipe/258468/beef-stroganoff-for-instant-pot/",
                   "https://www.allrecipes.com/recipe/220869/easy-pressure-cooker-pot-roast/",
                   "https://www.allrecipes.com/recipe/261498/instant-pot-garlic-roasted-potatoes/",
                   "https://www.allrecipes.com/recipe/263876/best-instant-pot-scalloped-potatoes/",
                   "https://www.allrecipes.com/recipe/280269/instant-pot-potato-salad/",
                   "https://www.allrecipes.com/recipe/261394/instant-pot-mashed-potatoes/",
                   "https://www.allrecipes.com/recipe/269144/instant-pot-sweet-potato-casserole/",
                   "https://www.allrecipes.com/recipe/279426/instant-pot-bangers-and-mash/",
                   "https://www.allrecipes.com/recipe/280718/instant-pot-broccolini-and-potato-salad/"]

    print(len(lst_of_urls))

    for url in lst_of_urls:
        assert get_ingred_and_instr(url) is not None

    # uncomment this line to run the file via command line
    # fetch_to_parse(sys.argv[1]) # where argv[1] is a url
