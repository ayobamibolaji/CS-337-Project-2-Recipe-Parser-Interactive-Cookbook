import spacy
import en_core_web_sm
import pandas as pd
nlp = spacy.load("en_core_web_sm")
from helpers import *

'''
Helpful documentation:
https://spacy.io/usage/linguistic-features#pos-tagging - for understanding how spacy decomposes text
https://universaldependencies.org/docs/u/pos/ - describes the acronyms used in part-of-speech tagging
https://spacy.io/models/en - lists the different labels that are used with spacy, specifically en_core_web_sm
https://spacy.io/api/top-level#spacy.explain - a spacy function that's helpful for defining labels
'''

class Method():
    '''
    Methods
        Primary cooking method (e.g. sauté, broil, boil, poach, etc.)
        (optional) Other cooking methods used (e.g. chop, grate, stir, shake, mince, crush, squeeze, etc.)
    '''

    # accepts a recipe instruction/step as input
    def __init__(self, step):
        self.step = step
        self.primary_methods = []
        self.secondary_methods = []

        self.getMethods()
    def __str__(self):
        return (
            ",".join([method for method in self.methods])
        )

    def addTool(self, tool):
        self.append(tool)

    def getMethods(self):

        # dict of primary cooking methods
        # 1 - primary
        # 2 - secondary
        dict_of_methods = {
            'bake': 1,
            'whisk': 2,
            'fry': 1,
            'roast': 1,
            'grill': 1,
            'steam': 1,
            'poach': 2,
            'simmer': 2,
            'boil': 1,
            'blanch': 2,
            'braise': 2,
            'stew': 2,
            'broil': 2,
            'fold': 2,
            'fillet': 2,
            'baste': 2,
            'cure': 2,
            'season': 1,
            'heat': 1,
            'preheat': 1,
            'stir': 1,
            'mix': 1,
            'whisking': 2,
            'stirring': 1,
            'broiling': 2,
            'boiling': 1,
            'simmering': 2,
            'frying': 1,
            'mixing': 1,
            'rub': 2,
            'bring': 2,
            'place': 2,
            'use': 2,
            'remove': 2,
            'add': 2,
            'combine': 2,
            'continue': 2,
            'slip': 2,
            'set': 2,
            'return': 2,
            'serve': 2,
            'transfer': 2,
            'take': 2,
            'save': 2,
        }

        def in_methods(token_text):
            lowercase_text = token_text.lower()
            if lowercase_text == "whisking":
                return "whisk"
            if lowercase_text == "boiling":
                return "boil"
            if lowercase_text == "simmering":
                return "simmer"
            if lowercase_text == "stirring":
                return "stir"
            if lowercase_text == "mixing":
                return "mix"
            if lowercase_text == "frying":
                return "fry"
            else:
                if lowercase_text in dict_of_methods:
                    return lowercase_text
            return None

        # common way to search for a method in a recipe instruction/step:
        # check if the token is the root of the sentence or
        # is a compound phrase, and occurs at the 0th index


        # def get_secondary_methods(token, index_in_step):
        #    return ((token.dep_ == 'compound' or token.dep_ == "ROOT")
        #            or (token.dep_ == 'ROOT' and token.tag_ == "VB"))\
        #            and index_in_step == 0

        decomposed_step = nlp(self.step)  # decompose the step with spacy

        if "deep fry" in self.step:
            self.primary_methods.append("deep fry")
        if "air fry" in self.step:
            self.primary_methods.append("air fry")

        for token in decomposed_step:  # looping through each token in the step
            # if we find one of the primary cooking methods
            found_method = in_methods(token.text)
            if found_method:
                if dict_of_methods[found_method] == 1:
                    self.primary_methods.append(found_method)
                else:
                    self.secondary_methods.append(found_method)


    def __repr__(self):
        return self.methods[0]
