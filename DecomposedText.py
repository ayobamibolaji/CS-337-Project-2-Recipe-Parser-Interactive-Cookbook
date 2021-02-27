import spacy
import en_core_web_sm
import pandas as pd
nlp = spacy.load("en_core_web_sm")

# Text decomposer: Creates an object that allows one to access the tokenized form of a texxt along with its
# part-of-speech tagging, lemmas, and relations to other words.
class DecomposedText():
    def __init__(self, text):
        self.full_text = text
        self.doc = nlp(text)
        self.text = []
        self.lemma = []
        self.pos = []
        self.tag = []
        self.dep = []
        self.parent = []
        self.children = []
        self.nouns = []

        for token in self.doc:
            self.text.append(token.text)
            self.lemma.append(token.lemma_)
            self.pos.append(token.pos_)
            self.tag.append(token.tag_)
            self.dep.append(token.dep_)
            self.parent.append(token.head)
            self.children.append([child for child in token.children])

        self.nouns = [chunk for chunk in self.doc.noun_chunks]

    def show(self):
        print(pd.DataFrame({'Text': self.text, 'Lemma': self.lemma, 'Pos': self.pos, 'Tag':self.tag, 'Dep':self.dep, 'Parent': self.parent, 'Children': self.children}))
        print(self.nouns)

    def getRoot(self):
        for token in self.doc:
            if token.dep_ == 'ROOT':
                return token

    def getToken(self, str):
        for token in self.doc:
            if token.text == str:
                return token

