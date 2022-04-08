import spacy
from enlever_mots_vides import nettoyage_mots_frequent
from NER import return_NER
adjectifs=[]
noms=[]
verbes=[]
prepositions=[]
adverbes=[]
determinants=[]
conjonction_de_subordination=[]
conjonction_de_coordination=[]
auxiliaires=[]
ponctuations=[]
pronoms=[]
numeros=[]
proposition=[]
espace=[]
personnes=[]
dates=[]
temps=[]
def return_pos(sentences):
    texte3=nettoyage_mots_frequent(sentences)
    texte4=" ".join(texte3)
    nlp=spacy.load('fr_core_news_sm')

    doc=nlp(texte4)
    try:
        for tok1 in doc:
            if tok1.lemma_ not in adjectifs and tok1.pos_=="ADJ":
                adjectifs.append(tok1.lemma_)

            elif tok1.pos_=="NOUN":
                noms.append(tok1.lemma_)
                
            elif tok1.lemma_ not in prepositions and tok1.pos_=="ADP":
                prepositions.append(tok1.lemma_)

            elif tok1.lemma_ not in noms and tok1.pos_=="NUM":
                noms.append(tok1.lemma_)

            elif tok1.lemma_ not in pronoms and  tok1.pos_=="PRON":
                pronoms.append(tok1.lemma_)

            elif  tok1.lemma_ not in verbes and tok1.pos_=="VERB":
                verbes.append(tok1.lemma_)
            
            elif  tok1.lemma_ not in adverbes and tok1.pos_=="ADV":
                adverbes.append(tok1.lemma_)

            elif tok1.lemma_ not in determinants and  tok1.pos_=="DET":
                determinants.append(tok1.lemma_)

            elif tok1.lemma_ not in conjonction_de_subordination and  tok1.pos_=="SCONJ":
                conjonction_de_subordination.append(tok1.lemma_)

            elif tok1.lemma_ not in conjonction_de_coordination and  tok1.pos_=="CCONJ":
                conjonction_de_coordination.append(tok1.lemma_)

            elif  tok1.lemma_ not in auxiliaires and tok1.pos=="AUX":
                auxiliaires.append(tok1.lemma_)

            elif tok1.lemma_ not in ponctuations and  tok1.pos_=="PUNCT":
                ponctuations.append(tok1.lemma_)
            elif tok1.lemma_ not in numeros and  tok1.pos_=="NUM":
                numeros.append(tok1.lemma_)
            elif tok1.lemma_ not in proposition and  tok1.pos_=="PROPN":
                proposition.append(tok1.lemma_)
            elif tok1.lemma_ not in espace and  tok1.pos_=="SPACE":
                espace.append(tok1.lemma_)
            elif tok1.lemma_ not in personnes and tok1.pos=="PERSON":
                personnes.append(tok1.lemma_)
            else:
                print("Ce mot n'existe pas en français")   
        return print("LES ADJECTIFS :",adjectifs,
    "\nLES NOMS :",noms,
    "\nLES VERBES :",verbes,
    "\nLES PREPOSITIONS",prepositions,
    "\nLES NUMEROS",numeros,
    "\nLES ADVERBES",adverbes,
    "\nLES DETERMINANTS",determinants,
    "\nLES CONJONCTIONS DE SUBORDINATION",conjonction_de_subordination,
    "\nLES CONJONCTIONS DE COORDINATION",conjonction_de_coordination,
    "\nLES AUXILIAIRES",auxiliaires,"\nLES PONCTUATIONS",ponctuations,
    "\nLES PRONOMS",pronoms,
    "\nLES PROPOSITIONS",proposition,
    "\nLES ESPACES",espace,
    "\n personnes",personnes)
    except:
            print("Entrer un mot valide")
    finally:
            print("FIN DU PROGRAMME")
