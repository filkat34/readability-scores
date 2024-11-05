import re

def caracteres(str):
    """Counts the number of characters"""
    return len(re.findall(r'\w', str))

def voyelles(str):
    """Counts the number of vowels"""
    return len(re.findall(r'[aeiouœéèàâûù]', str, re.I))

def digrammes(str):
    """Counts the number of vowel digraphs"""
    return len(re.findall(r'(au)|(eu)|(ou)|(oû)|(où)|(oi)|(œu)|(ei)|(ai)|(ée)|(que)|(qui)', str, re.I))

def trigrammes(str):
    """Counts the number of vowel trigraphs"""
    return len(re.findall(r'(eau)|(oue)', str, re.I))

def syllabes_graphiques(str):
    """Counts the number of written syllables by substracting the number of bigraphs and trigraphs from the number of vowels"""
    return voyelles(str) - (digrammes(str)+trigrammes(str))

def mots(str):
    """Counts the number of words"""
    return len(re.findall(r'\w+', str))

def mots_plusdesixlettres(str):
    """Counts the number of words consisting of more than six letters"""
    return len(re.findall(r'\w{7,}', str))

def mots_plusdetroissyllabes(str):
    """Counts the number of words consisting of more than three syllables"""
    mots_polysyllabiques = 0
    for mot in str.split():
        if (len(re.findall(r'[aeiouœéèàâûù]', mot, re.I))-(len(re.findall(r'(au)|(eu)|(ou)|(oû)|(où)|(oi)|(œu)|(ei)|(ai)|(ée)|(que)|(qui)', mot, re.I))+len(re.findall(r'(eau)|(oue)', mot, re.I)))) >= 3 :
            mots_polysyllabiques+=1
    return mots_polysyllabiques

def phrases(str):
    """Counts the number of sentences"""
    return len(re.findall(r'\w{2,}\s?[.?!]', str))