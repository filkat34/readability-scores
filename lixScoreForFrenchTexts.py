# Programme lix readability score for French texts
# but : calculer l'indice de lisibilité LIX d'un texte français
# auteur : Filippos

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# Fonctions

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
        difficulte = "Difficulté moyenne"
    elif scoreLix >= 30:
        difficulte = "Facile"
    else:
        difficulte = "Très facile"
    return scoreLix, difficulte

def programmeLIX():
    global filename
    filename = filedialog.askopenfilename(
    filetypes=(("Text files", ("*.txt", "*.doc", "*.docx", "*.odt")),("PDF Files", ".pdf")))
    file = open(filename, encoding="utf8", errors='ignore')
    texte = file.read()
    file.close()
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
    return filename,mots, motsLongs, phrases, lix, difficulte

def affichageResultats():
    return f"Nombre de mots : {mots}\n\nNombre de mots longs : {motsLongs}\n\nNombre de phrases : {phrases}\n\nScore LIX : {lix}\n\nDifficulté : {difficulte}"

# Interface du programme

root = tk.Tk()
root.title("Calculateur d'indice de lisibilité LIX")
root.minsize(500,200)
root.maxsize(600,300)
root.geometry("500x200+0+0")
userInput = tk.Label(text="Ajoutez un fichier texte (txt, odt, doc, docx, pdf)\n pour calculer son indice de lisibilité LIX.\n\nLe temps de chargement dépend de la longueur du texte.\n\n⌛ Patientez...",
                     padx= 10, pady= 10, font=("Monospace", 12))
userInput.pack()

def button_clicked():
    programmeLIX()
    window_results()

def window_results():
    resultats = tk.Toplevel()
    resultats.title(f"{filename}")
    resultats.minsize(300,300)
    resultats.maxsize(1200,400)
    resultats.geometry("300x300+550+0")
    resultats.config(width=500, height=600)
    resultatsDetail = tk.Label(resultats, text=affichageResultats(),
                        padx= 20, pady= 20, justify="left", font=("Monospace", 12))
    resultatsDetail.pack(anchor="w")
    button = tk.Button(resultats, 
                   text="Quitter", 
                   command=resultats.destroy,
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