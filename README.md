# Scores de lisibilité pour textes français

## Objectif 

L'objectif de ce programme est de permettre, à partir d'un fichier en texte brut (.txt) fourni par l'utilisateur, le calcul de six scores de lisibilité :

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
* syllabes
* mots
* mots de plus de six caractères
* mots de plus de trois syllabes
* phrases

## Description

Ce programme repose entièrement sur les expressions régulières pour établir les variables qui servent au calcul de ces scores de lisibilité. 

Si les expressions régulières apportent une réponse algorithmique efficace pour la grande majorité des variables à établir, elles se revèlent moins précises, bien que souvent suffisantes, pour calculer le nombre de syllabes d'un mot. Cela est étroitement lié à la complexité et à l'irrégularité de la langue française. 

Pour faire face à ce problème et afin que les résultats soient fiables, il a été décidé de procéder au décompte des syllabes graphiques et non phoniques : pour cela, on comptabilise d'abord le nombre de voyelles dans un mot donné ; ensuite, on soustrait à cette somme le nombre de digrammes et de trigrammes qui s'y trouvent.

## Prise en main

Pour exécuter ce programme, il suffit d'avoir un environnement de développement intégré pour le langage Python sur votre ordinateur. Un script js. est également proposé mais qui permet uniquement de calculer l'indice LIX.