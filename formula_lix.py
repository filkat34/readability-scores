from text_analysis import mots, phrases, mots_plusdesixlettres

def lix(str):
    lix=mots(str)/phrases(str)+100*(mots_plusdesixlettres(str)/mots(str))
    if lix > 60 :
        lix_difficulte = "Texte très difficile"
    elif lix >= 50:
        lix_difficulte = "Texte difficile"
    elif lix >= 40:
        lix_difficulte = "Texte de difficulté moyenne"
    elif lix >= 30:
        lix_difficulte = "Texte facile"
    else:
        lix_difficulte = "Très très facile"
    return lix, lix_difficulte