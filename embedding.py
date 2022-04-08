import spacy
from enlever_mots_vides import nettoyage_mots_frequent
import numpy as np
def return_word_embedding(sentence):
    # Tokeniser la phrase
    nlp=spacy.load('fr_core_news_sm')
    doc=nlp(sentence)
    # Retourner le vecteur lié à chaque token
    return [(X.vector) for X in doc]
print("vecteur",return_word_embedding("Maman travaille à l'hopital. Elle est infirmière."))