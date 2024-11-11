# Scores de lisibilité pour textes français

## Objectif 

L'objectif de ce programme est de permettre, à partir d'un texte saisi ou d'un fichier en texte brut (.txt), le calcul de six scores de lisibilité :

* LIX 
* RIX
* Automated Readability Index (ARI)
* Gunning Fog index
* Coleman-Liau index
* Flesch-Kincaid Grade Level (FKGL)
* Simple Measure of Gobbledygook index (SMOG).

Ce programme permet aussi l'affichage des statistiques du texte sur lesquelles il s'est fondé pour effectuer le calcul. Il affiche les nombres de: 

* caractères
* voyelles
* digrammes
* trigrammes
* syllabes graphiques
* mots
* mots de plus de six caractères
* mots de plus de trois syllabes
* phrases

## Description

Ce programme repose entièrement sur les expressions régulières pour établir les variables qui servent au calcul de ces scores de lisibilité. 

Si les expressions régulières apportent une réponse algorithmique efficace pour la grande majorité des variables à établir, elles se revèlent moins précises, bien que souvent suffisantes, pour calculer le nombre de syllabes d'un mot. Cela est étroitement lié à la complexité et à l'irrégularité de la langue française. 

Pour faire face à ce problème et afin que les résultats soient fiables, il a été décidé de procéder au décompte des syllabes graphiques et non phoniques : pour cela, on comptabilise d'abord le nombre de voyelles dans un mot donné ; ensuite, on soustrait à cette somme le nombre de digrammes et de trigrammes qui s'y trouvent.

## Prise en main

Pour exécuter ce programme, il suffit d'avoir un environnement de développement intégré pour le langage Python sur votre ordinateur et exécuter le fichier "readability_scores_calculator.py". 

Ce programme est également fourni en tant que script JS : pour l'exécuter il suffit de télécharger le fichier "readability_scores_calculator.html" et l'ouvrir avec votre navigateur.

## Bibliographie indicative

* Benoît J.-P. (1986). "<a href="https://doi.org/10.3406/prati.1986.1409">Revue critique des formules de lisibilité (60 ans de formules de lisibilité : qu'en reste-t-il ?)</a>".

* Conquet A., Richaudeau F. (1973). "<a href="https://doi.org/10.3406/colan.1973.3978">Cinq méthodes de mesure de la lisibilité</a>".

* De Landsheere, G. (1963). "<a href="http://www.jstor.org/stable/40659295">Pour une application des tests de lisibilité de Flesch à la langue française</a>"

* Henry G. (1980). "<a href ="https://doi.org/10.3406/colan.1980.1364">Lisibilité et compréhension</a>".

* Labasse B. (1999). "<a href="https://doi.org/10.3406/colan.1999.2951">La lisibilité rédactionnelle : fondements et perspectives</a>".

* Le Maux, J. (2015). "<a href = "https://doi.org/10.3917/rfla.202.0099">La lisibilité de l’information financière</a>".

* Mesnager J. (1989). "<a href="https://doi.org/10.3406/colan.1989.1081"> Lisibilité des textes pour enfants : un nouvel outil ?</a>.

* Richaudeau F. (1976). "<a href="https://doi.org/10.3406/colan.1976.4293">Faut-il brûler les formules de lisibilité ?</a>".