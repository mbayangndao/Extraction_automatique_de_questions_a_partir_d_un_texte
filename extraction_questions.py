import spacy
from transformers import GPT2Tokenizer
from enlever_mots_vides import nettoyage_mots_frequent
from tokenisation_des_phrases import tokenisation_des_phrases
from nltk.corpus import brown
import string
from nltk import FreqDist
from similarity.normalized_levenshtein import NormalizedLevenshtein
from flashtext import KeywordProcessor
from nltk import word_tokenize
nlp=spacy.load("fr_core_news_sm")
fdist = FreqDist(brown.words())#compte d'un mot spécifique
normalized_levenshtein=NormalizedLevenshtein
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



        
    #Obtenir des options #OK
       

    #est loin
    def comparaisonMotCles(liste_MotCles,mot_actuel,seuil):#OK
        liste_de_score =[]
        for MotCles in liste_MotCles:
            liste_de_score.append(normalized_levenshtein.distance(MotCles.lower(),mot_actuel.lower()))#distance euclidienne entre MotCles et mot actuel
        if min(liste_de_score)>=seuil:
            return True
        else:
            return False
    #Filter les phrases
    def listeReponses(texte):
        motsValables=nettoyage_mots_frequent(texte)
        nom=[]
        popr=[]
        numero=[]
        sortie = []
        doc=nlp(texte)
        for x in doc:
            if x.pos_=="NOUN" and x.text in motsValables:
                nom.append(x.text)
        for y in doc:
            if y.pos_=="PROPN" and y.text in motsValables:
                popr.append(y.text)
        for z in doc:
            if z.pos_=="NUM" and z.text in motsValables:
                numero.append(z.text)
        sortie=nom+popr+numero
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

def accord(texte):#ok
    MotsCles=TotalMotsCles(texte)
    phrase=tokenisation_des_phrases(texte)
    m=len(phrase)
    for j in range(m):
        sentence=(phrase[j])
        doc17=nlp(sentence)
        for token17 in doc17:
            for token18 in doc17:
                 for token19 in doc17:
                    question1={}
                    question2={}
                    try:
                        while token17.pos_=="NOUN" and token17.text in MotsCles and token17.dep_=="obj" and token18.pos_=="VERB" and token18.dep_=="acl" and token19.pos_=="PROPN" and token19.text in MotsCles:
                                        phrase1=sentence.split(token19.text)
                                        phrase1_=phrase1[0]+token19.text
                                        question1['accord']="Qu'est ce qu'ils ont "+token18.text+" "+phrase1_+" ?"
                                        question1['Réponse']="Le/La/Les "+token17.text
                                        return question1
                    except:
                        print("planté")
                       
                        

def questionLieu1(texte):#ok
    MotsCles=TotalMotsCles(texte)
    phrase=tokenisation_des_phrases(texte)
    m=len(phrase)
    for j in range(m):
        sentence=(phrase[j])
        doc17=nlp(sentence)
        for token17 in doc17:
            for token3 in doc17:
                question={}
                try:
                    while token17.pos_=="PROPN" and token17.text in MotsCles and token17.dep_=="flat:name" and token3.pos_=="PROPN" and token3.dep_=="obl:mod" and token3.text in MotsCles:
                        phrase1=sentence.split(token3.text)
                        phrase1_=phrase1[0]
                        question['Lieu']="Ou est ce que "+phrase1_+" ?"
                        question['Réponse']="A "+token3.text+" "+token17.text
                        return question
                except:
                    print("Pas de question lié à la date")
def questionLieu2(sentes):#OK
    MotClesCles=TotalMotsCles(sentes)
    phrase=tokenisation_des_phrases(sentes)
    m=len(phrase)
    for j in range(m):
        sentence=(phrase[j])
        Questions={}
        doc3=nlp(sentence)
        for token3 in doc3:
            try:
                if token3.pos_=="PROPN" and token3.dep_=="obl:mod" and token3.text in MotClesCles and token3.text in sentence:
                    phrase2=sentence.split(token3.text)
                    phrase1=phrase2[0]
                    Questions['lieu']="Ou est ce que "+phrase1+" ?"
                    Questions['réponse']="A "+token3.text
                    return Questions
            except:
                Questions="pas de question"
                return Questions
                            
def sujet_passe(texte):#OK
    MotCles=TotalMotsCles(texte)
    phrase=tokenisation_des_phrases(texte)
    m=len(phrase)
    for j in range(m):
        sentence=(phrase[j])
        doc6=nlp(sentence)
        tokens=word_tokenize(sentence)
        n=len(tokens)
        question:dict
        reponse:dict
        for nomSujet in doc6:
            try:
                while nomSujet.pos_=="NOUN" and nomSujet.text in MotCles and nomSujet.dep_=="nsubj:pass":
                    phrase2=sentence.split(nomSujet.text)
                    phrase2_=phrase2[1]
                    question="Qui "+phrase2_+" ?"
                    question=nomSujet.text
                    return (question,reponse)
            except:
                    print("aucune correspondance")             

def questionTempsDate(texte):#ok
    MotsCles=TotalMotsCles(texte)
    phrase=tokenisation_des_phrases(texte)
    m=len(phrase)
    for j in range(m):
        sentence=(phrase[j])
        doc17=nlp(sentence)
        for token17 in doc17:
            question:string
            reponse:string
            try:
                while token17.pos_=="NUM" and token17.text in MotsCles and token17.dep_=="nmod":
                                phrase1=sentence.split(token17.text)
                                phrase1_=phrase1[1]
                                question="Quant est ce que "+phrase1_+" ?"
                                reponse="En "+token17.text
                                
                                return (question,reponse)
            except:
                print("Pas de question lié à la date")
                question="Aucune question trouvée"
                return question

def questionTempsMois(texte):#ok
    MotsCles=TotalMotsCles(texte)
    phrase=tokenisation_des_phrases(texte)
    m=len(phrase)
    for j in range(m):
        sentence=(phrase[j])
        doc18=nlp(sentence)
        question:string
        reponse:string
        for token18 in doc18:
            try:
                if token18.pos_=="NOUN" and token18.text in MotsCles and token18.dep_=="obl:mod":
                                phrase2=sentence.split(token18.text)
                                phrase2_=phrase2[1]
                                question="En quel moi de "+phrase2_+" ?" 
                                reponse="En "+token18.text
                                return (question,reponse)
            except:
                question="pas de question lié au mois"
                return question

def complementDuNom(texte):#ok
    MotsCles=TotalMotsCles(texte)
    phrase=tokenisation_des_phrases(texte)
    m=len(phrase)
    for j in range(m):
        sentence=(phrase[j])
        doc17=nlp(sentence)
        for token17 in doc17:
            for token18 in doc17:
                question={}
                try:
                    if token17.pos_=="NOUN" and token17.text in MotsCles and token17.dep_=="nmod" and token18.pos_=="NOUN" and token18.dep_=="nsubj:pass":
                                    question['DATE']="Quel "+token18.text+" ?"
                                    question['Réponse']="de "+token17.text
                                    
                                    return question
                except:
                    print("Pas de question lié à la date")

def cOS(texte):#ok
    MotsCles=TotalMotsCles(texte)
    phrase=tokenisation_des_phrases(texte)
    m=len(phrase)
    for j in range(m):
        sentence=(phrase[j])
        doc17=nlp(sentence)
        for token17 in doc17:
            for token18 in doc17:
                question={}
                try:
                    if token17.pos_=="PROPN" and token17.text in MotsCles and token17.dep_=="nmod" and token18.text in MotsCles and token18.pos_=="NOUN" and token18.dep_=="nmod":
                                    question['DATE']=token18.text+" de quoi "+" ?"
                                    question['Réponse']="(De /D') "+token17.text
                                    return question
                except:
                    print("Pas de question lié à la date")

def nombreSujet(texte):#OK
    MotCles=TotalMotsCles(texte)
    phrase=tokenisation_des_phrases(texte)
    m=len(phrase)
    for j in range(m):
        sentence=(phrase[j])
        doc6=nlp(sentence)
        tokens=word_tokenize(sentence)
        n=len(tokens)
        question={}
        for nomSujet in doc6:
                if nomSujet.pos_=="NUM" and nomSujet.text in MotCles and nomSujet.dep_=="nummod":
                    try:
                                        
                        phrase2=sentence.split(nomSujet.text)
                        phrase2_=phrase2[1]
                        question['personne']="Combien de "+phrase2_+" ?" 
                        question['Réponse']=nomSujet.text
                        return question
                    except:
                            question['personne']="Qui "+phrase2_+" ?"
                            question['Réponse']="Aucune personne liée !"
                            return question

def coordination(texte):#ok
    MotsCles=TotalMotsCles(texte)
    phrase=tokenisation_des_phrases(texte)
    m=len(phrase)
    for j in range(m):
        sentence=(phrase[j])
        doc17=nlp(sentence)
        for token17 in doc17:
            question={}
            try:
                if token17.pos_=="PROPN" and token17.text in MotsCles and token17.dep_=="conj":
                                phrase1=sentence.split(token17.text)
                                phrase1_=phrase1[1]
                                question['DATE']="Quel "+phrase1_+" ?"
                                question['Réponse']="En "+token17.text
                                
                                return question
            except:
                print("Pas de question lié à la date")

def Maniere(texte):#ok
    MotsCles=TotalMotsCles(texte)
    phrase=tokenisation_des_phrases(texte)
    m=len(phrase)
    for j in range(m):
        sentence=(phrase[j])
        doc17=nlp(sentence)
        for token17 in doc17:
            question={}
            try:
                if token17.pos_=="NOUN" and token17.text in MotsCles and token17.dep_=="conj":
                                phrase1=sentence.split(token17.text)
                                phrase1_=phrase1[1]
                                question['DATE']="Comment est ce que "+phrase1_+" ?"
                                question['Réponse']="En "+token17.text
                                
                                return question
            except:
                print("Pas de question lié à la date")

def X(texte):#ok
    MotsCles=TotalMotsCles(texte)
    phrase=tokenisation_des_phrases(texte)
    m=len(phrase)
    for j in range(m):
        sentence=(phrase[j])
        doc17=nlp(sentence)
        for token17 in doc17:
            question={}
            try:
                if token17.pos_=="NOUN" and token17.text in MotsCles and token17.dep_=="amod":
                                phrase1=sentence.split(token17.text)
                                phrase1_=phrase1[1]
                                question['DATE']="Quant est ce que "+phrase1_+" ?"
                                question['Réponse']="En "+token17.text
                                
                                return question
            except:
                print("Pas de question lié à la date")

def A(texte):#ok
    MotsCles=TotalMotsCles(texte)
    phrase=tokenisation_des_phrases(texte)
    m=len(phrase)
    for j in range(m):
        sentence=(phrase[j])
        doc17=nlp(sentence)
        for token17 in doc17:
            question={}
            try:
                if token17.pos_=="NOUN" and token17.text in MotsCles and token17.dep_=="obl:arg":
                                phrase1=sentence.split(token17.text)
                                phrase1_=phrase1[1]
                                question['DATE']="Quant est ce que "+phrase1_+" ?"
                                question['Réponse']="En "+token17.text
                                
                                return question
            except:
                print("Pas de question lié à la date")

def motif(texte):#ok
    MotsCles=TotalMotsCles(texte)
    phrase=tokenisation_des_phrases(texte)
    m=len(phrase)
    for j in range(m):
        sentence=(phrase[j])
        doc17=nlp(sentence)
        for token17 in doc17:
            question={}
            try:
                if token17.pos_=="PROPN" and token17.text in MotsCles and token17.dep_=="obl:arg":
                                phrase1=sentence.split(token17.text)
                                phrase1_=phrase1[1]
                                question['DATE']="Quant est ce que "+phrase1_+" ?"
                                question['Réponse']="En "+token17.text
                                
                                return question
            except:
                print("Pas de question lié à la date")

def nomSujet(texte):#OK
    MotCles=TotalMotsCles(texte)
    phrase=tokenisation_des_phrases(texte)
    m=len(phrase)
    for j in range(m):
        sentence=(phrase[j])
        doc6=nlp(sentence)
        tokens=word_tokenize(sentence)
        n=len(tokens)
        question={}
        for nomSujet in doc6:
                if nomSujet.pos_=="NOUN" and nomSujet.text in MotCles and nomSujet.dep_=="nsubj":
                    try:
                                        
                        phrase2=sentence.split(nomSujet.text)
                        phrase2_=phrase2[1]
                        question['personne']="Qui "+phrase2_+" ?" 
                        question['Réponse']=nomSujet.text
                        return question
                    except:
                            question['personne']="Qui "+phrase2_+" ?"
                            question['Réponse']="Aucune personne liée !"
                            return question

def nS(texte):#OK
    MotCles=TotalMotsCles(texte)
    phrase=tokenisation_des_phrases(texte)
    m=len(phrase)
    for j in range(m):
        sentence=(phrase[j])
        doc6=nlp(sentence)
        tokens=word_tokenize(sentence)
        n=len(tokens)
        question={}
        for nomSujet in doc6:
                if nomSujet.pos_=="NUM" and nomSujet.text in MotCles and nomSujet.dep_=="nsubj":
                    try:
                                        
                        phrase2=sentence.split(nomSujet.text)
                        phrase2_=phrase2[1]
                        question['personne']="Qui "+phrase2_+" ?" 
                        question['Réponse']=nomSujet.text
                        return question
                    except:
                            question['personne']="Qui "+phrase2_+" ?"
                            question['Réponse']="Aucune personne liée !"
                            return question   

def sujetPrecis(texte):#OK
    MotCles=TotalMotsCles(texte)
    phrase=tokenisation_des_phrases(texte)
    m=len(phrase)
    for j in range(m):
        sentence=(phrase[j])
        doc6=nlp(sentence)
        tokens=word_tokenize(sentence)
        n=len(tokens)
        question={}
        for nomSujet in doc6:
            try:   
                if nomSujet.pos_=="PROPN" and nomSujet.text in MotCles and nomSujet.dep_=="fixed":     
                    phrase2=sentence.split(nomSujet.text)
                    phrase2_=phrase2[1]
                    question['personne']="Qui "+phrase2_+" ?" 
                    question['Réponse']=nomSujet.text
                    return question
            except:
                        print("pas de question trouvé")

def nS5(texte):#OK
    MotCles=TotalMotsCles(texte)
    phrase=tokenisation_des_phrases(texte)
    m=len(phrase)
    for j in range(m):
        sentence=(phrase[j])
        doc6=nlp(sentence)
        tokens=word_tokenize(sentence)
        n=len(tokens)
        question={}
        for nomSujet in doc6:
                if nomSujet.pos_=="NOUN" and nomSujet.text in MotCles and nomSujet.dep_=="fixed":
                    try:
                                        
                        phrase2=sentence.split(nomSujet.text)
                        phrase2_=phrase2[1]
                        question['personne']="Qui "+phrase2_+" ?" 
                        question['Réponse']=nomSujet.text
                        return question
                    except:
                            question['personne']="Qui "+phrase2_+" ?"
                            question['Réponse']="Aucune personne liée !"
                            return question

def nS8(texte):#OK
    MotCles=TotalMotsCles(texte)
    phrase=tokenisation_des_phrases(texte)
    m=len(phrase)
    for j in range(m):
        sentence=(phrase[j])
        doc6=nlp(sentence)
        tokens=word_tokenize(sentence)
        n=len(tokens)
        question={}
        for nomSujet in doc6:
                if nomSujet.pos_=="NOUN" and nomSujet.text in MotCles and nomSujet.dep_=="obl:agent":
                    try:
                                        
                        phrase2=sentence.split(nomSujet.text)
                        phrase2_=phrase2[1]
                        question['personne']="Qui "+phrase2_+" ?" 
                        question['Réponse']=nomSujet.text
                        return question
                    except:
                            question['personne']="Qui "+phrase2_+" ?"
                            question['Réponse']="Aucune personne liée !"
                            return question
texte1=open("texte1.txt","+r",encoding="utf-8")
text1=texte1.read()
texte2=open("texte2.txt","+r",encoding="utf-8")
text2=texte2.read()
print("token",accord(text1))

