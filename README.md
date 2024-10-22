# LIX readability score calculator for french texts

Ce programme calcule l'indice de lisibilité LIX. Il est paramétré pour les textes français.

L'indice de lisibilité LIX est une mesure développée par le linguiste suédois Carl-Hugo Björnsson vers 1968. Il est calculé en additionnant le nombre moyen de mots par phrase au pourcentage de mots longs (plus de six lettres) dans un texte donné :

> LIX = (nombre de mots / nombre de phrases) + (100 * nombre de mots longs / nombre de mots)

Plus l'indice LIX est élevé, plus le texte est difficile à lire.

## Description

Ce programme accepte en saisie utilisateur le chemin d'accès d'un fichier texte (text, odt, doc, docx, pdf) dont il souhaite calculer l'indice LIX et affiche en sortie les éléments suivants :

- nombre de phrases ;
- nombre de mots ;
- nombre de mots longs (>6 lettres) ;
- score de lisibilité LIX ;
- interprétation du niveau de difficulté du texte (très difficile, difficile, moyenne, facile, très facile).

Le code propose une interface utilisateur minimaliste programmée sur Tkinter.