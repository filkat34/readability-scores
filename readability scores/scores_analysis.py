"""Grade levels list"""
niveau = ["CP", "CE1", "CE2", "CM1", "CM2", "Sixième", "Cinquième", "Quatrième", "Troisième",
           "Seconde", "Première", "Terminale", "Licence", "Master/Doctorat" ]  


def difficulte(score):
    """Returns the grade level for index scores : ARI, FKGL, Coleman-Liau, Gunning Fog, Smog """
    if score >= 15 :
        return niveau[13]
    if score >= 13 :
        return niveau [12]
    if score >= 12 :
        return niveau[11]
    if score >= 11 :
        return niveau[10]
    if score >= 10 :
        return niveau[9]
    if score >= 9 :
        return niveau[8]
    if score >= 8 :
        return niveau[7]
    if score >= 7 :
        return niveau[6]
    if score >= 6 :
        return niveau[5]
    if score >=5 :
        return niveau[4]
    if score >= 4 :
        return niveau[3]
    if score >= 3 :
        return niveau[2]
    if score >= 2 :
        return niveau[1]
    return niveau[0]


def difficulte_lix(score):
    """Returns the grade level for index score : LIX"""
    if score >= 60 :
        return niveau[13]
    if score >= 56 :
        return niveau[12]
    if score >= 52 :
        return niveau[11]
    if score >= 48 :
        return niveau[10]
    if score >= 44 :
        return niveau[9]
    if score >= 40 :
        return niveau[8]
    if score >= 36 :
        return niveau[7]
    if score >= 32 :
        return niveau[6]
    if score >= 28 :
        return niveau[5]
    if score >= 24 :
        return niveau[4]
    if score >= 20 :
        return niveau[3]
    if score >= 15 :
        return niveau[2]
    if score >= 10 :
        return niveau[1]
    return niveau[0]

def difficulte_rix(score):
    """Returns the grade level for index score : RIX"""
    if score > 8:
        return niveau[13]
    if score >= 7.2 :
        return niveau[12]
    if score >= 6.2 :
        return niveau[11]
    if score >= 5.3 :
        return niveau[10]
    if score >= 4.5 :
        return niveau[9]
    if score >= 3.7 :
        return niveau[8]
    if score >= 3.0 :
        return niveau[7]
    if score >= 2.4 :
        return niveau[6]
    if score >= 1.8 :
        return niveau[5]
    if score >= 1.3 :
        return niveau[4]
    if score >= 0.8 :
        return niveau[3]
    if score >= 0.5 :
        return niveau[2]
    if score >= 0.2 :
        return niveau[1]
    return niveau[0]