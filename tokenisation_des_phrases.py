import spacy
from nltk import sent_tokenize
nlp=spacy.load('fr_core_news_sm')
def tokenisation_des_phrases(sentence):
    phrase=sent_tokenize(sentence)
    return phrase
    
#Aprés tokenistaion des phrase
def tokenise_mot(texte):
    phrases_obtenues=tokenisation_des_phrases(texte)
    m=len(phrases_obtenues)
    for j in range(m):
        doc1=nlp(phrases_obtenues[j])
        return [token.text for token in doc1]
