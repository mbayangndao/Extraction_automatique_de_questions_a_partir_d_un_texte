import spacy
from enlever_mots_vides import nettoyage_mots_frequent
from tokenisation_des_phrases import tokenisation_des_phrases
from nltk import word_tokenize
nlp=spacy.load("fr_core_news_sm")

def extraction_questions(texte):
   mots=nettoyage_mots_frequent(texte)
   phrase=tokenisation_des_phrases(texte)
   m=len(phrase)
   for j in range(m):
       sentence=(phrase[j])
       mot=word_tokenize(sentence)
       doc7=nlp(sentence)
       for token1 in doc7:
           for tok1 in doc7:
               for toke1 in doc7:
                   for determinant in doc7:
                        while token1.text in mots and token1.text in mot and token1.pos_=="PROPN" and token1.dep_=="fixed" and token1.is_stop==False and tok1.pos_=="AUX" and tok1.dep_=="cop" and toke1.pos_=="NOUN" and toke1.dep_=="nmod" and toke1.is_stop==False and toke1.text in sentence and determinant.pos_=="DET" and determinant.dep_=="det":
                            questions="qui "+tok1.text+" "+determinant.text+" "+toke1.text+"\nréponse:"+token1.text
                            return questions

def questions_lieu(texte):
   mots=nettoyage_mots_frequent(texte)
   phrase=tokenisation_des_phrases(texte)
   m=len(phrase)
   for j in range(m):
    sentence=(phrase[j])
    doc2=nlp(sentence)
    for token2 in doc2:
        if token2.text in mots and token2.pos_=="PROPN" and token2.dep_=="obl:mod" and token2.is_stop==False:
            for tok2 in doc2:
             if tok2.text in mots and tok2.pos_=="VERB" and tok2.dep_=="ROOT":
                 for toke2 in doc2:
                     if toke2.text in mots and toke2.pos_=="NOUN" and toke2.dep_=="nsubj:pass":
                         for tokes2 in doc2:
                             if tokes2.pos_=="AUX" and tokes2.dep_=="aux:pass":
                                return "ou s'"+tokes2.text+" "+tok2.text+" "+toke2.text+" "+"?"+"\n réponse:"+token2.text#lieu propre

       
def nom_propre(texte):
    mots=nettoyage_mots_frequent(texte)
    phrase=tokenisation_des_phrases(texte)
    m=len(phrase)
    for j in range(m):
        sentence=(phrase[j])
        doc7=nlp(sentence)
        for token3 in doc7:
            if token3.text in mots and token3.pos_=="PROPN" and token3.dep_=="flat:name" and token3.is_stop==False:#Pour obtenir le deuxième mot comme résultat
                for tok3 in doc7:
                    if tok3.text in mots and tok3.pos_=="VERB" and tok3.dep_=="ROOT":
                        for toke3 in doc7:
                            if toke3.text in mots and toke3.pos_=="NOUN" and toke3.dep_=="nsubj:pass":
                                for tokes3 in doc7:
                                    if tokes3.pos_=="AUX" and tokes3.dep_=="aux:pass":
                                        return "ou s'"+tokes3.text+" "+tok3.text+" "+toke3.text+" ?\n réponse: "+token3.text#lieu propre

def complement_du_nom(texte):
    mots=nettoyage_mots_frequent(texte)
    phrase=tokenisation_des_phrases(texte)
    m=len(phrase)
    for j in range(m):
        sentence=(phrase[j])
        doc7=nlp(sentence)
        for token4 in doc7:
            if token4.text in mots and token4.pos_=="PROPN" and token4.dep_=="nmod" and token4.is_stop==False:
                for entite in doc7:
                    if entite.pos=="NOUN" and entite.dep_=="obl:arg":#nom employé comme lieu"
                        questions="Quel "+entite.text+"\nréponse:"+" "+token4.text
                        return questions

def questions_temps(texte):
    mots=nettoyage_mots_frequent(texte)
    phrase=tokenisation_des_phrases(texte)
    m=len(phrase)
    for j in range(m):
        sentence=(phrase[j])
        doc7=nlp(sentence)
        for temps in doc7:
            if temps.text in mots and temps.pos_=="NOUN" and temps.dep_=="obl:mod" and temps.is_stop==False:#CCT avec mois
                for nombre in doc7:
                        if nombre.text in mots and nombre.pos_=="NUM" and nombre.dep_=="nummod":
                            for nomSujet in doc7:
                                if nomSujet.text in mots and nomSujet.pos_=="NOUN" and nomSujet.dep_=="nsubj:pass":
                                    for avoirConjugue in doc7:     
                                        if  avoirConjugue.pos_=="AUX" and avoirConjugue.dep_=="aux:tense":
                                            for pPasse in doc7:
                                                if pPasse.pos_=="VERB" and pPasse.dep=="acl:relcl":
                                                    for preposition in doc7:
                                                        if preposition.pos=="ADP" and preposition.dep_=="case":
                                                            return "Quant est ce que"+" "+nombre.text+" "+nomSujet.text+""+avoirConjugue.text+" "+pPasse.text+" "+preposition.text+" ?"+"\n réponse: "+temps.text

def sujet_passe(texte):
    mots=nettoyage_mots_frequent(texte)
    phrase=tokenisation_des_phrases(texte)
    m=len(phrase)
    for j in range(m):
        sentence=(phrase[j])
        doc7=nlp(sentence)
        for nomSujet in doc7:
            if nomSujet.text in mots and nomSujet.pos_=="NOUN" and nomSujet.dep_=="nsubj:pass" and nomSujet.is_stop==False:
                for tok in doc7:
                            if tok.text in mots and tok.pos_=="" and tok.dep_=="":
                                for toke in doc7:
                                    if toke.text in mots and toke.pos_=="" and toke.dep_=="":
                                        return print("")
def questions(texte):
    mots=nettoyage_mots_frequent(texte)
    phrase=tokenisation_des_phrases(texte)
    m=len(phrase)
    for j in range(m):
        sentence=(phrase[j])
        doc7=nlp(sentence)
        for token7 in doc7:
            if token7.text in mots and token7.pos_=="NOUN" and token7.dep_=="nmod" and token7.is_stop==False:#COI
                return print("")

        for token8 in doc7:
            if token8.text in mots and token8.pos_=="NOUN" and token8.dep_=="obl:mod" and token8.is_stop==False:#COD
                return print("")

        for token9 in doc7:
            if token9.text in mots and token9.pos_=="NOUN" and token9.dep_=="obl:mod" and token9.is_stop==False:#CCT
                return print("")

        for token10 in doc7:
            if token10.text in mots and token10.pos_=="NOUN" and token10.dep_=="root" and token10.is_stop==False:
                return print("")#commplément du nom
        for token10 in doc7:
            if token10.text in mots and token10.pos_=="NOUN" and token10.dep_=="obj" and token10.is_stop==False:#COD
                return print("")
        for token11 in doc7:
            if token11.text in mots and token11.pos_=="VERB" and token11.dep_=="acl:relcl" and token11.is_stop==False:#participe passé employé comme adjectif qualificatif attribut
                return print("")
        for token12 in doc7:
            if token12.text in mots and token12.pos_=="VERB" and token12.dep_=="root" and token12.is_stop==False:#verbe pronominal
                return print("")
            
        for token13 in doc7:
            if token13.text in mots and token13.pos_=="VERB" and token13.dep_=="acl" and token13.is_stop==False:#Verb à l'infinitif
                return print("")

        for token14 in doc7:
            if token14.text in mots and token14.pos_=="VERB" and token14.dep_=="acl" and token14.is_stop==False:#participe présent
                return print("")

        for token15 in doc7:
            if token15.text in mots and token15.pos_=="ADJ" and token15.dep_=="amod" and token15.is_stop==False:#épithète du nom
                return print("")

        for token16 in doc7:
            if token16.text in mots and token16.pos_=="ADJ" and token16.dep_=="amod" and token16.is_stop==False:
                return print("")

        for token17 in doc7:
            if token17.text in mots and token17.pos_=="NUM" and token17.dep_=="nmod" and token17.is_stop==False:#CCT avec année
                return print("")

        for token18 in doc7:
            if token18.text in mots and token18.pos_=="CCONJ" and token18.dep_=="" and token18.is_stop==False:
                return print("")

        for token19 in doc7:
            if token19.text in mots and token19.pos_=="" and token19.dep_=="" and token19.is_stop==False:
                return print("")
        for token20 in doc7:
            if token20.text in mots and token20.pos_=="" and token20.dep_=="" and token20.is_stop==False:
                return print("")

        for token21 in doc7:
            if token21.text in mots and token21.pos_=="" and token21.dep_=="" and token21.is_stop==False:
                return print("")