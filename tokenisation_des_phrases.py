import spacy
import enlever_mots_vides
from flashtext import KeywordProcessor
from nltk import FreqDist
from nltk.corpus import brown
fdist = FreqDist(brown.words())#compte d'un mot spécifique
nlp=spacy.load('fr_core_news_sm')
def tokenisation_des_phrases(sentence):
    doc=nlp(sentence)
    return [phrase.text for phrase in doc.sents]
    
#Aprés tokenistaion des phrase
def tokenise_mot(texte):
    phrases_obtenues=tokenisation_des_phrases(texte)
    m=len(phrases_obtenues)
    for j in range(m):
        doc1=nlp(phrases_obtenues[j])
        return [token.text for token in doc1]
class Modification:
 #trouver le nombre de fois qu'un caractère d'un mot est présent dans une ou des phrases avec comme clé la caractère et la valeur une liste des caractères trouvés #OK
    def PhraseDeMotClesCles(MotsCles,phrases):
        processeur_de_MotsCles=KeywordProcessor('french')
        phrases_de_MotsCles={}
        for mot in MotsCles:
            mot =mot.strip()
            phrases_de_MotsCles[mot] = []
            processeur_de_MotsCles.add_keyword(mot)
        for phrase in phrases:
            MotsCles_trouves = processeur_de_MotsCles.extract_keywords(phrase)
            for cle in MotsCles_trouves:
                phrases_de_MotsCles[cle].append(phrase)

        for cle in phrases_de_MotsCles.keys():
            valeurs =phrases_de_MotsCles[cle]
            valeurs = sorted(valeurs, key= lambda x: len(x), reverse=True)
            phrases_de_MotsCles[cle] = valeurs

        cles_supprimes = []
        for k in phrases_de_MotsCles.keys():
            if len(phrases_de_MotsCles[k]) == 0:
                cles_supprimes.append(k)
        for cle_supprime in cles_supprimes:
            del phrases_de_MotsCles[cle_supprime]
        return phrases_de_MotsCles



        
    #Intervalle de réponses
    def listeReponses(texte):
        motsValables=enlever_mots_vides.nettoyage_mots_frequent(texte)
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
    MotCles=Modification.obtentionGroupeNominal(texte)+Modification.listeReponses(texte)
    return MotCles
