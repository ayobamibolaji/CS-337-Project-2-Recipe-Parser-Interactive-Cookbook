from DecomposedText import DecomposedText
from helpers import *

class Ingredient():
    def __init__(self, str):
        self.str = cleanIngredientText(str)
        self.name = ""
        self.doc = DecomposedText(self.str)
        self.measurement = None
        self.quantity = None
        self.descriptors = None
        self.preparation = None

        self.extractProperties(self.str)
    def __str__(self):
        return(
            "Name: "+
            self.name +
            "\tQuantity: "+
            str(self.quantity)+
            "\tMeasurement: "+
            self.measurement +
            (("\tDescriptor: "+
            ",".join(self.descriptors)) if self.descriptors else "")
            +
            (("\tPreparation:"+
            self.preparation) if self.preparation else "")
        )

    def extractProperties(self, str):
        # Extract quantity
        self.quantity = float(self.doc.text[0]) if self.doc.pos[0] == 'NUM' else None

        # Extract measurement
        self.measurement = self.doc.text[1] if self.doc.text[1] == self.doc.parent[0].text else None
        self.measurement = self.doc.text[1] if self.doc.doc[1].ent_type_ == 'QUANTITY' and self.doc.doc[1].pos_ == 'NOUN' else self.measurement
        self.measurement = self.doc.text[1] if containsAnyOf(self.doc.text[1], measures) else self.measurement
        self.measurement = nextToken(self.doc.getToken(")")).text if self.doc.doc[1].tag_ == '-LRB-' else self.measurement
            

        root = self.doc.getRoot()

        # Extract ingredient name
        if root.pos_ != 'NOUN' or root.text == self.measurement:
            for child in root.children:
                if child.pos_ == 'NOUN' and child.text != self.measurement and child.i > root.i:
                    root = child
                    break
        
        if root.pos_ != 'NOUN' and self.measurement != None:
            if not nextToken(self.doc.getToken(self.measurement)): pass
            elif nextToken(self.doc.getToken(self.measurement)).pos_ == 'NOUN':
                root = nextToken(self.doc.getToken(self.measurement))
            elif nextToken(self.doc.getToken(self.measurement)).head.pos_ == 'NOUN':
                root = nextToken(self.doc.getToken(self.measurement)).head

        self.name = precedingWords(root, restrictions=[self.measurement]) + root.text + proceedingWords(root)


        # Extract descriptors
        descriptors = []
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
                descriptors.append(desc)
            if (tokenHasProperties(token, "DET", "DT", "det")) and \
                nextToken(token).tag_ == "HYPH" and nextToken(nextToken(token)).pos_ == "NOUN":
                descriptors.append(self.doc.getTextFromNouns(nextToken(nextToken(token)).text))

        self.descriptors = ', '.join(descriptors)

        # Extract preparation
        preparations = []
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
                preparations.append(prep)

        self.preparation = ', '.join(preparations)

    # Try to fix

    def __repr__(self):
        return f"{self.name}"
