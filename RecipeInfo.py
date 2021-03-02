from fetch_recipe import GetRecipe
from Ingredient import Ingredient
from Method import Method

'''
Helpful documentation:
https://spacy.io/usage/linguistic-features#pos-tagging - for understanding how spacy decomposes text
https://universaldependencies.org/docs/u/pos/ - describes the acronyms used in part-of-speech tagging
https://spacy.io/models/en - lists the different labels that are used with spacy, specifically en_core_web_sm
https://spacy.io/api/top-level#spacy.explain - a spacy function that's helpful for defining labels

'''

class RecipeInfo():
    def __init__(self, url):
        # GetRecipe returns a dictionary with the recipe's
        # name, ingredients, and instructions
        self.rcp = GetRecipe(url)
        self.name = self.rcp['name']

        self.Ingredients = []
        self.Steps = []
        self.Methods = []
        self.Tools = []

        # call function that extracts all important
        # information from the recipe
        self.extractInfo()

    def extractInfo(self):
        '''
        Extract all important information from the recipe,
        update the class fields

        As of 3/1/2021 these are extracted:
        ingredients, steps (in general, not broken down into methods or tools)

        :return: None
        '''

        for full_ingredient in self.rcp['ingredients']:
            # The Ingredient class in Ingredient.py does all of the extraction
            try:
                self.Ingredients.append(Ingredient(full_ingredient))
            except:
                print("Ingredient could not be extracted. Skipping...")
                continue
        
        for step_text in self.rcp['instructions']:
            # formatting each instruction then updating the
            # class field
            self.extractSteps(step_text)

        # extract methods and tools from each step
        for step in self.Steps:
            self.extractMethods(step)
            self.extractTools(step)

    def extractSteps(self, step_text):
        sub_steps = step_text.split('.')
        for stp in sub_steps:
            stp = stp.strip()  # removing newline characters, empty strings
            if stp: self.Steps.append(stp)

    def extractMethods(self, step):
        # the Method class in Method.py does all of the extraction
        pass#self.Methods.append(Method(step))

    def extractTools(self, step):
        pass
        
    def __repr__(self):
        return f"{self.name}"
