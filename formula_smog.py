from text_analysis import mots_plusdetroissyllabes, phrases
from math import sqrt
 
def smog(str):
    smog = 1.043*(sqrt((mots_plusdetroissyllabes(str)*30)/phrases(str)))+3.1291
    if smog >= 15 :
        smog_difficulte = "Niveau master/doctorat"
    elif smog >= 13 :
        smog_difficulte = "Niveau licence"
    elif smog  >= 12 :
        smog_difficulte = "Niveau terminale"
    elif smog >= 11 :
        smog_difficulte = "Niveau première"
    elif smog >= 10 :
        smog_difficulte = "Niveau seconde"
    elif smog >= 9 :
        smog_difficulte = "Niveau troisième"
    elif smog >= 8 :
        smog_difficulte = "Niveau quatrième"
    elif smog >= 7 :
        smog_difficulte = "Niveau cinquième"
    elif smog >= 6 :
        smog_difficulte = "Niveau sixième"
    elif smog >=5 :
        smog_difficulte = "Niveau CM2"
    elif smog >= 4 :
        smog_difficulte = "Niveau CM1"
    elif smog >= 3 :
        smog_difficulte = "Niveau CE2"
    elif smog >= 2 :
        smog_difficulte = "Niveau CE1"
    else:
        smog_difficulte = "Niveau CP"
    return smog, smog_difficulte