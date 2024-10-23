# LIX readability score calculator for french texts(with Regex)
# but : calculer l'indice de lisibilité LIX d'un texte français
# auteur : Filippos

from tkinter import filedialog
import os
import re


## Fonctions

def nbMots(texte):
    return len(re.findall(r'\w+', texte))

def nbMotsLongs(texte):
    return len(re.findall(r'\w\w\w\w\w\w\w+', texte))

def nbPhrases(texte):
    texte = texte.replace('...', '.').replace("…", ".") # évite de comptabiliser les points de suspension comme trois ponctuations fortes
    return len(re.findall(r'[.!?]', texte))

def lixScore(nbMots,nbMotsLongs,nbPhrases):
    return (nbMots/nbPhrases)+(100*(nbMotsLongs/nbMots))

def niveauDifficulte(lixScore):
    if lixScore > 60 :
        return "Très difficile"
    elif lixScore >= 50:
        return "Difficile"
    elif lixScore >= 40:
        return "Moyenne"
    elif lixScore >= 30:
        return "Facile"
    else:
        return "Très facile"

## Programme

filepath = filedialog.askopenfilename(initialdir = "/desktop",
                                          title = "Choisissez un fichier .txt",
                                          filetype = (("txt files","*.txt"),("all files","*.*")))
file=open(filepath, encoding="utf8", errors='ignore')
texte=file.read()
file.close()
filename=os.path.basename(filepath)
nbMots=nbMots(texte)
nbMotsLongs=nbMotsLongs(texte)
nbPhrases=nbPhrases(texte)
lixScore=lixScore(nbMots,nbMotsLongs,nbPhrases)
niveauDifficulte=niveauDifficulte(lixScore)

print(f'''
      Fichier.................. {filename}
      Score LIX................ {lixScore}
      Difficulté............... {niveauDifficulte}
      Nombre de mots........... {nbMots}
      Nombre de mots longs..... {nbMotsLongs}
      Nombre de phrases........ {nbPhrases}
      ''')