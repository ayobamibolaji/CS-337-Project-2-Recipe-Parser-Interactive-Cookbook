from fetch_recipe import GetRecipe
from Ingredient import Ingredient
from Method import Method
from helpers import MEAT_SUBSTITUTES, VEGGIE_SUBSTITUTES, HEALTHY_SUBSTITUTES, UNHEALTHY_SUBSTITUTES
import re
from tabulate import tabulate

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

    def __str__(self):
        return (
            "Name: " +
            self.name
            + "\n\nIngredients:\n" +
            "\n"+
            tabulate([[ing.quantity,
                       ing.measurement,
                       ing.name,
                       ing.descriptors,
                       ing.preparation] for ing in self.Ingredients],
                     headers=['Quantity', "Measurement", 'Name', "Descriptors", "Preparation"])
            + "\n\nSteps:\n" +
            "\n".join([str(step) for step in self.Steps])
            + "\n\nMethods:\n" +
            ", ".join([str(method) for method in self.Methods])
            + "\n\nTools:\n" +
            ", ".join([str(tool) for tool in self.Tools])
        )

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

    def transformQuantities(self, factor):
        for ing in self.Ingredients:
            ing.quantity *= factor

    def transformIngredient(self, old: str, new, oldToNewRatio, condition):
        # see if the ingredient is in the recipe
        for ing in self.Ingredients:
            if condition(ing):
                if isinstance(new, str):
                    ing.name = new
                    ing.quantity = ing.quantity * oldToNewRatio
                else:
                    ing.name = new.name
                    ing.doc = new.doc
                    ing.measurement = new.measurement
                    ing.quantity = ing.quantity * oldToNewRatio
                    ing.descriptors = new.descriptors
                    ing.preparation = new.preparation
        # regex replace the ingredient name in the steps.
        for idx, step in enumerate(self.Steps):
            pattern = re.compile(old, re.IGNORECASE)
            if isinstance(new, str):
                self.Steps[idx] = pattern.sub(new, step)
            else:
                self.Steps[idx] = pattern.sub(new.name, step)

    def healthify(self):
        # Mark the title as healthy
        self.name = "Healthy " + self.name
        for unhealthy_ing, healthy_alt in UNHEALTHY_SUBSTITUTES.items():
            self.transformIngredient(unhealthy_ing, healthy_alt[0], healthy_alt[1], (lambda ing: unhealthy_ing in ing.name))

    def unHealthify(self):
        for unhealthy_ing, healthy_alt in UNHEALTHY_SUBSTITUTES.items():
            self.transformIngredient(unhealthy_ing, healthy_alt[0], healthy_alt[1], (lambda ing: unhealthy_ing in ing.name))
    
        # Maybe add a conditional for this next step lol
        self.Ingredients.append(Ingredient("1 can Coca Cola"))
        self.Steps.append("Enjoy the meal alongside an ice cold Coca Cola.")

    def makeVegetarian(self):
        # Mark the title as vegetarian
        self.name = "Vegetarian " + self.name
        for meat_ing, meat_alt in MEAT_SUBSTITUTES.items():
            self.transformIngredient(meat_ing, meat_alt, 1, (lambda ing: meat_ing in ing.name))

    def makeUnVegetarian(self):
        self.name = "Un-Vegetarian " + self.name
        for veggie_ing, veggie_alt in VEGGIE_SUBSTITUTES.items():
            self.transformIngredient(veggie_ing, veggie_alt, 1, (lambda ing: veggie_ing in ing.name))
        
        # Maybe add a conditional for this next step lol
        self.Ingredients.append(Ingredient(".5 cups bacon strips"))
        self.Steps.append("Sprinkle bacon strips on top of final dish.")
        
    def __repr__(self):
        return f"{self.name}"
