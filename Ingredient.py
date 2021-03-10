from DecomposedText import DecomposedText
from helpers import *
from tabulate import tabulate
import re


class Ingredient():
    def __init__(self, str="", name="", measurement=None, quantity=None, descriptors=[], preparation=[]):
        if str != "":
            self.str = cleanIngredientText(str)
            self.name = ""
            self.doc = DecomposedText(self.str)
            self.measurement = None
            self.quantity = None
            self.descriptors = []
            self.preparation = []
            self.extractProperties(self.str)
        else:
            self.name = name
            self.measurement = measurement
            self.quantity = quantity
            self.descriptors = descriptors
            self.preparation = preparation


    def __str__(self):
        return(
            "Name: "+ self.name +
            "\tQuantity: " + str(self.quantity)+
            "\tMeasurement: " + self.measurement +
            (("\tDescriptors: "+
            self.descriptors) if self.descriptors else "")
            +
            (("\tPreparation:"+
            self.preparation) if self.preparation else "")
        )

    def extractProperties(self, str):
        # # Extract quantity
        self.quantity = float(self.doc.text[0]) if self.doc.pos[0] == 'NUM' else None

        # Extract measurement
        # self.measurement = self.doc.text[1] if self.doc.text[1] == self.doc.parent[0].text else None
        # self.measurement = self.doc.text[1] if self.doc.doc[1].ent_type_ == 'QUANTITY' and self.doc.doc[1].pos_ == 'NOUN' else self.measurement
        self.measurement = self.doc.text[1] if len(self.doc.text) > 1 and containsAnyOf(self.doc.text[1], MEASURES) else self.measurement
        self.measurement = nextToken(self.doc.getToken(")")).text if len(self.doc.text) > 1 and self.doc.doc[1].tag_ == '-LRB-' and containsAnyOf(nextToken(self.doc.getToken(")")).text, MEASURES) else self.measurement
            

        root = self.doc.getRoot()

        # # Extract ingredient name

        # Check if it's a common ingredient
        for ing in COMMON_INGREDIENTS:
            if ing in self.str:
                self.name = ing

        # If the root is not a noun, check its children for nouns
        if not self.name and root.pos_ != 'NOUN' or root.text == self.measurement:
            for child in root.children:
                if child.pos_ == 'NOUN' and child.text != self.measurement and child.i > root.i:
                    root = child
                    break
        
        if not self.name and root.pos_ == 'VERB' and previousToken(root).pos_ == 'PUNCT' and previousToken(previousToken(root)).pos_ == 'NOUN':
            root = previousToken(previousToken(root))

        # Get all neighboring nouns to build up ingredient name
        if not self.name and root.pos_ != 'NOUN' and self.measurement != None:
            if not nextToken(self.doc.getToken(self.measurement)): pass
            elif nextToken(self.doc.getToken(self.measurement)).pos_ in ['NOUN', 'PROPN']:
                root = nextToken(self.doc.getToken(self.measurement))
            elif nextToken(self.doc.getToken(self.measurement)).head.pos_ in ['NOUN', 'PROPN']:
                root = nextToken(self.doc.getToken(self.measurement)).head

        # Check if ingredient name has a color in its name
        if not self.name:
            possible_color = previousToken(root).text + " " if previousToken(root) and previousToken(root).text in COLORS else ""
            self.name = precedingWords(root, restrictions=[self.measurement]) + possible_color + root.text + proceedingWords(root)
        else:
            split = re.split(" |-", self.name)
            root = self.doc.getToken(split[0])
            end = self.doc.getToken(split[-1])
            possible_color = previousToken(root).text + " " if previousToken(root) and previousToken(root).text in COLORS else "" 
            self.name = precedingWords(root, restrictions=[self.measurement]) + possible_color + self.name + proceedingWords(end)

        # # Extract descriptors
        descriptors = []

        for desc in COMMON_DESCRIPTORS:
            if desc in self.str:
                descriptors.append(desc)

        for token in self.doc.doc:
            if token.text == self.measurement: continue
            if (tokenHasProperties(token, "ADJ", "JJ", "amod") and token.head.text in self.name) or\
                    (tokenHasProperties(token, "NOUN", "NN", "nmod") and token.head.text in self.name):
                desc = token.text
                if (tokenHasProperties(previousToken(token), "ADV", "RB", "advmod")):
                    desc = previousToken(token).text + " " + desc
                if self.doc.getTextFromNouns(desc):
                    if self.doc.getTextFromNouns(desc) in descriptors: continue
                    desc = self.doc.getTextFromNouns(desc)

                if desc not in descriptors: descriptors.append(desc)
            if (tokenHasProperties(token, "DET", "DT", "det")) and \
                nextToken(token).tag_ == "HYPH" and nextToken(nextToken(token)).pos_ == "NOUN":
                descriptors.append(self.doc.getTextFromNouns(nextToken(nextToken(token)).text))

        # # Extract preparation
        preparations = []

        for prep in COMMON_PREPARATIONS:
            if prep in self.str:
                preparations.append(prep)

        for token in self.doc.doc:
            if token.text == self.measurement:
                continue

            nameInChild = tokenHasProperties(token, child=self.name)
            if (tokenHasProperties(token, "VERB", "VBN", "amod") and True) or\
                    (tokenHasProperties(token, "VERB", "VBD", "acl") and True) or\
                        (tokenHasProperties(token, "VERB", "VBD", "ROOT") and True) or\
                            (tokenHasProperties(token, "VERB", "VBN", "acl") and True):
                prep = token.text
                if (tokenHasProperties(previousToken(token), "ADV", "RB", "advmod")):
                    prep = previousToken(token).text + " " + prep

                if prep and prep not in preparations: preparations.append(prep)

        
        # Store the final definitions 
        self.preparation = ', '.join(preparations)
        self.descriptors = ', '.join([desc for desc in descriptors if desc not in preparations])

        # Remove descriptors and preparations from name
        for desc in COMMON_DESCRIPTORS:
            self.name = self.name.replace(desc, "").strip()
        for prep in COMMON_PREPARATIONS:
            self.name = self.name.replace(prep, "").strip()

    def __repr__(self):
        return f"{self.name}"
