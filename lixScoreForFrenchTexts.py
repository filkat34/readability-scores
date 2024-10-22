# Programme lix readability score for french texts
# but : calculer l'indice de lisibilité LIX d'un texte français
# auteur : Filippos

import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os

## Programme

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
    texte = texte.replace("  ", " ").replace("\\n", "") # supprimer les retours à la ligne et s'assurer qu'un seul espace sépare les mots
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
    filepath = filedialog.askopenfilename(
    filetypes=(("Text files", ("*.txt", "*.doc", "*.docx", "*.odt")),("PDF Files", ".pdf")))
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
    return f"Fichier : {filename}\n\nNombre de mots : {mots}\n\nNombre de mots longs : {motsLongs}\n\nNombre de phrases : {phrases}\n\nScore LIX : {lix}\n\nDifficulté : {difficulte}"

## GUI Tkinter

mainWindow = tk.Tk()
mainWindow.title("Calculateur d'indice de lisibilité LIX")


### Interactions utilisateur

def button_clicked():
    varPatientez.set('⌛ Patientez. Cela peut prendre du temps...')
    effacer()
    programmeLIX()
    varFichier.set(f"{filename}")
    varnbMots.set(f"{mots}")
    varnbMotsLongs.set(f"{motsLongs}")
    varnbPhrases.set(f"{phrases}")
    varlix.set(f"{lix}")
    varniveauDifficulte.set(f"{difficulte}")
    varPatientez.set('✅ Terminé !')

def effacer():
    varFichier.set("                        ")
    varnbMots.set("                        ")
    varnbMotsLongs.set("                        ")
    varnbPhrases.set("                        ")
    varlix.set("                        ")
    varniveauDifficulte.set("                        ")

### Textes et variables

intro="Ajoutez un fichier texte (txt, odt, doc, docx, pdf) pour calculer son indice de lisibilité LIX."
txtFichier="Fichier :"
txtNbMots="Nombre de mots :"
txtNbMotsLongs="Nombre de mots longs (>6 lettres) :"
txtNbPhrases="Nombre de phrases :"
txtLix="Score LIX :"
txtNiveauDifficulte="Niveau de difficulté :"

varFichier=tk.StringVar()
varFichier.set("                        ")
varnbMots=tk.StringVar()
varnbMots.set("                        ")
varnbMotsLongs=tk.StringVar()
varnbMotsLongs.set("                        ")
varnbPhrases=tk.StringVar()
varnbPhrases.set("                        ")
varlix=tk.StringVar()
varlix.set("                        ")
varniveauDifficulte=tk.StringVar()
varniveauDifficulte.set("                        ")
varPatientez=tk.StringVar()
varPatientez.set("⚠️ Le temps de chargement dépend de la longueur du texte.")

### Labels

introTexte=tk.Label(text=intro, justify="center")
patientez=tk.Label(textvariable=varPatientez, fg='red', justify='center')
resfichier=tk.Label(text=txtFichier)
resfichier1=tk.Label(textvariable=varFichier, fg='blue')
resnbMots= tk.Label(text=txtNbMots)
resnbMots1= tk.Label(textvariable=varnbMots, fg='blue')
resnbMotsLongs= tk.Label(text=txtNbMotsLongs)
resnbMotsLongs1= tk.Label(textvariable=varnbMotsLongs, fg='blue')
resnbPhrases= tk.Label(text=txtNbPhrases)
resnbPhrases1= tk.Label(textvariable=varnbPhrases, fg='blue')
reslix= tk.Label(text=txtLix)
reslix1= tk.Label(textvariable=varlix, fg='blue')
resniveauDifficulte= tk.Label(text=txtNiveauDifficulte)
resniveauDifficulte1= tk.Label(textvariable=varniveauDifficulte, fg='blue')

### Boutons

boutonAjouter = tk.Button(text ="Ajouter", command=lambda:button_clicked())

### Disposition sur la grille

introTexte.grid(row=0, column=0, sticky="w", columnspan=2, pady=10, padx=10)
boutonAjouter.grid(row=1, column=0, columnspan=2, pady=10, padx=10)
patientez.grid(row=2, column=0, columnspan=2, pady=10, padx=10)
resfichier.grid(row=3, column=0, sticky="e", pady=10, padx=10)
resfichier1.grid(row=3, column=1, sticky="w", pady=10, padx=10)
resnbMots.grid(row=4, column=0, sticky="e", pady=10, padx=10)
resnbMots1.grid(row=4, column=1, sticky="w", pady=10, padx=10)
resnbMotsLongs.grid(row=5, column=0, sticky="e", pady=10, padx=10)
resnbMotsLongs1.grid(row=5, column=1, sticky="w", pady=10, padx=10)
resnbPhrases.grid(row=6, column=0, sticky="e", pady=10, padx=10)
resnbPhrases1.grid(row=6, column=1, sticky="w", pady=10, padx=10)
reslix.grid(row=7, column=0, sticky="e", pady=10, padx=10)
reslix1.grid(row=7, column=1, sticky="w", pady=10, padx=10)
resniveauDifficulte.grid(row=8, column=0, sticky="e", pady=10, padx=10)
resniveauDifficulte1.grid(row=8, column=1, sticky="w", pady=10, padx=10)

mainWindow.mainloop()