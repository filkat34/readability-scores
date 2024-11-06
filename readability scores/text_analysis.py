import re

def caracteres(txt):
    """Counts the number of characters"""
    return len(re.findall(r'\w', txt))

def voyelles(txt):
    """Counts the number of vowels"""
    return len(re.findall(r'[aeiouœéèàâûù]', txt, re.I))

def digrammes(txt):
    """Counts the number of vowel digraphs"""
    return len(re.findall(r'(au)|(eu)|(ou)|(oû)|(où)|(oi)|(œu)|(ei)|(ai)|(ée)|(que)|(qui)', txt, re.I))

def trigrammes(txt):
    """Counts the number of vowel trigraphs"""
    return len(re.findall(r'(eau)|(oue)', txt, re.I))

def syllabes_graphiques(txt):
    """Counts the number of written syllables by substracting the number of bigraphs and trigraphs from the number of vowels"""
    return voyelles(txt) - (digrammes(txt)+trigrammes(txt))

def mots(txt):
    """Counts the number of words"""
    return len(re.findall(r'\w+', txt))

def mots_plusdesixlettres(txt):
    """Counts the number of words consisting of more than six letters"""
    return len(re.findall(r'\w{7,}', txt))

def mots_plusdetroissyllabes(txt):
    """Counts the number of words consisting of more than three syllables"""
    mots_polysyllabiques = 0
    for mot in txt.split():
        if (len(re.findall(r'[aeiouœéèàâûù]', mot, re.I))-(len(re.findall(r'(au)|(eu)|(ou)|(oû)|(où)|(oi)|(œu)|(ei)|(ai)|(ée)|(que)|(qui)', mot, re.I))+len(re.findall(r'(eau)|(oue)', mot, re.I)))) >= 3 :
            mots_polysyllabiques+=1
    return mots_polysyllabiques

def phrases(txt):
    """Counts the number of sentences"""
    if len(re.findall(r'\w{2,}\s?[.?!]', txt)) == 0:
        return 1 # Prevents ZeroDivison error
    return len(re.findall(r'\w{2,}\s?[.?!]', txt))