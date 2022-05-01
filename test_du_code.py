from extraction_questionsGN import *
from extraction_questionsMAM import *

from os import chdir
text1=open("TEXTES/texte1.txt","r+",encoding="utf_8")
texte1=text1.read()
text2=open("TEXTES/texte2.txt","r+",encoding="utf_8")
texte2=text2.read()
chdir("C:/Users/debbo/Documents/SEMESTRE 4")
text3=open("test3.txt","r+",encoding="utf_8")
texte3=text3.read()

#test du système sur le texte1

entites_nommees=GNT(texte1)
n=len(entites_nommees)
for j in range(n):
    print("question NERT possible",entites_nommees[j])

accord= ExtractionQuestionsReponses.accord(texte1)
print("accord",accord)
questionLieu1=ExtractionQuestionsReponses.questionLieu1(texte1)
questionLieu2=ExtractionQuestionsReponses.questionLieu2(texte1)
sujet_passe=ExtractionQuestionsReponses.sujet_passe(texte1)
questionTempsDate=ExtractionQuestionsReponses.questionTempsDate(texte1)
questionTempsMois=ExtractionQuestionsReponses.questionTempsMois(texte1)
complementDuNom=ExtractionQuestionsReponses.complementDuNom(texte1)
cOS=ExtractionQuestionsReponses.cOS(texte1)
nombreSujet=ExtractionQuestionsReponses.nombreSujet(texte1)
coordination=ExtractionQuestionsReponses.coordination(texte1)
Manière=ExtractionQuestionsReponses.Maniere(texte1)
X=ExtractionQuestionsReponses.X(texte1)
A=ExtractionQuestionsReponses.A(texte1)
motif=ExtractionQuestionsReponses.motif(texte1)
nomSujet=ExtractionQuestionsReponses.nomSujet(texte1)
sujetPrecis=ExtractionQuestionsReponses.sujetPrecis(texte1)



    


#test du système sur le texte2
groupe_nominaux2=GNT(texte2)
p=len(groupe_nominaux2)
for k in range(p):
    print("question GNT possible",groupe_nominaux2[k])

entites_nommees2=ExtractionQuestionsReponses.NERT(texte2)
q=len(entites_nommees2)
for l in range(q):
    print("question NERT possible",entites_nommees2[l])
accord2= ExtractionQuestionsReponses.accord(texte2)
questionLieu12=ExtractionQuestionsReponses.questionLieu1(texte2)
questionLieu22=ExtractionQuestionsReponses.questionLieu2(texte2)
sujet_passe2=ExtractionQuestionsReponses.sujet_passe(texte2)
questionTempsDate2=ExtractionQuestionsReponses.questionTempsDate(texte2)
questionTempsMois2=ExtractionQuestionsReponses.questionTempsMois(texte2)
complementDuNom2=ExtractionQuestionsReponses.complementDuNom(texte2)
cOS2=ExtractionQuestionsReponses.cOS(texte2)
nombreSujet2=ExtractionQuestionsReponses.nombreSujet(texte2)
coordination2=ExtractionQuestionsReponses.coordination(texte2)
Manière2=ExtractionQuestionsReponses.Maniere(texte2)
X2=ExtractionQuestionsReponses.X(texte2)
A2=ExtractionQuestionsReponses.A(texte2)
motif2=ExtractionQuestionsReponses.motif(texte2)
nomSujet2=ExtractionQuestionsReponses.nomSujet(texte2)
sujetPrecis2=ExtractionQuestionsReponses.sujetPrecis(texte2)
from spacy import displacy
 
doc = nlp(texte1)
displacy.serve(doc, style="dep")
