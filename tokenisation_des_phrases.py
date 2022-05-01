import spacy
from nltk import FreqDist
from nltk.corpus import brown
nlp=spacy.load('fr_core_news_sm')
def tokenisation_des_phrases(sentence):
    doc=nlp(sentence)
    return [phrase.text for phrase in doc.sents]

#Aprés tokenistaion des phrase
def tokenise_mot(texte):
    doc1=nlp(texte)
    return [token.text for token in doc1]
 