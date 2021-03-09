import spacy
import en_core_web_sm
import pandas as pd
nlp = spacy.load("en_core_web_sm")
from helpers import *

class Tool():
    def __init__(self, step):
        self.step = step
        self.tools = []

        self.addTools()

    def addTools(self):
        # board: likely combined with cutting or chopping
        # poacher, separator: likely combined with egg
        # pestle: likely combined with "mortar and"
        # pin: likely with rolling
        # substitute scoop with scooper
        decomposed_step = nlp(self.step)  # decompose the step with spacy

        def in_tools(token_text):
            lowercase_text = token_text.lower()
            if lowercase_text in TOOLS:
                if lowercase_text == 'board':
                    return "chopping or cutting board"
                if lowercase_text == 'poacher' or lowercase_text == 'separator':
                    return "egg " + lowercase_text
                if lowercase_text == 'pestle':
                    return "mortar and " + lowercase_text
                if lowercase_text == 'pin':
                    return "rolling " + lowercase_text
                if lowercase_text == 'scoop':
                    return "scooper"
                if lowercase_text == 'process' or lowercase_text == 'processor':
                    return "food processor"
                if lowercase_text == 'blend':
                    return "blender"
                if lowercase_text == 'saute':
                    return "frying pan"
                if lowercase_text == "cooker" and "pressure cooker" not in self.tools:
                    return "slow cooker"
                if lowercase_text == 'pressure' or lowercase_text == "cooker" and "slow cooker" not in self.tools:
                    return "pressure cooker"
                else:
                    return lowercase_text

        for token in decomposed_step:  # looping through each token in the step
            # if we find one of the primary cooking methods
            text_to_lower = token.text.lower()
            found_tool = in_tools(text_to_lower)
            if found_tool:
                self.tools.append(found_tool)