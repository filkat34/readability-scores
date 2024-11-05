from math import sqrt
from text_analysis import caracteres, mots, phrases, syllabes_graphiques, mots_plusdesixlettres, mots_plusdetroissyllabes

def ari(txt):
    """Calculates the ARI readability score"""
    return 4.71*(caracteres(txt)/mots(txt))+0.5*(mots(txt)/phrases(txt))-21.43

def coleman_liau(txt):
    """Calculates the Coleman-Liau readability score"""
    return 5.88*(caracteres(txt)/mots(txt))-2.96*(phrases(txt)/mots(txt))-15.8

def fkgl(txt):
    """Calculates the Flesch-Kincaid Grade Level (FKGL)"""
    return 0.39*(mots(txt)/phrases(txt))+11.8*(syllabes_graphiques(txt)/mots(txt))-15.59

def gunning(txt):
    """Calculates the Gunning Fog Index"""
    return 0.4*((mots(txt)/phrases(txt))+100*(mots_plusdetroissyllabes(txt)/mots(txt)))

def lix(txt):
    """Calculates the LIX readability score"""
    return mots(txt)/phrases(txt)+100*(mots_plusdesixlettres(txt)/mots(txt))

def rix(txt):
    """Calculates the RIX readability score"""
    return mots_plusdesixlettres(txt)/phrases(txt)

def smog(txt):
    """Calculates the smog index"""
    return 1.043*(sqrt((mots_plusdetroissyllabes(txt)*30)/phrases(txt)))+3.1291