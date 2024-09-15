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


#Programme
cheminAcces = input("Saisissez le chemin d'accès du fichier texte (.txt) : ")
file = open(cheminAcces, encoding="utf8", errors='ignore')
texte = file.read()
file.close()
print("Nombre de phrases : ", nbPhrases(texte))
print("Nombre de mots : ", nbMots(texte))
print("Nombre de mots longs :", nbMotsLongs(texte))
indiceLix = calculLIX(nbMots(texte), nbPhrases(texte), nbMotsLongs(texte))
print("L'indice de lisibilité LIX est de : ", indiceLix)
if indiceLix > 60 :
    print("Texte très difficile.")
elif indiceLix >= 50:
    print("Texte difficile.")
elif indiceLix >= 40:
    print("Texte de difficulté moyenne.")
elif indiceLix >= 30:
    print("Texte facile.")
else:
    print("Texte très facile.")
