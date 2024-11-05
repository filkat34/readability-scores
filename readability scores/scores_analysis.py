"""Grade levels list"""
niveaux=["Maternelle/école élementaire", "Ecole élementaire", "Collège", "Lycée", "Licence", "Master/doctorat"]


def difficulte(score):
    """Returns the grade level for index scores : ARI, FKGL, Coleman-Liau, Gunning Fog, Smog """
    if score > 15 :
        return niveaux[5]
    if score > 12 :
        return niveaux[4]
    if score > 9 :
        return niveaux[3]
    if score > 6 :
        return niveaux[2]
    if score > 3 :
        return niveaux[1]
    return niveaux[0]


def difficulte_lix(score):
    """Returns the grade level for index score : LIX"""
    if score > 60 :
        return niveaux[5]
    if score > 56 :
        return niveaux[4]
    if score > 40 :
        return niveaux[3]
    if score > 28 :
        return niveaux[2]
    if score > 10 :
        return niveaux[1]
    return niveaux[0]


def difficulte_rix(score):
    """Returns the grade level for index score : RIX"""
    if score > 8:
        return niveaux[5]
    if score >= 7.2 :
        return niveaux[4]
    if score >= 4.5 :
        return niveaux[3]
    if score >= 1.8 :
        return niveaux[2]
    if score >= 0.2 :
        return niveaux[1]
    return niveaux[0]