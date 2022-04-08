import spacy
nlp=spacy.load('fr_core_news_sm')
from reduction_mot_stremming import return_mots_reduits
"""Spacy dispose également d’une option de visualisation qui nous permet simplement d’afficher les étiquettes identifiées ainsi que les dépendances entre ces étiquettes.
#displacy.serve(doc, style="dep")
Spacy dispose également d’une option de visualisation qui nous permet simplement d’afficher les étiquettes identifiées ainsi que les dépendances entre ces étiquettes.
"""
organisations=[]
localites=[]
but=[]
motivation=[]
dates=[]
    #NNP
    #NNPS
    #NNS
    #PRP
    #NN
    #
    #
    #
    #     
def return_NER(sentence):
    texte4=return_mots_reduits(sentence)
    text4=" ".join(texte4)
    doc=nlp(text4)
    for X in doc.ents:
        if X.label_=="ORG": 
            organisations.append(X.text)
        elif X.label_=="LOC":
            localites.append(X.text)
        elif X.label_=="PER":
         but.append(X.text)
        elif X.label_=="MISC":
            motivation.append(X.text)
        elif X.label_=="TIME":
            dates.append(X.text)
        else:
            print("vérifiez le mot")
    return print("\nOrganisation",organisations,
    "\nlocalisation",localites,
    "\nbut",but,
    "\nmotivation",motivation,
    "\ndates",dates
    )

    # Retourner le texte et le label pour chaque entit"