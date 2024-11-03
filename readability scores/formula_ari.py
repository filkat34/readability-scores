from text_analysis import caracteres, mots, phrases

def ari(str):
    ari=4.71*(caracteres(str)/mots(str))+0.5*(mots(str)/phrases(str))-21.43
    if ari >= 15 :
        ari_difficulte = "Niveau master/doctorat"
    elif ari >= 13 :
        ari_difficulte = "Niveau licence"
    elif ari  >= 12 :
        ari_difficulte = "Niveau terminale"
    elif ari >= 11 :
        ari_difficulte = "Niveau première"
    elif ari >= 10 :
        ari_difficulte = "Niveau seconde"
    elif ari >= 9 :
        ari_difficulte = "Niveau troisième"
    elif ari >= 8 :
        ari_difficulte = "Niveau quatrième"
    elif ari >= 7 :
        ari_difficulte = "Niveau cinquième"
    elif ari >= 6 :
        ari_difficulte = "Niveau sixième"
    elif ari >=5 :
        ari_difficulte = "Niveau CM2"
    elif ari >= 4 :
        ari_difficulte = "Niveau CM1"
    elif ari >= 3 :
        ari_difficulte = "Niveau CE2"
    elif ari >= 2 :
        ari_difficulte = "Niveau CE1"
    else:
        ari_difficulte = "Niveau CP"
    return ari, ari_difficulte