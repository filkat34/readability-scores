from text_analysis import caracteres, mots, phrases 

def coleman_liau(str):
    coleman_liau=5.88*(caracteres(str)/mots(str))-2.96*(phrases(str)/mots(str))-15.8
    if coleman_liau >= 15 :
        coleman_liau_difficulte = "Niveau master/doctorat"
    elif coleman_liau >= 13 :
        coleman_liau_difficulte = "Niveau licence"
    elif coleman_liau  >= 12 :
        coleman_liau_difficulte = "Niveau terminale"
    elif coleman_liau >= 11 :
        coleman_liau_difficulte = "Niveau première"
    elif coleman_liau >= 10 :
        coleman_liau_difficulte = "Niveau seconde"
    elif coleman_liau >= 9 :
        coleman_liau_difficulte = "Niveau troisième"
    elif coleman_liau >= 8 :
        coleman_liau_difficulte = "Niveau quatrième"
    elif coleman_liau >= 7 :
        coleman_liau_difficulte = "Niveau cinquième"
    elif coleman_liau >= 6 :
        coleman_liau_difficulte = "Niveau sixième"
    elif coleman_liau >=5 :
        coleman_liau_difficulte = "Niveau CM2"
    elif coleman_liau >= 4 :
        coleman_liau_difficulte = "Niveau CM1"
    elif coleman_liau >= 3 :
        coleman_liau_difficulte = "Niveau CE2"
    elif coleman_liau >= 2 :
        coleman_liau_difficulte = "Niveau CE1"
    else:
        coleman_liau_difficulte = "Niveau CP"
    return coleman_liau, coleman_liau_difficulte
        