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
        self.tools = []

        self.getMethods()

    def addTool(self, tool):
        self.append(tool)

    def getMethods(self):

        # common way to search for a method in a recipe instruction/step:
        # check if the token
        # is the root of the sentence and is a verb
        def rule_one(token):
            return token.dep_ == "ROOT" and token.tag_ == "VB"

        # common way to search for a method in a recipe instruction/step:
        # check if the token is the root of the sentence or
        # is a compound phrase, and occurs at the 0th index
        def rule_two(token, index_in_step):
            return token.dep_ == 'compound' or token.dep_ == "ROOT" and index_in_step == 0

        # not so common way to search for a method in a recipe instruction/step:
        # check if you have a situation like "air fry" or "stir fry"
        # where the first two tokens have the same head and one of them
        # is the root of the sentence
        def rule_three(decomposed_step):
            token_0 = decomposed_step[0]
            token_1 = decomposed_step[1]

            # check for a common method: 'place'
            if token_0.text == "Place":
                return token_0.text

            if token_0.dep_ == "ROOT" or token_1.dep_ == "ROOT" and token_0.head == token_1.head:
                if token_0.tag_ == "NN" and token_1.tag_ == "NN":
                    return token_0.text + " " + token_1.text

            return False

        decomposed_step = nlp(self.step)  # decompose the step with spacy


        if rule_three(decomposed_step):
            self.methods.append(rule_three(decomposed_step))
        else:
            for index, token in enumerate(decomposed_step):  # looping through each token in the step

                if index == 0:  # do this check since rule_two operates on the 0th token
                    if rule_one(token) or rule_two(token, 0):
                        self.methods.append(token.text)
                else:
                    if rule_one(token):
                        self.methods.append(token.text)



                # Extracting data from each token in the recipe step/instruction
                # for testing
                #info_list = [token.text, (token.dep_), (spacy.explain(token.tag_), token.tag_), (token.head)]
                #self.methods.append(info_list)
