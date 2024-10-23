# LIX readability score calculator for french texts(with Regex)
# but : calculer l'indice de lisibilité LIX d'un texte français
# auteur : Filippos

import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
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

def programmeLIX():
    filepath = filedialog.askopenfilename(title= "Chosissez un fichier en texte brut...",
    filetypes=(("Texte brut", ("*.txt")),("All Files", "*.*")))
    file = open(filepath, encoding="utf8", errors='ignore')
    texte = file.read()
    file.close()
    global filename
    filename = os.path.basename(filepath)
    global mots
    mots = nbMots(texte)
    global motsLongs
    motsLongs = nbMotsLongs(texte)
    global phrases
    phrases = nbPhrases(texte)
    global lix
    lix=lixScore(mots,motsLongs,phrases)
    global difficulte
    difficulte = niveauDifficulte(lix)
    return filename, mots, motsLongs, phrases, lix, difficulte

def affichageResultats():
    return f"Fichier : {filename}\n\nNombre de mots : {mots}\n\nNombre de mots longs : {motsLongs}\n\nNombre de phrases : {phrases}\n\nScore LIX : {lix}\n\nDifficulté : {difficulte}"

## GUI Tkinter

mainWindow = tk.Tk()
mainWindow.resizable(False, False)
mainWindow.title("Calculateur d'indice de lisibilité LIX")


### Interactions utilisateur

def button_clicked():
    vartermine.set('')
    varPatientez.set('⌛ Patientez. Cela peut prendre du temps...')
    effacer()
    programmeLIX()
    varFichier.set(f"{filename}")
    varnbMots.set(f"{mots}")
    varnbMotsLongs.set(f"{motsLongs}")
    varnbPhrases.set(f"{phrases}")
    varlix.set(f"{lix}")
    varniveauDifficulte.set(f"{difficulte}")
    varPatientez.set('')
    vartermine.set('✅ Terminé !')

def effacer():
    varFichier.set("")
    varnbMots.set("")
    varnbMotsLongs.set("")
    varnbPhrases.set("")
    varlix.set("")
    varniveauDifficulte.set("")

### Textes et variables

intro='''
L'indice de lisibilité LIX est une mesure développée par le linguiste 
suédois Carl-Hugo Björnsson vers 1968. 

Il est calculé en additionnant le nombre moyen de mots par phrase au 
pourcentage de mots longs (plus de six lettres) dans un texte donné. 

Plus l'indice LIX est élevé, plus le texte est difficile à lire.

Ajoutez un fichier texte brut (.txt) pour calculer son indice LIX.'''
txtFichier="Nom du fichier :"
txtNbMots="Nombre de mots :"
txtNbMotsLongs="Nombre de mots longs (>6 lettres) :"
txtNbPhrases="Nombre de phrases :"
txtLix="Score LIX :"
txtNiveauDifficulte="Niveau de difficulté :"

varFichier=tk.StringVar()
varFichier.set("")
varnbMots=tk.StringVar()
varnbMots.set("")
varnbMotsLongs=tk.StringVar()
varnbMotsLongs.set("")
varnbPhrases=tk.StringVar()
varnbPhrases.set("")
varlix=tk.StringVar()
varlix.set("")
varniveauDifficulte=tk.StringVar()
varniveauDifficulte.set("")
varPatientez=tk.StringVar()
varPatientez.set("⚠️ Le temps de chargement dépend de la longueur du texte.")
vartermine=tk.StringVar()
vartermine.set("")

### Labels

introTexte=tk.Label(text=intro, justify="left", font=('Monospace', 11))
patientez=tk.Label(textvariable=varPatientez, fg='red', justify='center', font=('Monospace', 11))
termine=tk.Label(textvariable=vartermine, fg='green', justify='center', font=('Monospace', 11))
resfichier=tk.Label(text=txtFichier, font=('Monospace', 11),justify="center")
resfichier1=tk.Label(textvariable=varFichier, fg='blue', font=('Monospace', 11))
resnbMots= tk.Label(text=txtNbMots, font=('Monospace', 11))
resnbMots1= tk.Label(textvariable=varnbMots, fg='green', font=('Monospace', 11))
resnbMotsLongs= tk.Label(text=txtNbMotsLongs, font=('Monospace', 11))
resnbMotsLongs1= tk.Label(textvariable=varnbMotsLongs, font=('Monospace', 11), fg='green')
resnbPhrases= tk.Label(text=txtNbPhrases, font=('Monospace', 11))
resnbPhrases1= tk.Label(textvariable=varnbPhrases, fg='green', font=('Monospace', 11))
reslix= tk.Label(text=txtLix, font=('Monospace', 11))
reslix1= tk.Label(textvariable=varlix, fg='green', font=('Monospace', 11))
resniveauDifficulte= tk.Label(text=txtNiveauDifficulte, font=('Monospace', 11))
resniveauDifficulte1= tk.Label(textvariable=varniveauDifficulte, fg='green', font=('Monospace', 11))

### Boutons

boutonAjouter = tk.Button(text ="Ajouter texte", font=('Monospace', 11), command=lambda:button_clicked())

### Disposition sur la grille

introTexte.grid(row=0, column=0, columnspan=2, pady=5, padx=20)
boutonAjouter.grid(row=1, column=0, columnspan=2, pady=5, padx=10)
patientez.grid(row=2, column=0, columnspan=2, pady=0, padx=10)
termine.grid(row=3, column=0, columnspan=2, pady=0, padx=10)
resfichier.grid(row=4, column=0, columnspan=2, pady=5, padx=20)
resfichier1.grid(row=5, column=0, columnspan=2, pady=5, padx=20)
resnbMots.grid(row=6, column=0, sticky="w", pady=5, padx=20)
resnbMots1.grid(row=6, column=1, sticky="w", pady=5, padx=20)
resnbMotsLongs.grid(row=7, column=0, sticky="w", pady=5, padx=20)
resnbMotsLongs1.grid(row=7, column=1, sticky="w", pady=5, padx=20)
resnbPhrases.grid(row=8, column=0, sticky="w", pady=5, padx=20)
resnbPhrases1.grid(row=8, column=1, sticky="w", pady=5, padx=20)
reslix.grid(row=9, column=0, sticky="w", pady=5, padx=20)
reslix1.grid(row=9, column=1,sticky="w", pady=5, padx=20)
resniveauDifficulte.grid(row=10, column=0, sticky="w", pady=5, padx=20)
resniveauDifficulte1.grid(row=10, column=1, sticky="w", pady=5, padx=20)

mainWindow.mainloop()