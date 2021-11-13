import random, json, pickle, nltk
import numpy as np

from nltk.stem import WordNetLemmatizer as wnl     
from tensorflow.keras.models import Sequential as seq
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD as sgd

lem = wnl()
intents = json.loads(open("intents.json").read())

words = []
classes = []
docs = []
ignored_letters = ["?","!",".",","]


for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        docs.append((word_list,intent["tag"]))
        if intent["tag"] not in classes:
            classes.append(intent["tag"])


print(docs)
