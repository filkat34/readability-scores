import text_analysis
import formula_coleman_liau
import formula_lix
import formula_fkgl
import formula_smog
import formula_gunning
import formula_ari


def print_readability_scores(str):
    lix = formula_lix.lix(str)[0]
    lix_difficulte = formula_lix.lix(str)[1]
    gunning = formula_gunning.gunning(str)[0]
    gunning_difficulte = formula_gunning.gunning(str)[1]
    fkgl = formula_fkgl.fkgl(str)[0]
    fkgl_difficulte = formula_fkgl.fkgl(str)[1]
    coleman_liau = formula_coleman_liau.coleman_liau(str)[0]
    coleman_liau_difficulte = formula_coleman_liau.coleman_liau(str)[1]
    ari = formula_ari. ari(str)[0]
    ari_difficulte = formula_ari.ari(str)[1]
    smog = formula_smog.smog(str)[0]
    smog_difficulte = formula_smog.smog(str)[1]
    return print (f'''
                Les indices de lisibilité suivants ont été conçus pour l'Anglais. L'indice de lisibilité LIX
                est le plus fiable pour évaluer le niveau de difficulté des textes français.

                INDICES DE LISIBILITE
                ---------------------
                LIX................................ {lix} : {lix_difficulte}
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