from math import sqrt
from text_analysis import caracteres, mots, phrases, syllabes_graphiques, mots_plusdesixlettres, mots_plusdetroissyllabes

def ari(str):
    """Calculates the ARI readability score"""
    return 4.71*(caracteres(str)/mots(str))+0.5*(mots(str)/phrases(str))-21.43

def coleman_liau(str):
    """Calculates the Coleman-Liau readability score"""
    return 5.88*(caracteres(str)/mots(str))-2.96*(phrases(str)/mots(str))-15.8

def fkgl(str):
    """Calculates the Flesch-Kincaid Grade Level (FKGL)"""
    return 0.39*(mots(str)/phrases(str))+11.8*(syllabes_graphiques(str)/mots(str))-15.59

def gunning(str):
    """Calculates the Gunning Fog Index"""
    return 0.4*((mots(str)/phrases(str))+100*(mots_plusdetroissyllabes(str)/mots(str)))

def lix(str):
    """Calculates the LIX readability score"""
    return mots(str)/phrases(str)+100*(mots_plusdesixlettres(str)/mots(str))

def rix(str):
    """Calculates the RIX readability score"""
    return mots_plusdesixlettres(str)/phrases(str)

def smog(str):
    """Calculates the smog index"""
    return 1.043*(sqrt((mots_plusdetroissyllabes(str)*30)/phrases(str)))+3.1291



