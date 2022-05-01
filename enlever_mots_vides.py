import spacy
from nltk.corpus import stopwords
nlp=spacy.load("fr_core_news_sm")
import tokenisation_des_phrases
stopWords = set(stopwords.words('french'))
class MotsCles:
    def nettoyage_mots_frequent(texte):
        clean_words = []
        tokeniser_mot=tokenisation_des_phrases.tokenise_mot(texte)
        for token in tokeniser_mot:
            if token not in stopWords:
                clean_words.append(token)
        return clean_words
    def listeReponses(texte):
        motsValables=MotsCles.nettoyage_mots_frequent(texte)
        nom=[]
        popr=[]
        numero=[]
        entite_nommee=[]
        sortie = []
        doc=nlp(texte)
        for x in doc:
            if x.pos_=="NOUN" and x.text in motsValables:#étiquetages morphosyntaxiques
                nom.append(x.text)
        for y in doc:
            if y.pos_=="PROPN" and y.text in motsValables:
                popr.append(y.text)
        for z in doc:
            if z.pos_=="NUM" and z.text in motsValables:
                numero.append(z.text)
        for E in doc.ents:#reconnaissance d'entitée nommée
            entite_nommee.append(E.text)
        sortie=nom+popr+numero+entite_nommee
        return sortie

    #Obtenir phrase: OK
    def obtentionGroupeNominal(text):
        doc1=nlp(text)
        phrases={}
        for np in doc1.noun_chunks:
            phrase =np.text
            nbrePhrases = len(phrase.split())#nombre de caractères des phrases nominales
            if nbrePhrases > 1:
                if phrase not in phrases:
                    phrases[phrase]=1
                else:
                    phrases[phrase]=phrases[phrase]+1

        cle_phrase=list(phrases.keys())#liste des clés du dictionnaire
        cle_phrase=cle_phrase[:40]
        return cle_phrase
    #obtenir MotCles clés
    def TotalMotsCles(texte):
        MotCles=MotsCles.obtentionGroupeNominal(texte)+MotsCles.listeReponses(texte)
        return MotCles

#TESTS
text1=open("TEXTES/texte1.txt","r+",encoding="utf_8")
texte1=text1.read()
text2=open("TEXTES/texte2.txt","r+",encoding="utf_8")
texte2=text2.read()
print("toke",MotsCles.TotalMotsCles(texte1))