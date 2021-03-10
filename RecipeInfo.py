from fetch_recipe import GetRecipe
from Ingredient import Ingredient
from Tool import Tool
from Method import Method
from helpers import MEAT_SUBSTITUTES, VEGGIE_SUBSTITUTES, HEALTHY_SUBSTITUTES, UNHEALTHY_SUBSTITUTES, FATS, ASIAN_SIDES, ASIAN_SPICES, TURKISH_SIDES, TURKISH_SPICES
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
        self.primaryMethods = []
        self.secondaryMethods = []
        self.Tools = []

        # call function that extracts all important
        # information from the recipe
        self.extractInfo()

    def __str__(self):
        return (
                "Name: " +
                self.name
                + "\n\nIngredients:\n" +
                "\n" +
                tabulate([[ing.quantity,
                           ing.measurement,
                           ing.name,
                           ing.descriptors,
                           ing.preparation] for ing in self.Ingredients],
                         headers=['Quantity', "Measurement", 'Name', "Descriptors", "Preparation"])
                + "\n\nSteps:\n" +
                "\n".join([str(step) for step in self.Steps])
                + "\n\nPrimary Methods:\n" +
                ", ".join([str(method) for method in self.primaryMethods])
                + "\n\nSecondary Methods:\n" +
                ", ".join([str(method) for method in self.secondaryMethods])
                + "\n\nTools:\n" +
                ", ".join([str(tool) for tool in self.Tools])
                + "\n"
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
                print(f"Ingredient \"{full_ingredient}\" could not be extracted. Skipping...")
                continue

        for step_text in self.rcp['instructions']:
            # formatting each instruction then updating the
            # class field
            self.extractSteps(step_text)

        # extract methods and tools from each step
        for step in self.Steps:
            self.extractMethods(step)
            self.extractTools(step)

        # these for loops catches some edge cases with
        # the methods and tools
        for method in self.primaryMethods:
            if method == "boil":
                if "pot" not in self.Tools:
                    self.Tools.append('pot')
            if method == "bake":
                if "oven" not in self.Tools:
                    self.Tools.append('oven')

        for tool in self.Tools:
            if tool == "slow cooker":
                if "cook with slow cooker" not in self.primaryMethods:
                    self.primaryMethods.append("cook with slow cooker")
            if tool == "pressure cooker":
                if "cook with pressure cooker" not in self.primaryMethods:
                    self.primaryMethods.append("cook with pressure cooker")

        if 'fry' in self.primaryMethods and "air fry" in self.primaryMethods or "deep fry" in self.primaryMethods:
            # removing duplicate instances of fry like "air fry" and "fry"
            self.primaryMethods[:] = [method for method in self.primaryMethods if method != "fry"]

    def extractSteps(self, step_text):
        sub_steps = step_text.split('.')
        for stp in sub_steps:
            stp = stp.strip()  # removing newline characters, empty strings
            if stp: self.Steps.append(stp)

    def extractMethods(self, step):
        extracted_methods = Method(step)
        primary_methods = extracted_methods.primary_methods
        secondary_methods = extracted_methods.secondary_methods

        for method in primary_methods:
            if method not in self.primaryMethods:
                self.primaryMethods.append(method)

        for method in secondary_methods:
            if method not in self.secondaryMethods:
                self.secondaryMethods.append(method)

    def extractTools(self, step):
        tools = Tool(step).tools

        for tool in tools:
            if tool not in self.Tools:
                self.Tools.append(tool)

    def transformQuantities(self, factor):
        for ing in self.Ingredients:
            if ing.quantity != None: ing.quantity *= factor

    def transformIngredient(self, old: str, new, oldToNewRatio, condition):
        # see if the ingredient is in the recipe
        for ing in self.Ingredients:
            if condition(ing):
                old_name = ing.name.split(" ")
                if isinstance(new, str):
                    ing.name = new
                    if ing.quantity is not None:
                        ing.quantity = ing.quantity * oldToNewRatio
                else:
                    ing.name = new.name
                    ing.measurement = new.measurement if new.measurement else ing.measurement
                    if ing.quantity is not None:
                        ing.quantity = ing.quantity * oldToNewRatio
                    ing.descriptors = new.descriptors
                    ing.preparation = new.preparation
                # regex replace the ingredient name in the steps.
                for idx, step in enumerate(self.Steps):
                    for old_part in old_name:
                        pattern = re.compile(old_part, re.IGNORECASE)
                        if isinstance(new, str):
                            self.Steps[idx] = pattern.sub(new, step)
                        else:
                            self.Steps[idx] = pattern.sub(new.name, step)

    def healthify(self):
        # Mark the title as healthy
        self.name = "Healthy " + self.name
        
        # Replace fats
        for fat in FATS:
            self.transformIngredient(fat, Ingredient(name="oil", descriptors="olive"), 0.5,
                                     (lambda ing: fat in ing.name and "foil" not in ing.name))
        
        # Replace unhealthy ingredients
        for unhealthy_ing, healthy_alt in UNHEALTHY_SUBSTITUTES.items():
            self.transformIngredient(unhealthy_ing, Ingredient(healthy_alt[0]), healthy_alt[1], healthy_alt[2])
        
        self.transformQuantities(.8)

    def unHealthify(self):
        # Mark the title as unhealthy
        self.name = "Unhealthy " + self.name
        for healthy_ing, unhealthy_alt in HEALTHY_SUBSTITUTES.items():
            self.transformIngredient(healthy_ing, unhealthy_alt[0], unhealthy_alt[1],
                                     (lambda ing: healthy_ing in ing.name))
        self.transformIngredient("milk", Ingredient(name="cream"), 1, (lambda ing: "milk" in ing.name and "milk chocolate" not in ing.name))
        self.transformIngredient("olive oil", Ingredient(name="butter"), 1,
                                 (lambda ing: "oil" in ing.name and "olive" in ing.descriptors))

        self.transformQuantities(1.3)

        # Maybe add a conditional for this next step lol
        if 'CocaCola' not in [ing.name for ing in self.Ingredients]:
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
        if 'bacon strips' not in [ing.name for ing in self.Ingredients]:
            self.Ingredients.append(Ingredient(".5 cups bacon strips"))
            self.Steps.append("Sprinkle bacon strips on top of final dish.")

    def makeAsian(self):
        # change name
        self.name = "Asian " + self.name

        # switch out side for jasmine rice
        for side_ing, jasmine in ASIAN_SIDES.items():
            self.transformIngredient(side_ing, jasmine, 1, (lambda ing: side_ing in ing.name))

        # switch out common spices and herbs
        for spice_ing, spice_alt in ASIAN_SPICES.items():
            self.transformIngredient(spice_ing, spice_alt[0], spice_alt[1],spice_alt[2])

        # catch all herb that goes with almost everything in case no common spice is found
        if 'anise seeds' not in [ing.name for ing in self.Ingredients]:
            self.Ingredients.append(Ingredient("1 tablespoon anise seeds"))
            self.Steps.append("When serving, sprinkle Anise seeds generously over the dish")

        # try to stir fry
        if 'fry' in [step for step in self.Steps]:
            self.Ingredients.append(Ingredient("half cup stir fry sauce"))
            self.Steps.append("While frying finishes, whisk stir fry sauce into dish")
            self.name = self.name+'stir fry'


        # add soy sauce
        if 'soy sauce' not in [ing.name for ing in self.Ingredients]:
            self.Ingredients.append(Ingredient("2 teaspoons soy sauce"))
            self.Steps.append("Gently add soy sauce spread evenly across final dish.")

    def makeTurkish(self):
        self.name = "Turkish " + self.name

        # switch out side for bulgur pilaf
        for side_ing, bulgur in TURKISH_SIDES.items():
            self.transformIngredient(side_ing, bulgur, 1, (lambda ing: side_ing in ing.name))

        # switch out common spices and herbs
        for spice_ing, spice_alt in TURKISH_SPICES.items():
            self.transformIngredient(spice_ing, spice_alt, 1, (lambda ing: spice_ing in ing.name))

        ing_set = set([ing.name for ing in self.Ingredients])
        meats_set = set(MEAT_SUBSTITUTES)

        # try to skewer if meat is involved
        if ing_set.intersection(meats_set) and "Give a final grilling for no more than 2 minutes to lightly crisp the meats" not in self.Steps:
            self.Steps.append("When meats are nearly done, thread them onto skewers. Leave 1.5 inches open for handling")
            self.Steps.append("Give a final grilling for no more than 2 minutes to lightly crisp the meats")
            self.name = self.name + ' Kebab'

        # add baharat seasoning as a catch all
        if 'baharat seasoning' not in [ing.name for ing in self.Ingredients]:
            self.Ingredients.append(Ingredient("1 teaspoon baharat seasoning"))
            self.Steps.append("Gently add baharat seasoning evenly across final dish.")

        if '1-5 Metal or Bamboo skewers' not in self.Tools:
            self.Tools.append("1-5 Metal or Bamboo skewers")

    def __repr__(self):
        return f"{self.name}"
