def difficulte(score):
    if score >= 15 :
        return "Master/doctorat"
    elif score >= 13 :
        return "Licence"
    elif score >= 12 :
        return "Terminale"
    elif score >= 11 :
        return "Première"
    elif score >= 10 :
        return "Seconde"
    elif score >= 9 :
        return "Troisième"
    elif score >= 8 :
        return "Quatrième"
    elif score >= 7 :
        return "Cinquième"
    elif score >= 6 :
        return "Sixième"
    elif score >=5 :
        return "CM2"
    elif score >= 4 :
        return "CM1"
    elif score >= 3 :
        return "CE2"
    elif score >= 2 :
        return "CE1"
    else:
        return "CP"

def difficulte_lix(score):
    if score >= 60 :
        return "Master/doctorat"
    elif score >= 56 :
        return "Licence"
    elif score >= 52 :
        return "Terminale"
    elif score >= 48 :
        return "Première"
    elif score >= 44 :
        return "Seconde"
    elif score >= 40 :
        return "Troisième"
    elif score >= 36 :
        return "Quatrième"
    elif score >= 32 :
        return "Cinquième"
    elif score >= 28 :
        return "Sixième"
    elif score >= 24 :
        return "CM2"
    elif score >= 20 :
        return "CM1"
    elif score >= 15 :
        return "CE2"
    elif score >= 10 :
        return "CE1"
    else:
        return "CP"
    

def difficulte_rix(score):
    if score >= 7.2 :
        return "Université"
    elif score >= 6.2 :
        return "Terminale"
    elif score >= 5.3 :
        return "Première"
    elif score >= 4.5 :
        return "Seconde"
    elif score >= 3.7 :
        return "Troisième"
    elif score >= 3.0 :
        return "Quatrième"
    elif score >= 2.4 :
        return "Cinquième"
    elif score >= 1.8 :
        return "Sixième"
    elif score >= 1.3 :
        return "CM2"
    elif score >= 0.8 :
        return "CM1"
    elif score >= 0.5 :
        return "CE2"
    elif score >= 0.2 :
        return "CE1"
    else:
        return "CP"