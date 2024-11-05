import text_analysis
import readability_formulas
import scores_analysis


def print_readability_scores(str):
    lix = readability_formulas.lix(str)
    lix_difficulte = scores_analysis.difficulte_lix(lix)
    rix = readability_formulas.rix(str)
    rix_difficulte = scores_analysis.difficulte_rix(rix)
    gunning = readability_formulas.gunning(str)
    gunning_difficulte = scores_analysis.difficulte(gunning)
    fkgl = readability_formulas.fkgl(str)
    fkgl_difficulte = scores_analysis.difficulte(fkgl)
    coleman_liau = readability_formulas.coleman_liau(str)
    coleman_liau_difficulte = scores_analysis.difficulte(coleman_liau)
    ari = readability_formulas.ari(str)
    ari_difficulte = scores_analysis.difficulte(ari)
    smog = readability_formulas.smog(str)
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
    
def print_text_statistics(str):
    caracteres = text_analysis.caracteres(str)
    voyelles = text_analysis.voyelles(str)
    digrammes = text_analysis.digrammes(str)
    trigrammes = text_analysis.trigrammes(str)
    syllabes_graphiques = text_analysis.syllabes_graphiques(str)
    mots = text_analysis.mots(str)
    mots_plusdesixlettres = text_analysis.mots_plusdesixlettres(str)
    mots_plusdetroissyllabes = text_analysis.mots_plusdetroissyllabes(str)
    phrases = text_analysis.phrases(str)
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