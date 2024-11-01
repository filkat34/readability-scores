from tkinter import filedialog
import os
import re


def scores_lisibilite():
    filepath = filedialog.askopenfilename(title= "Chosissez un fichier en texte brut...",
    filetypes=(("Texte brut", ("*.txt")),("All Files", "*.*")))
    file=open(filepath, encoding="utf8", errors='ignore')
    texte=file.read()
    file.close()
    caracteres=len(re.findall(r'\w', texte))
    voyelles=len(re.findall(r'[aeiouœuAEIOUŒ]', texte))
    e_caducs=len(re.findall(r'ée|ées|[aeiouAEIOU]e|\w\we\b|\w\wes\b', texte))
    diphtongues=len(re.findall(r'eu|E|oi|Oi|eu|Eu|au|Au|ou|Ou|eau|Eau|oeu|Oeu|Œu|œu', texte))
    triphtongues=len(re.findall(r'eau|Eau|oeu|Oeu|Œu|œu', texte))
    syllabes = voyelles-(e_caducs+diphtongues+triphtongues)
    mots=len(re.findall(r'\w+', texte))
    mots_longs=len(re.findall(r'\w\w\w\w\w\w\w+', texte))
    phrases=len(re.findall(r'\w\w+\s?[.?!]', texte))
    if phrases == 0 or mots == 0 :
        return "Votre texte ne comporte aucune ponctuation forte. Le calcul du score est impossible."
    else:
        lix=mots/phrases+100*(mots_longs/mots)
        automated_ri=4.71*(caracteres/mots)+0.5*(mots/phrases)-21.43
        flesch_kincaid=206.835-1.015*(mots/phrases)-84.6*(syllabes/mots)
        coleman_liau=(0.0588*((caracteres/mots)*100))-(0.296*((phrases/mots)*100))-15.8
        return f'''
                INDICES DE LISIBILITE
                ---------------------

                Automated readability index........ {automated_ri}
                Score LIX.......................... {lix}
                Flesch Kincaid..................... {flesch_kincaid}
                Indice de Coleman-Liau............. {coleman_liau}

                STATISTIQUES DU TEXTE
                ---------------------

                Caractères......................... {caracteres}
                Voyelles........................... {voyelles}
                e caducs........................... {e_caducs}
                Diphtongues........................ {diphtongues}
                Triphtongues....................... {triphtongues}
                Syllabes........................... {syllabes}
                Mots............................... {mots}
                Mots Longs......................... {mots_longs}
                Phrases............................ {phrases}
                '''
    
print(scores_lisibilite())