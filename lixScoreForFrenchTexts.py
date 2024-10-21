# Programme lix readability score for French texts
# but : calculer l'indice de lisibilité LIX d'un texte français
# auteur : Filippos

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
        difficulte = "Facile."
    else:
        difficulte = "Très facile"
    return scoreLix, difficulte

def programmeLIX():
    filename = filedialog.askopenfilename(
    filetypes=(
        ("Text files", ("*.txt", "*.doc", "*.docx", "*.odt")),
        ("PDF Files", ".pdf")))
    file = open(filename, encoding="utf8", errors='ignore')
    texte = file.read()
    file.close()
    Mots = compteurMots(texte)[0]
    MotsLongs = compteurMots(texte)[1]
    Phrases = nbPhrases(texte)
    Lix = scoreLix(compteurMots(texte)[0], compteurMots(texte)[1], nbPhrases(texte))[0]
    difficulte = scoreLix(compteurMots(texte)[0], compteurMots(texte)[1], nbPhrases(texte))[1]
    return print (f"Nombre de mots : {Mots}\nNombre de mots longs : {MotsLongs}\nNombre de phrases : {Phrases}\nScore LIX : {Lix}\nDifficulté : {difficulte}")


# Programme

programmeLIX()