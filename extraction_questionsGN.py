from enlever_mots_vides import nettoyage_mots_frequent
from tokenisation_des_phrases import tokenisation_des_phrases,nlp,TotalMotsCles

#ORG()
#LOC(ou)
#MISC(quand)
#PER
def entiteesNommees(sentence):#question basée sur les entitée nommées
        phrases=tokenisation_des_phrases(sentence)
        motsValables=nettoyage_mots_frequent(sentence)
        motsCles=TotalMotsCles(sentence)
        organisation1={}
        organisation2={}
        organisation3={}
        localite1={}
        localite2={}
        localite3={}
        localite4={}
        localite5={}
        localite6={}
        localite7={}
        periode1={}
        periode2={}
        personne1={}
        personne2={}
        questions={}
        n=len(phrases)
        for j in range(n):
            doc=nlp(phrases[j])
            for org1 in doc.ents:
                if org1.label_=="ORG" and org1.root.dep_=="obj":
                    phrase1=phrases[j].split(org1.text)
                    organisation1['question']="Ou "+phrase1[0]+" ?"
                    organisation1['Réponse']=org1.text
                    
            for org2 in doc.ents:
                if org2.label_=="ORG" and org2.root.dep_=="nsubj:pass":
                    phrase2=phrases[j].split(org2.text)
                    organisation2['question']="Quelle organisation "+phrase2[1].replace(".","?")
                    organisation2['Réponse']=org2.text
            questions['organisations_sujet_passe']=organisation2

            for org3 in doc.ents:
                if org3.label_=="ORG" and org3.root.dep_=="nmod":
                    phrase3=phrases[j].split(org3.text)
                    organisation2['question']="Dans quelle organisation "+phrase3[1].replace(".","?")
                    organisation2['Réponse']=org3.text
            questions['organisations_sujet_passe']=organisation3


            for loc1 in doc.ents:
                if loc1.label_=="LOC" and loc1.root.dep_=="nsubj":
                
                    phrase4=phrases[j].split(loc1.text)
                    localite1['question']="Dans quelle localité "+phrase4[1].replace(".","?")
                    localite1['Réponse']=loc1.text
            questions['localités_sujets']=localite1

            for loc2 in doc.ents:
                if loc2.label_=="LOC" and loc2.root.dep_=="nmod":
                    phrase5=phrases[j].split(loc2.text)
                    localite2['question']="Qui est"+phrase5[1].replace(".","?")#ok
                    localite2['Réponse']=loc2.text
            questions['localités_accord']=localite2

            for loc3 in doc.ents:
                if loc3.label_=="LOC" and loc3.root.dep_=="conj":
                    phrase6=phrases[j].split(loc3.text)
                    localite3['question']="Dans quelle localité "+phrase6[1].replace(".","?")
                    localite3['Réponse']=loc3.text
            questions['localités_supplémentaires']=localite3

            for loc4 in doc.ents:
                if loc4.label_=="LOC" and loc4.root.dep_=="nsubj":
                    phrase7=phrases[j].split(loc4.text)
                    localite4['question']="Dans quelle localité "+phrase7[1].replace(".","?")
                    localite4['Réponse']=loc4.text
            questions['localités_sujets']=localite4

            for loc5 in doc.ents:
                if loc5.label_=="LOC" and loc5.root.dep_=="obl:arg":
                    phrase8=phrases[j].split(loc5.text)
                    localite5['question']="Dans quelle localité "+phrase8[1].replace(".","?")
                    localite5['Réponse']=loc5.text
            questions['localités-lieu2']=localite5

            for loc6 in doc.ents:
                if loc6.label_=="LOC" and loc6.root.dep_=="apos":
                    phrase9=phrases[j].split(loc6.text)
                    localite6['question']="Dans quelle localité "+phrase9[1].replace(".","?")
                    localite6['Réponse']=loc6.text
            questions['localités-apos']=localite6

            for loc7 in doc.ents:
                if loc7.label_=="LOC" and loc7.root.dep_=="ROOT":
                    phrase10=phrases[j].split(loc7.text)
                    localite7['question']="Dans quelle localité "+phrase10[1].replace(".","?")
                    localite7['Réponse']=loc7.text
            questions['localités_partie']=localite7

            for per1 in doc.ents:
                if per1.label_=="MISC" and per1.root.dep_=="nmod":
                    phrase11=phrases[j].split(per1.text)
                    periode1['question']="En quelle période "+phrase11[0]+" ?"#ok
                    periode1['Réponse']=per1.text
            questions['période_nom']=periode1

            for per2 in doc.ents:
                if per2.label_=="MISC" and per2.root.dep_=="conj":
                    phrase12=phrases[j].split(per2.text)
                    periode2['question']="et en "+phrase12[1].replace(".","?")
                    periode2['Réponse']=per2.text
            questions['périodes_supplémentaires']=periode2

            for pers1 in doc.ents:
                if pers1.label_=="PER" and pers1.root.dep_=="ROOT":
                    phrase13=phrases[j].split(pers1.text)
                    personne1['question']="Qui "+phrase13[1].replace(".","?")
                    personne1['Réponse']=pers1.text
            questions['personnes']=personne1

            for pers2 in doc.ents:
                if pers2.label_=="PER" and pers2.root.dep_=="nsubj":
                    phrase14=phrases[j].split(pers2.text)
                    personne2['question']="Dans quelle localité "+phrase14[1].replace(".","?")
                    personne2['Réponse']=pers2.text
            questions['peronnes_sujets']=personne2

        return questions

def groupeNominal(texte):
    phrases=tokenisation_des_phrases(texte)
    motsCles=TotalMotsCles(texte)
    n=len(phrases)
    paire={}
    paire1={}
    paire2={}
    paire3={}
    paire4={}
    paire5={}
    paire6={}
    paire7={}
    paire8={}
    paire9={}
    for j in range(n):
        doc=nlp(phrases[j])
        for X in doc.noun_chunks:
            if X.root.pos_=="NOUN" and X.root.dep_=="nsubj:pass" and X.text in motsCles:#ok
                phrase1=phrases[j].split(X.text)
                paire1['question']="Qui "+phrase1[1].replace(".","?")
                paire1['réponse'] = X.text
                paire['nom_sujet_principal']=paire1

        for Y in doc.noun_chunks:
            if Y.root.pos_=="NOUN" and Y.root.dep_=="obj" and Y.text in motsCles:#ok
                phrase2=phrases[j].split(Y.text)
                paire2['question']="Qu'est ce que "+phrase2[0]#verbe entre les deux 
                paire2['réponse'] = Y.text
                paire['nom_COD']=paire2

        for Z in doc.noun_chunks:
            if Z.root.pos_=="NOUN" and Z.root.dep_=="root" and Z.text in motsCles:
                phrase3=phrases[j].split(Z.text)
                paire3['question']="Qu'est ce que "+phrase3[0]
                paire3['réponse'] = Z.text
                paire['nom_motif']=paire3

        for T in doc.noun_chunks:
            if T.root.pos_=="NOUN" and T.root.dep_=="nsubj" and T.text in motsCles:#ok
                phrase4=phrases[j].split(T.text)
                paire4['question']="Qui"+phrase4[1].replace(".","?")
                paire4['réponse'] = T.text
                paire['nom_sujet']=paire4
        
        for P in doc.noun_chunks:
            if P.root.pos_=="NOUN" and P.root.dep_=="nmod" and P.text in motsCles:#à vérifier
                phrase5=phrases[j].split(P.text)
                paire5['question']="Quelle entité"+phrase5[1].replace(".","?")
                paire5['réponse'] = P.text
                paire['nom_temps']=paire5
        
        for Q in doc.noun_chunks:
            if Q.root.pos_=="PROPN" and Q.root.dep_=="nmod" and Q.text in motsCles:#à vérifier
                phrase6=phrases[j].split(Q.text)
                paire6['question']="Quelle entité, "+phrase6[1].replace(".","?")
                paire6['réponse'] = Q.text
                paire['prop_temps']=paire6

        for R in doc.noun_chunks:
            if R.root.pos_=="PROPN" and R.root.dep_=="appos" and R.text in motsCles:
                phrase7=phrases[j].split(R.text)
                paire7['question']="Qui"+phrase7[1].replace(".","?")
                paire7['réponse'] = R.text
                paire['prop_apos']=paire7

        for S in doc.noun_chunks:
            if S.root.pos_=="PROPN" and S.root.dep_=="conj" and S.text in motsCles:#ok
                phrase8=phrases[j].split(S.text)
                paire8['question']="Quel"+phrase8[1].replace(".","?")
                paire8['réponse'] = S.text
                paire['prop_conj']=paire8

        for A in doc.noun_chunks:
            if A.root.pos_=="NOUN" and A.root.dep_=="conj" and A.text in motsCles:
                phrase9=phrases[j].split(A.text)
                paire9['question']="Comment est ce que "+phrase9[1].replace(".","?")
                paire9['réponse'] = A.text
                paire['non_conj']=paire9 
    return paire             
