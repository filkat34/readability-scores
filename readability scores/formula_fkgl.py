from text_analysis import mots, phrases, syllabes_graphiques

def fkgl(str):
    fkgl=0.39*(mots(str)/phrases(str))+11.8*(syllabes_graphiques(str)/mots(str))-15.59
    if fkgl >= 15 :
        fkgl_difficulte = "Niveau master/doctorat"
    elif fkgl >= 13 :
        fkgl_difficulte = "Niveau licence"
    elif fkgl >= 12 :
        fkgl_difficulte = "Niveau terminale"
    elif fkgl >= 11 :
        fkgl_difficulte = "Niveau première"
    elif fkgl >= 10 :
        fkgl_difficulte = "Niveau seconde"
    elif fkgl >= 9 :
        fkgl_difficulte = "Niveau troisième"
    elif fkgl >= 8 :
        fkgl_difficulte = "Niveau quatrième"
    elif fkgl >= 7 :
        fkgl_difficulte = "Niveau cinquième"
    elif fkgl >= 6 :
        fkgl_difficulte = "Niveau sixième"
    elif fkgl >=5 :
        fkgl_difficulte = "Niveau CM2"
    elif fkgl >= 4 :
        fkgl_difficulte = "Niveau CM1"
    elif fkgl >= 3 :
        fkgl_difficulte = "Niveau CE2"
    elif fkgl >= 2 :
        fkgl_difficulte = "Niveau CE1"
    else:
        fkgl_difficulte = "Niveau CP"
    return fkgl, fkgl_difficulte