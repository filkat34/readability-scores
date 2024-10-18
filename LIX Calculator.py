#Programme : calculateur de score de lisibilité LIX pour textes français

#Identificateur de ponctuation forte
def estPonctuationForte(caractere):
    if caractere in ['.', '?', '!']:
        return True
    else:
        return False


#Formatage ponctuation du texte pour simplifier l'identification des phrases
#Evite que les points de suspension soient comptabilisés comme trois points
#Supprime les points qui ne marquent pas la fin d'une phrase mais une abréviation
def formatagePonctuation(texte):
    texte = texte.replace('...', '.')
    texte = texte.replace('’', "'")
    texte = texte.replace("…", ".")
    texte = texte.replace('M.', 'M')
    return texte


#Compteur de nombre de mots dans un texte
def nbMots(texte):
    texte = supprimePonctuation(texte)
    texte = texte.replace('\n', ' ').replace('\r', '')
    listeMots = str.split(texte)
    return len(listeMots)


# Compteur de mots de plus de 6 lettres
def nbMotsLongs(texte):
    texte = supprimePonctuation(texte)
    texte = texte.replace('\n', ' ').replace('\r', '')
    listeMots = str.split(texte)
    motsLongs = 0
    for mot in range(len(listeMots)):
        if len(listeMots[mot]) > 6:
            motsLongs += 1
    return motsLongs


#Compteur de phrases
def nbPhrases(texte):
    texte = formatagePonctuation(texte)
    nombre = 0
    for k in range(len(texte)):
        if estPonctuationForte(texte[k]):
                nombre += 1
    return nombre


#Supprime la ponctuantion du texte 
#Remplace l'apostrophe ainsi que le trait d'union par un espace
#Supprime l'apostrophe de mots anciennement composés mais qui ne comptent que pour un seul
def supprimePonctuation(texte):
    texte = texte.replace("aujourd'hui", "aujourdhui")
    texte = texte.replace("aujourd’hui", "aujourdhui")
    texte = texte.replace("’", " ")
    texte = texte.replace("'", " ")
    texte = texte.replace("-", " ")
    texte = texte.replace("“", "")
    texte = texte.replace("”", "")
    texte = texte.replace(".", "")
    texte = texte.replace("...", "")
    texte = texte.replace("…", "")
    texte = texte.replace("!", "")
    texte = texte.replace(";", "")
    texte = texte.replace("?", "")
    texte = texte.replace(":", "")
    texte = texte.replace(",", "")
    texte = texte.replace("—", "")
    texte = texte.replace("—", "")
    texte = texte.replace("\"", "")
    texte = texte.replace("(", "")
    texte = texte.replace(")", "")
    texte = texte.replace("[", "")
    texte = texte.replace("]", "")
    texte = texte.replace("  ", " ")
    texte = texte.replace("   ", " ")
    return texte


#Calcul de l'indice de lisibilité LIX
def calculLIX(nbMots,nbPhrases,nbMotsLongs):
    indiceLix = (nbMots/nbPhrases)+(100*(nbMotsLongs/nbMots))
    return indiceLix

#Niveau de difficulté

def difficulte(indiceLix):
    if indiceLix > 60 :
        return("Très difficile.")
    elif indiceLix >= 50:
        return("Difficile.")
    elif indiceLix >= 40:
        return("Difficulté moyenne.")
    elif indiceLix >= 30:
        return("Facile.")
    else:
        return("Très facile.")

#Programme
from tkinter import filedialog
import tkinter as tk

filename = filedialog.askopenfilename(
    filetypes=(
        ("Text files", ("*.txt", "*.doc", "*.docx", "*.odt")),
        ("PDF Files", ".pdf")
    )
)
file = open(filename, encoding="utf8", errors='ignore')
texte = file.read()
file.close()
print("Nombre de phrases : ", nbPhrases(texte))
print("Nombre de mots : ", nbMots(texte))
print("Nombre de mots longs :", nbMotsLongs(texte))
indiceLix = calculLIX(nbMots(texte), nbPhrases(texte), nbMotsLongs(texte))
print("L'indice de lisibilité LIX est de : ", indiceLix)
print("Niveau de difficulté :", difficulte(indiceLix))
