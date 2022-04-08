from nltk.corpus import stopwords
from tokenisation_des_phrases import tokenise_mot,tokenisation_des_phrases
stopWords = set(stopwords.words('french'))

def nettoyage_mots_frequent(texte):
    clean_words = []
    tokeniser_mot=tokenise_mot(texte)
    for token in tokeniser_mot:
     if token not in stopWords:
        clean_words.append(token)
    return clean_words
#TESTS