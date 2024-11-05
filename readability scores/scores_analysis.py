"""Grade levels list"""
niveau = ["CP", "CE1", "CE2", "CM1", "CM2", "Sixième", "Cinquième", "Quatrième", "Troisième",
           "Seconde", "Première", "Terminale", "Licence", "Master/Doctorat" ]  

def difficulte(score):
    """Returns the grade level for index scores : ARI, FKGL, Coleman-Liau, Gunning Fog, Smog """
    if score >= 15 :
        return niveau[13]
    elif score >= 13 :
        return niveau [12]
    elif score >= 12 :
        return niveau[11]
    elif score >= 11 :
        return niveau[10]
    elif score >= 10 :
        return niveau[9]
    elif score >= 9 :
        return niveau[8]
    elif score >= 8 :
        return niveau[7]
    elif score >= 7 :
        return niveau[6]
    elif score >= 6 :
        return niveau[5]
    elif score >=5 :
        return niveau[4]
    elif score >= 4 :
        return niveau[3]
    elif score >= 3 :
        return niveau[2]
    elif score >= 2 :
        return niveau[1]
    else:
        return niveau[0]

def difficulte_lix(score):
    """Returns the grade level for index score : LIX"""
    if score >= 60 :
        return niveau[13]
    elif score >= 56 :
        return niveau[12]
    elif score >= 52 :
        return niveau[11]
    elif score >= 48 :
        return niveau[10]
    elif score >= 44 :
        return niveau[9]
    elif score >= 40 :
        return niveau[8]
    elif score >= 36 :
        return niveau[7]
    elif score >= 32 :
        return niveau[6]
    elif score >= 28 :
        return niveau[5]
    elif score >= 24 :
        return niveau[4]
    elif score >= 20 :
        return niveau[3]
    elif score >= 15 :
        return niveau[2]
    elif score >= 10 :
        return niveau[1]
    else:
        return niveau[0]
    

def difficulte_rix(score):
    """Returns the grade level for index score : RIX"""
    if score > 8:
        return niveau[13]
    elif score >= 7.2 :
        return niveau[12]
    elif score >= 6.2 :
        return niveau[11]
    elif score >= 5.3 :
        return niveau[10]
    elif score >= 4.5 :
        return niveau[9]
    elif score >= 3.7 :
        return niveau[8]
    elif score >= 3.0 :
        return niveau[7]
    elif score >= 2.4 :
        return niveau[6]
    elif score >= 1.8 :
        return niveau[5]
    elif score >= 1.3 :
        return niveau[4]
    elif score >= 0.8 :
        return niveau[3]
    elif score >= 0.5 :
        return niveau[2]
    elif score >= 0.2 :
        return niveau[1]
    else:
        return niveau[0]