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

def GetRecipe(url):
    '''
    This function fetches html doc/content from the recipe url.
    It then uses BeautifulSoup to extract a JSON object that
    contains the recipe ingredients and instructions

    :param url: (string) url of recipe to fetch
    :return: (dict) a dictionary containing the recipe ingredients and instructions
    '''
    fetch_response = urllib.request.urlopen(url)

    html_doc = (fetch_response.read()).decode("utf-8")  # we use decode here because .read() returns bytes

    html_doc_parser = BeautifulSoup(html_doc, 'html.parser')
    # returns a BeautifulSoup object that we can then use functions like
    # find_all(tag name here), get_text(), etc
    # documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#navigating-the-tree

    recipe_json_as_tag = html_doc_parser.find_all('script')[0]
    # extracts the JavaScript information from the HTML content,
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
    recipe_instructions = [dict['text'] for dict in recipe_json[1]["recipeInstructions"]]
    recipe_name = recipe_json[1]['name']

    recipe_info = dict()
    # dictionary to store the recipe name, ingredients and instructions
    recipe_info["name"] = recipe_name
    recipe_info["ingredients"] = recipe_ingredients
    recipe_info["instructions"] = recipe_instructions




    # uncomment this line to visually see the final json object
    # from: https://www.journaldev.com/33302/python-pretty-print-json
    # print(json.dumps(recipe_json, indent=2))
    return recipe_info

