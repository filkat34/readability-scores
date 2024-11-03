import re

def caracteres(str):
    return len(re.findall(r'\w', str))

def voyelles(str):
    return len(re.findall(r'[aeiouœéèàâûù]', str, re.I))

def digrammes(str):
    return len(re.findall(r'(au)|(eu)|(ou)|(oû)|(où)|(oi)|(œu)|(ei)|(ai)|(ée)|(que)|(qui)', str, re.I))

def trigrammes(str):
    return len(re.findall(r'(eau)|(oue)', str, re.I))

def syllabes_graphiques(str):
    return voyelles(str) - (digrammes(str)+trigrammes(str))

def mots(str):
    return len(re.findall(r'\w+', str))

def mots_plusdesixlettres(str):
    return len(re.findall(r'\w{7,}', str))

def mots_plusdetroissyllabes(str):
    mots_plusdetroissyllabes = 0
    for mot in str.split():
        if (len(re.findall(r'[aeiouœéèàâûù]', mot, re.I))-(len(re.findall(r'(au)|(eu)|(ou)|(oû)|(où)|(oi)|(œu)|(ei)|(ai)|(ée)|(que)|(qui)', mot, re.I))+len(re.findall(r'(eau)|(oue)', mot, re.I)))) >= 3 :
            mots_plusdetroissyllabes+=1
    return mots_plusdetroissyllabes

def phrases(str):
    return len(re.findall(r'\w{2,}\s?[.?!]', str))