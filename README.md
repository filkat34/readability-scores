# Scores de lisibilité pour textes français

## Objectif 

L'objectif de ce programme est de permettre, à partir d'un fichier en texte brut (.txt) fourni par l'utilisateur, le calcul de six scores de lisibilité : LIX, Automated RI, Gunning fog, Coleman-Liau, Flesch-Kincaid, Smog.

Ce programme permet aussi l'affichage des statistiques du texte sur lesquelles il s'est fondé pour effectuer le calcul, notamment les nombres de caractères, voyelles, digrammes, trigrammes, syllabes, mots, mots de plus de six caractères, mots de plus de trois syllabes, phrases.

## Description

Ce programme repose entièrement sur les expressions régulières pour établir les variables qui servent au calcul des scores de lisibilité. 

Si les expressions régulières apportent une réponse algorithmique efficace pour la grande majorité des variables à établir, elles se revèlent moins précises, bien que souvent suffisantes, pour calculer le nombre de syllabes d'un mot. Cela est étroitement lié à la complexité et à l'irrégularité de la langue française. 

Pour faire face à ce problème et afin que les résultats soient fiables, il a été décidé de procéder au décompte des syllabes graphiques et non phoniques : pour ce faire on comptabilise d'abord le nombre de voyelles dans un mot donné ; ensuite, on soustrait à cette somme le nombre de digrammes et de trigrammes qui se trouvent dans le mot.

## Bibliographie

* Benoît J.-P., <a href="https://www.persee.fr/doc/prati_0338-2389_1986_num_52_1_1409">"60 ans de formules de lisibilité : qu'en reste-t-il ?"</a>
* Conquet A., <a href="https://www.persee.fr/doc/colan_0336-1500_1973_num_17_1_3978">"Cinq méthodes de mesure de la lisibilité"</a>
* Henry G., <a href="https://www.persee.fr/doc/colan_0336-1500_1980_num_45_1_1364">"Lisibilité et compréhension"</a>
