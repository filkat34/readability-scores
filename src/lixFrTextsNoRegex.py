# LIX readability score calculator for french texts(without Regex)
# but : calculer l'indice de lisibilité LIX d'un texte français
# auteur : Filippos

import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os

## Fonctions

def nbPhrases(texte):
    texte = texte.replace('...', '.').replace("…", ".")
    nbPonctuationForte = 0
    for caractere in range(len(texte)):
        if texte[caractere] in ['.', '?', '!']:
            nbPonctuationForte+=1
    nbPhrases=nbPonctuationForte
    return nbPhrases

def compteurMots(texte):
    texte = texte.replace("’", " ").replace("'", " ") # séparer le mot élidé du suivant par un espace
    texte = texte.replace("-", " ") # remplacer trait d'union par espace pour séparer les mots lors d'une inversion sujet-verbe
    texte = texte.replace("  ", " ") # supprimer les retours à la ligne et s'assurer qu'un seul espace sépare les mots
    ponctuation = ['!','(',')','-','[',']','{','}',';',':',\
        '«','»',"'",'"','\\','<','>','.', '/', '?', '@', '#',\
         '$', '%','^','&','*','_','~','...', "…"]
    for element in texte:
        if element in ponctuation:
            texte=texte.replace(element,"")
    listeMots = str.split(texte)
    nbMots=len(listeMots)
    nbMotsLongs=0
    for mot in range(len(listeMots)):
        if len(listeMots[mot]) > 6:
            nbMotsLongs += 1
    return nbMots, nbMotsLongs

def scoreLix(nbMots, nbMotsLongs, nbPhrases):
    scoreLix = (nbMots/nbPhrases)+(100*(nbMotsLongs/nbMots))
    difficulte =''
    if scoreLix > 60 :
        difficulte = "Très difficile"
    elif scoreLix >= 50:
        difficulte = "Difficile"
    elif scoreLix >= 40:
        difficulte = "Moyenne"
    elif scoreLix >= 30:
        difficulte = "Facile"
    else:
        difficulte = "Très facile"
    return scoreLix, difficulte

def programmeLIX():
    filepath = filedialog.askopenfilename(initialdir = "/desktop",
                                          title = "Choisissez un fichier .txt",
                                          filetype = (("txt files","*.txt"),("all files","*.*")))
    file = open(filepath, encoding="utf8", errors='ignore')
    texte = file.read()
    file.close()
    global filename
    filename = os.path.basename(filepath)
    global mots
    mots = compteurMots(texte)[0]
    global motsLongs
    motsLongs = compteurMots(texte)[1]
    global phrases
    phrases = nbPhrases(texte)
    global lix
    lix = scoreLix(compteurMots(texte)[0], compteurMots(texte)[1], nbPhrases(texte))[0]
    global difficulte
    difficulte = scoreLix(compteurMots(texte)[0], compteurMots(texte)[1], nbPhrases(texte))[1]
    return filename, mots, motsLongs, phrases, lix, difficulte

def affichageResultats():
    return print(f'''
      Fichier.................. {filename}
      Score LIX................ {lix}
      Difficulté............... {difficulte}
      Nombre de mots........... {mots}
      Nombre de mots longs..... {motsLongs}
      Nombre de phrases........ {phrases}
      ''')

## Programme

programmeLIX()
affichageResultats()
