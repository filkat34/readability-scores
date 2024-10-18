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
    texte = texte.replace("\[", "")
    texte = texte.replace("\]", "")
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
        return("Très difficile")
    elif indiceLix >= 50:
        return("Difficile")
    elif indiceLix >= 40:
        return("Difficulté moyenne")
    elif indiceLix >= 30:
        return("Facile")
    else:
        return("Très facile")
    
#Fenêtres de l'interface

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


def window_results():
    secondary_window = tk.Toplevel()
    secondary_window.title(f"{filename}")
    secondary_window.minsize(550,350)
    secondary_window.maxsize(1200,400)
    secondary_window.geometry("550x350+550+0")
    secondary_window.config(width=500, height=600)
    phrases = nbPhrases(texte)
    mots = nbMots(texte)
    motsLongs = nbMotsLongs(texte)
    lix = calculLIX(nbMots(texte),nbPhrases(texte),nbMotsLongs(texte))
    niveauDifficulte = difficulte(lix)
    results1 = tk.Label(secondary_window, text =f'Nombre de phrases : {phrases}',
                       padx= 20, pady= 20, justify="left", font=("Monospace", 12))
    results1.pack(anchor="w")
    results2 = tk.Label(secondary_window, text =f'Nombre de mots : {mots}',
                       padx= 20, pady= 20, justify="left", font=("Monospace", 12))
    results2.pack(anchor="w")
    results3 = tk.Label(secondary_window, text =f'Nombre de mots longs : {motsLongs}',
                       padx= 20, pady= 20, justify="left", font=("Monospace", 12))
    results3.pack(anchor="w")
    results4 = tk.Label(secondary_window, text =f'Indice de lisibilité LIX : {lix}',
                       padx= 20, pady= 20, justify="left", font=("Monospace", 12))
    results4.pack(anchor="w")
    results5 = tk.Label(secondary_window, text =f'Niveau de difficulté : {niveauDifficulte}',
                       padx= 20, pady= 20, justify="left", font=("Monospace", 12))
    results5.pack(anchor="w")

def button_clicked():
    global filename
    filename = filedialog.askopenfilename(
    filetypes=(
        ("Text files", ("*.txt", "*.doc", "*.docx", "*.odt")),
        ("PDF Files", ".pdf")
    )  
    )
    file = open(filename, encoding="utf8", errors='ignore')
    global texte 
    texte = 'text'
    texte = file.read()
    file.close()
    window_results()

#Programme interface

root = tk.Tk()
root.title("Calculateur d'indice LIX")
root.minsize(500,150)
root.maxsize(600,300)
root.geometry("500x150+0+0")
invit = tk.Label(text="Ajoutez un fichier texte (txt, odt, doc, docx, pdf) \n pour calculer son indice de lisibilité LIX.",
                     padx= 5, pady= 5, font=("Monospace", 11))
invit.pack()
button = tk.Button(root, 
                   text="Ajouter", 
                   command=lambda:button_clicked(),
                   activebackground="grey", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Monospace", 11),
                   height=1,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=5,
                   pady=5,
                   width=10,
                   wraplength=100)
button.pack(padx=10, pady=15)
root.mainloop()
