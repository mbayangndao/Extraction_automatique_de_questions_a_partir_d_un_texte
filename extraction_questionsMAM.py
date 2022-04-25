import spacy
from enlever_mots_vides import nettoyage_mots_frequent
from tokenisation_des_phrases import tokenisation_des_phrases,TotalMotsCles
nlp=spacy.load("fr_core_news_sm")

class ExtractionQuestionsReponses:
    def accord(texte):#ok
        motsValables=nettoyage_mots_frequent(texte)
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
                        try:
                            while token17.pos_=="NOUN" and token17.text in MotsCles and token17.text in motsValables and token17.dep_=="obj" and token18.pos_=="VERB" and token18.dep_=="acl" and token19.pos_=="PROPN" and token19.text in MotsCles:
                                            phrase1=sentence.split(token19.text)
                                            phrase1_=phrase1[0]+token19.text
                                            question1['accord']="Qu'est ce qu'ils ont "+token18.text+" "+phrase1_+" ?"
                                            question1['Réponse']="Le/La/Les "+token17.text
                                            return question1
                        except:
                            print("planté")
                        
                            

    def questionLieu1(texte):#ok
        MotsCles=TotalMotsCles(texte)
        motsValables=nettoyage_mots_frequent(texte)
        phrase=tokenisation_des_phrases(texte)
        m=len(phrase)
        for j in range(m):
            sentence=(phrase[j])
            doc17=nlp(sentence)
            for token17 in doc17:
                for token3 in doc17:
                    question={}
                    try:
                        while token17.pos_=="PROPN" and token17.text in MotsCles and token17.text in motsValables and token17.dep_=="flat:name" and token3.pos_=="PROPN" and token3.dep_=="obl:mod" and token3.text in MotsCles:
                            phrase1=sentence.split(token3.text)
                            phrase1_=phrase1[0]
                            question['question']="Ou est ce que "+phrase1_+" ?"
                            question['Réponse']="A "+token3.text+" "+token17.text
                            return question
                    except:
                        print("Pas de question lié à la date")
    def questionLieu2(texte):#OK
        MotClesCles=TotalMotsCles(texte)
        motsValables=nettoyage_mots_frequent(texte)
        phrase=tokenisation_des_phrases(texte)
        m=len(phrase)
        for j in range(m):
            sentence=(phrase[j])
            Questions={}
            doc3=nlp(sentence)
            for token3 in doc3:
                try:
                    if token3.pos_=="PROPN" and token3.dep_=="obl:mod" and token3.text in MotClesCles and token3.text in motsValables:
                        phrase2=sentence.split(token3.text)
                        phrase1=phrase2[0]
                        Questions['question']="Ou est ce que "+phrase1+" ?"
                        Questions['réponse']="A "+token3.text
                        return Questions
                except:
                    print("pas de question")
                                
    def sujet_passe(texte):#OK
        MotCles=TotalMotsCles(texte)
        motsValables=nettoyage_mots_frequent(texte)
        phrase=tokenisation_des_phrases(texte)
        m=len(phrase)
        for j in range(m):
            sentence=(phrase[j])
            doc6=nlp(sentence)
            tokens=[X.text for X in doc6]
            n=len(tokens)
            question={}
            for nomSujet in doc6:
                try:
                    while nomSujet.pos_=="NOUN" and nomSujet.text in MotCles and nomSujet.text in motsValables and nomSujet.dep_=="nsubj:pass":
                        phrase2=sentence.split(nomSujet.text)
                        phrase2_=phrase2[1]
                        question['question']="Qui "+phrase2_+" ?"
                        question['réponse']=nomSujet.text
                        return question
                except:
                        print("aucune correspondance")             

    def questionTempsDate(texte):#ok
        MotsCles=TotalMotsCles(texte)
        motsValables=nettoyage_mots_frequent(texte)
        phrase=tokenisation_des_phrases(texte)
        question={}
        m=len(phrase)
        for j in range(m):
            sentence=(phrase[j])
            doc17=nlp(sentence)
            question={}
            for token17 in doc17:
                try:
                    while token17.pos_=="NUM" and token17.text in MotsCles and token17.text in motsValables and token17.dep_=="nmod":
                                    phrase1=sentence.split(token17.text)
                                    phrase1_=phrase1[1]
                                    question['question']="Quant est ce que "+phrase1_+" ?"
                                    question['reponse']="En "+token17.text
                                    return question
                except:
                    print("Pas de question lié à la date")
           
    def questionTempsMois(texte):#ok
        MotsCles=TotalMotsCles(texte)
        motsValables=nettoyage_mots_frequent(texte)
        phrase=tokenisation_des_phrases(texte)
        m=len(phrase)
        for j in range(m):
            sentence=(phrase[j])
            doc18=nlp(sentence)
            question={}
            for token18 in doc18:
                try:
                    if token18.pos_=="NOUN" and token18.text in MotsCles and token18.text in motsValables and token18.dep_=="obl:mod":
                                    phrase2=sentence.split(token18.text)
                                    phrase2_=phrase2[1]
                                    question['question']="En quel moi de "+phrase2_+" ?" 
                                    question['reponse']="En "+token18.text
                                    return question
                except:
                    print("pas de question lié au mois")

    def complementDuNom(texte):#ok
        MotsCles=TotalMotsCles(texte)
        motsValables=nettoyage_mots_frequent(texte)
        phrase=tokenisation_des_phrases(texte)
        m=len(phrase)
        for j in range(m):
            sentence=(phrase[j])
            doc17=nlp(sentence)
            question={}
            for token17 in doc17:
                for token18 in doc17:
                    try:
                        if token17.pos_=="NOUN" and token17.text in MotsCles and token17.text in motsValables and token17.dep_=="nmod" and token18.pos_=="NOUN" and token18.dep_=="nsubj:pass":
                            question['question']="Quel "+token18.text+" ?"
                            question['reponse']="de "+token17.text
                            return question      
                    except:
                        print("Pas de question lié à la date")

    def cOS(texte):#ok
        MotsCles=TotalMotsCles(texte)
        motsValables=nettoyage_mots_frequent(texte)
        phrase=tokenisation_des_phrases(texte)
        m=len(phrase)
        question={}
        for j in range(m):
            sentence=(phrase[j])
            doc17=nlp(sentence)
            for token17 in doc17:
                for token18 in doc17:
                    try:
                        if token17.pos_=="PROPN" and token17.text in MotsCles and token17.text in motsValables and token17.dep_=="nmod" and token18.text in MotsCles and token18.pos_=="NOUN" and token18.dep_=="nmod":
                                        question['DATE']=token18.text+" de quoi "+" ?"
                                        question['Réponse']="(De /D') "+token17.text
                                        return question
                    except:
                        print("Pas de question lié à la date")

    def nombreSujet(texte):#OK
        MotCles=TotalMotsCles(texte)
        motsValables=nettoyage_mots_frequent(texte)
        phrase=tokenisation_des_phrases(texte)
        m=len(phrase)
        for j in range(m):
            sentence=(phrase[j])
            doc6=nlp(sentence)
            tokens=[X.text for X in doc6]
            n=len(tokens)
            question={}
            for nomSujet in doc6:
                    if nomSujet.pos_=="NUM" and nomSujet.text in MotCles and nomSujet.text in motsValables and nomSujet.dep_=="nummod":
                        try:
                                            
                            phrase2=sentence.split(nomSujet.text)
                            phrase2_=phrase2[1]
                            question['personne']="Combien de "+phrase2_+" ?" 
                            question['Réponse']=nomSujet.text
                            return question
                        except:
                                print("Aucune personne liée !")

    def coordination(texte):#ok
        MotsCles=TotalMotsCles(texte)
        motsValables=nettoyage_mots_frequent(texte)
        phrase=tokenisation_des_phrases(texte)
        m=len(phrase)
        for j in range(m):
            sentence=(phrase[j])
            doc17=nlp(sentence)
            for token17 in doc17:
                question={}
                try:
                    if token17.pos_=="PROPN" and token17.text in MotsCles and token17.text in motsValables and token17.dep_=="conj":
                                    phrase1=sentence.split(token17.text)
                                    phrase1_=phrase1[1]
                                    question['DATE']="Quel "+phrase1_+" ?"
                                    question['Réponse']="En "+token17.text
                                    
                                    return question
                except:
                    print("Pas de question lié à la date")

    def Maniere(texte):#ok
        MotsCles=TotalMotsCles(texte)
        motsValables=nettoyage_mots_frequent(texte)
        phrase=tokenisation_des_phrases(texte)
        m=len(phrase)
        for j in range(m):
            sentence=(phrase[j])
            doc17=nlp(sentence)
            for token17 in doc17:
                question={}
                try:
                    if token17.pos_=="NOUN" and token17.text in MotsCles and token17.text in motsValables and token17.dep_=="conj":
                                    phrase1=sentence.split(token17.text)
                                    phrase1_=phrase1[1]
                                    question['DATE']="Comment est ce que "+phrase1_+" ?"
                                    question['Réponse']="En "+token17.text
                                    
                                    return question
                except:
                    print("Pas de question lié à la date")

    def X(texte):#à vérifier
        MotsCles=TotalMotsCles(texte)
        motsValables=nettoyage_mots_frequent(texte)
        phrase=tokenisation_des_phrases(texte)
        m=len(phrase)
        for j in range(m):
            sentence=(phrase[j])
            doc17=nlp(sentence)
            for token17 in doc17:
                question={}
                try:
                    if token17.pos_=="NOUN" and token17.text in MotsCles and token17.text in motsValables and token17.dep_=="amod":
                                    phrase1=sentence.split(token17.text)
                                    phrase1_=phrase1[1]
                                    question['DATE']="Quant est ce que "+phrase1_+" ?"
                                    question['Réponse']="En "+token17.text
                                    return question
                except:
                    print("Pas de question lié à la date")

    def A(texte):#ok
        MotsCles=TotalMotsCles(texte)
        motsValables=nettoyage_mots_frequent(texte)
        phrase=tokenisation_des_phrases(texte)
        m=len(phrase)
        for j in range(m):
            sentence=(phrase[j])
            doc17=nlp(sentence)
            for token17 in doc17:
                question={}
                try:
                    if token17.pos_=="NOUN" and token17.text in MotsCles and token17.text in motsValables and token17.dep_=="obl:arg":
                                    phrase1=sentence.split(token17.text)
                                    phrase1_=phrase1[1]
                                    question['DATE']="Quant est ce que "+phrase1_+" ?"
                                    question['Réponse']="En "+token17.text
                                    
                                    return question
                except:
                    print("Pas de question lié à la date")

    def motif(texte):#ok
        MotsCles=TotalMotsCles(texte)
        motsValables=nettoyage_mots_frequent(texte)
        phrase=tokenisation_des_phrases(texte)
        m=len(phrase)
        for j in range(m):
            sentence=(phrase[j])
            doc17=nlp(sentence)
            for token17 in doc17:
                question={}
                try:
                    if token17.pos_=="PROPN" and token17.text in MotsCles and token17.text in motsValables and token17.dep_=="obl:arg":
                                    phrase1=sentence.split(token17.text)
                                    phrase1_=phrase1[1]
                                    question['DATE']="Quant est ce que "+phrase1_+" ?"
                                    question['Réponse']="En "+token17.text
                                    
                                    return question
                except:
                    print("Pas de question lié à la date")

    def nomSujet(texte):#OK
        MotCles=TotalMotsCles(texte)
        motsValables=nettoyage_mots_frequent(texte)
        phrase=tokenisation_des_phrases(texte)
        m=len(phrase)
        for j in range(m):
            sentence=(phrase[j])
            doc6=nlp(sentence)
            tokens=[X.text for X in doc6]
            n=len(tokens)
            question={}
            for nomSujet in doc6:
                    if nomSujet.pos_=="NOUN" and nomSujet.text in MotCles and nomSujet.text in motsValables and nomSujet.dep_=="nsubj":
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
        motsValables=nettoyage_mots_frequent(texte)
        phrase=tokenisation_des_phrases(texte)
        m=len(phrase)
        for j in range(m):
            sentence=(phrase[j])
            doc6=nlp(sentence)
            tokens=[X.text for X in doc6]
            n=len(tokens)
            question={}
            for nomSujet in doc6:
                try:   
                    if nomSujet.pos_=="PROPN" and nomSujet.text in MotCles and nomSujet.text in motsValables and nomSujet.dep_=="fixed":     
                        phrase2=sentence.split(nomSujet.text)
                        phrase2_=phrase2[1]
                        question['personne']="Qui "+phrase2_+" ?" 
                        question['Réponse']=nomSujet.text
                        return question
                except:
                            print("pas de question trouvé")



