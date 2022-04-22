
from nltk import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
import spacy
import pke
import string
nlp=spacy.load("fr_core_news_sm")
stopWords = set(stopwords.words('french'))
text1=open("texte1.txt","r+",encoding="utf_8")
texte1=text1.read()
text2=open("texte2.txt","r+",encoding="utf_8")
texte2=text2.read()
