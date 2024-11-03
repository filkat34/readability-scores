from text_analysis import mots, phrases, mots_plusdetroissyllabes

def gunning(str):
    gunning=0.4*((mots(str)/phrases(str))+100*(mots_plusdetroissyllabes(str)/mots(str)))
    if gunning >= 15 :
        gunning_difficulte = "Niveau master/doctorat"
    elif gunning >= 13 :
        gunning_difficulte = "Niveau licence"
    elif gunning >= 12 :
        gunning_difficulte = "Niveau terminale"
    elif gunning >= 11 :
        gunning_difficulte = "Niveau première"
    elif gunning >= 10 :
        gunning_difficulte = "Niveau seconde"
    elif gunning >= 9 :
        gunning_difficulte = "Niveau troisième"
    elif gunning >= 8 :
        gunning_difficulte = "Niveau quatrième"
    elif gunning >= 7 :
        gunning_difficulte = "Niveau cinquième"
    elif gunning >= 6 :
        gunning_difficulte = "Niveau sixième"
    elif gunning >=5 :
        gunning_difficulte = "Niveau CM2"
    elif gunning >= 4 :
        gunning_difficulte = "Niveau CM1"
    elif gunning >= 3 :
        gunning_difficulte = "Niveau CE2"
    elif gunning >= 2 :
        gunning_difficulte = "Niveau CE1"
    else:
        gunning_difficulte = "Niveau CP"
    return gunning, gunning_difficulte
