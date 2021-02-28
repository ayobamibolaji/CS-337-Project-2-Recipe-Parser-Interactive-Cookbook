from fetch_recipe import GetRecipe
from Ingredient import Ingredient


class RecipeInfo():
    def __init__(self, url):
        self.rcp = GetRecipe(url)
        self.name = self.rcp['name']

        self.Ingredients = []
        self.Steps = []
        self.Methods = []
        self.Tools = []

        self.extractInfo()

    def extractInfo(self):
        for full_ingredient in self.rcp['ingredients']:
            self.Ingredients.append(Ingredient(full_ingredient))
        
        for step_text in self.rcp['instructions']:
            self.extractSteps(step_text)

        for step in self.Steps:
            self.extractMethods(step)
            self.extractTools(step)

    def extractSteps(self, step_text):
        sub_steps = step_text.split('.')
        for stp in sub_steps:
            stp = stp.strip()
            if stp: self.Steps.append(stp)

    def extractMethods(self, step):
        pass

    def extractTools(self, step):
        pass
        
    def __repr__(self):
        return f"{self.name}"
