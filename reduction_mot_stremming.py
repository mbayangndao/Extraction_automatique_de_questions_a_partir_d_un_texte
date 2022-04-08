import spacy
from enlever_mots_vides import nettoyage_mots_frequent
from nltk.stem.snowball import SnowballStemmer,FrenchStemmer
nlp = spacy.load("fr_core_news_sm")
stemmer = SnowballStemmer(language='french')
mots_obtenus=[]
def return_mots_reduits(text2):
    text1=nettoyage_mots_frequent(text2)
    text3=" ".join(text1)
    doc=nlp(text3)
    for X in doc:
        mots_obtenus.append(stemmer.stem(X.text))
    return mots_obtenus