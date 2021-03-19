import gensim
from gensim import models
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from model_download import downloadModel

downloadModel()

print("Loading NLP model...")
model = gensim.models.KeyedVectors.load_word2vec_format(
    'GoogleNews-vectors-negative300.bin.gz', binary=True, limit=500000)
print("Finished loading NLP model.")

# Because of circular imports, I have to just copy the commands dictionary here... Whoop-dee-doo
commands_lst = [
    "walk through a recipe",
    "go over ingredients list",
    "go over steps",
    # "go over list of tools",
    # "go over list of methods",
    # "what ingredients are used in this step",
    # "what tools are used in this step",
    # "what methods are used in this step",
    "yes",
    "no",
    "go to the previous step",
    "go to the next step",
    "go back NUMBER steps",
    "go forward NUMBER steps",
    "take me to the NUMBER step",
    "take me to step NUMBER",
    # "how do i do that",
    # "how do i QUERY",
    "that will be all",
    "goodbye"
]

# Just a few synonyms to help the NLP model out a bit
word_replacements = {
    "sure": "yes",
    "nah": "no",
    "nope": "no",
    "goodbye": "bye",
    "skip": "go forward",
    "that's all": "that will be all",
    "show me": "go over",
}


def cleanStr(str):
    for word, repl in word_replacements.items():
        str = str.replace(word, repl)
    return str.lower()


def forceVectorize(word):
    vec = np.zeros((300,))
    for i, char in enumerate(word):
        vec[i] = (ord(char)/256 - 0.5)
    return vec


def vectorize(str):
    str = cleanStr(str)
    return sum([model[word] if word in model.vocab else forceVectorize(word) for word in str.split()]).reshape(1, -1)


def mostSimilar(str, lstOfStr):
    mostSim = None
    bestScore = 0

    vectorizedStr = vectorize(str)

    for aStr in lstOfStr:
        score = cosine_similarity(vectorizedStr, vectorize(aStr))
        if score > bestScore:
            bestScore = score[0][0]
            mostSim = aStr
    # print((mostSim, bestScore))
    return (mostSim, bestScore) if bestScore > .5 else (str, 0)

