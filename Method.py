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
        self.methods = []

        self.getMethods()
    def __str__(self):
        return (
            ",".join([method for method in self.methods])
        )

    def addTool(self, tool):
        self.append(tool)

    def getMethods(self):

        # list of primary cooking methods
        lst_of_methods = ['bake', 'fry', 'roast', 'grill', 'steam',
                           'poach', 'simmer', 'boil', 'blanch', 'braise',
                           'stew', 'broil', 'fold', 'fillet', 'baste', 'cure',
                           'season', 'heat', 'preheat']

        def in_methods(token_text):
            return token_text.lower() in lst_of_methods

        # common way to search for a method in a recipe instruction/step:
        # check if the token is the root of the sentence or
        # is a compound phrase, and occurs at the 0th index


        # def get_secondary_methods(token, index_in_step):
        #    return ((token.dep_ == 'compound' or token.dep_ == "ROOT")
        #            or (token.dep_ == 'ROOT' and token.tag_ == "VB"))\
        #            and index_in_step == 0

        decomposed_step = nlp(self.step)  # decompose the step with spacy

        for token in decomposed_step:  # looping through each token in the step
            # if we find one of the primary cooking methods
            if in_methods(token.text):
                self.methods.append(token.text)

    def __repr__(self):
        return self.methods[0]
