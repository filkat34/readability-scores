from tkinter import filedialog
import os
import re


## Fonctions

def nb_mots(str):
    return len(re.findall(r'\w+', str))

def nb_mots_longs(str):
    return len(re.findall(r'\w\w\w\w\w\w\w+', str))

def nb_phrases(str):
    return len(re.findall(r'\w\w+\s?[.?!]', str))

def lix_score(str):
    return (nb_mots(str)/nb_phrases(str))+(100*(nb_mots_longs(str)/nb_mots(str)))

def niveau_difficulte(score):
    if score > 60 :
        return "Très difficile"
    elif score >= 50:
        return "Difficile"
    elif score >= 40:
        return "Moyenne"
    elif score >= 30:
        return "Facile"
    else:
        return "Très facile"


## Programme

filepath = filedialog.askopenfilename(title= "Chosissez un fichier en texte brut...",
    filetypes=(("Texte brut", ("*.txt")),("All Files", "*.*")))
file=open(filepath, encoding="utf8", errors='ignore')
texte=file.read()
file.close()
filename=os.path.basename(filepath)
mots=nb_mots(texte)
mots_longs=nb_mots_longs(texte)
phrases=nb_phrases(texte)
lix=lix_score(texte)
difficulte=niveau_difficulte(lix)

print(f'''
      Fichier.................. {filename}
      Score LIX................ {lix}
      Difficulté............... {difficulte}
      Nombre de mots........... {mots}
      Nombre de mots longs..... {mots_longs}
      Nombre de phrases........ {phrases}
      ''')