# LIX readability score calculator for french texts

Ce programme calcule l'indice de lisibilité LIX. Il est paramétré pour les textes français.

L'indice de lisibilité LIX est une mesure développée par le linguiste suédois Carl-Hugo Björnsson vers 1968. Il est calculé en additionnant le nombre moyen de mots par phrase au pourcentage de mots longs (plus de six lettres) dans un texte donné :

> LIX = (nombre de mots / nombre de phrases) + (100 * nombre de mots longs / nombre de mots)

Plus l'indice LIX est élevé, plus le texte est difficile à lire.

Ce programme accepte en saisie un fichier texte brut (.txt) dont l'utilisateur souhaite calculer l'indice LIX et affiche en sortie les éléments suivants :

- nombre de phrases ;
- nombre de mots ;
- nombre de mots longs (>6 lettres) ;
- score de lisibilité LIX ;
- interprétation du niveau de difficulté du texte (très difficile, difficile, moyenne, facile, très facile).

Le code propose une interface utilisateur minimaliste programmée sur Tkinter.

## Description

Pour le traitement du texte des expressions régulières ont été utilisées:

- pour compter le nombre de mots : "\w+" ;
- pour le décompte des mots de plus de six lettres : "\w\w\w\w\w\w\w+" ;
- pour le décompte des phrases : "\w\w+\s?[.?!]". Le fait de chercher une ponctuation forte après un mot d'au moins deux lettres, permet d'exclure la plupart des abréviations consistant en une majuscule suivie d'un point".

## Notes pour plus tard...

- [ ] Rajouter au programme une dimension sémantique en créant un indice composite fondé à la fois sur LIX et la fréquence lexicale des mots considée comme un indicateur de la difficulté du vocabulaire ;
- [ ] Quelles bases de données de fréquence lexicale utiliser ? Open Lexicon...
