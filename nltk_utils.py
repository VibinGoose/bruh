import torch, nltk

from nltk.stem.porter import PorterStemmer as ps

stemmer = ps()

def tokenise(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bagOfWords(tokenSentence, allWords):
    pass


words = ["organize","organizes","organizing"]
stemmed = [stem(w) for w in words]
a = "How long does shipping take?"
print(stemmed)
