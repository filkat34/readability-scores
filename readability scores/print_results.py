import text_analysis
import readability_formulas
import scores_analysis


def print_readability_scores(txt):
    """Prints the readability scores and the grade levels corresponding"""
    lix = readability_formulas.lix(txt)
    lix_difficulte = scores_analysis.difficulte_lix(lix)
    rix = readability_formulas.rix(txt)
    rix_difficulte = scores_analysis.difficulte_rix(rix)
    gunning = readability_formulas.gunning(txt)
    gunning_difficulte = scores_analysis.difficulte(gunning)
    fkgl = readability_formulas.fkgl(txt)
    fkgl_difficulte = scores_analysis.difficulte(fkgl)
    coleman_liau = readability_formulas.coleman_liau(txt)
    coleman_liau_difficulte = scores_analysis.difficulte(coleman_liau)
    ari = readability_formulas.ari(txt)
    ari_difficulte = scores_analysis.difficulte(ari)
    smog = readability_formulas.smog(txt)
    smog_difficulte = scores_analysis.difficulte(smog)
    return print (f'''
                Les indices de lisibilité suivants ont été conçus pour l'Anglais. Les indices de lisibilité LIX
                et RIX sont les plus fiables pour évaluer le niveau de difficulté des textes français.

                INDICES DE LISIBILITE
                ---------------------
                LIX................................ {lix} : {lix_difficulte}
                RIX................................ {rix} : {rix_difficulte}
                Gunning............................ {gunning} : {gunning_difficulte}
                Flesch-Kincaid..................... {fkgl} : {fkgl_difficulte} 
                Coleman-Liau....................... {coleman_liau} : {coleman_liau_difficulte}
                Automated readability index........ {ari} : {ari_difficulte}
                SMOG............................... {smog} : {smog_difficulte}''')

def print_text_statistics(txt):
    """Prints the text stastistics that served to calculate the readability scores"""
    caracteres = text_analysis.caracteres(txt)
    voyelles = text_analysis.voyelles(txt)
    digrammes = text_analysis.digrammes(txt)
    trigrammes = text_analysis.trigrammes(txt)
    syllabes_graphiques = text_analysis.syllabes_graphiques(txt)
    mots = text_analysis.mots(txt)
    mots_plusdesixlettres = text_analysis.mots_plusdesixlettres(txt)
    mots_plusdetroissyllabes = text_analysis.mots_plusdetroissyllabes(txt)
    phrases = text_analysis.phrases(txt)
    return print(f'''
                STATISTIQUES DU TEXTE
                ---------------------
                Caractères......................... {caracteres}
                Voyelles........................... {voyelles}
                Digrammmes......................... {digrammes}
                Trigrammes......................... {trigrammes}
                Syllabes graphiques................ {syllabes_graphiques}
                Mots............................... {mots}
                Mots Longs (>6 lettres)............ {mots_plusdesixlettres}
                Mots complexes (>3 syllabes)....... {mots_plusdetroissyllabes}
                Phrases............................ {phrases}
                ''')