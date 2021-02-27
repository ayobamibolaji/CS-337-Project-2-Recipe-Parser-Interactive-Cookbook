from DecomposedText import DecomposedText
from helpers import *

class Ingredient():
    def __init__(self, str):
        self.str = cleanIngredientText(str)
        self.name = ""
        self.doc = DecomposedText(self.str)
        self.measurement = None
        self.quantity = None
        self.descriptor = None
        self.preparation = None

        self.extractProperties(self.str)

    def extractProperties(self, str):
        # Extract quantity
        self.quantity = float(self.doc.text[0]) if self.doc.pos[0] == 'NUM' else None

        # Extract measurement
        self.measurement = self.doc.text[1] if self.doc.text[1] == self.doc.parent[0].text else None
        self.measurement = self.doc.text[1] if self.doc.doc[1].ent_type_ == 'QUANTITY' else self.measurement
        self.measurement = self.doc.text[1] if containsAnyOf(self.doc.text[1], measures) else self.measurement
            

        root = self.doc.getRoot()

        # Extract ingredient name
        if root.pos_ != 'NOUN' or root.text == self.measurement:
            for child in root.children:
                if child.pos_ == 'NOUN' and child.text != self.measurement:
                    root = child
                    break
        
        if root.pos_ != 'NOUN' and self.measurement != None:
            if nextToken(self.doc.getToken(self.measurement)).pos_ == 'NOUN':
                root = nextToken(self.doc.getToken(self.measurement))

        self.name = precedingWords(root, restrictions=[self.measurement]) + root.text + proceedingWords(root)

