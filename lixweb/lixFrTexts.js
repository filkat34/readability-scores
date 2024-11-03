const input= "Il était une fois une petite fille de village, la plus jolie qu'on eût su voir : sa mère en était folle, et sa grand-mère plus folle encore. Cette bonne femme lui fit faire un petit chaperon rouge qui lui seyait si bien, que partout on l'appelait le petit Chaperon rouge.";

function nbMots(str) { 
    let regex = /(\w+)/g;
    return str.match(regex).length;
}

function nbMotsLongs(str) { 
  let regex = /(\w\w\w\w\w\w\w+)/g;
  return str.match(regex).length;
}

function nbPhrases(str){
  let regex = /(\w\w+\s?[.?!])/g;
  return str.match(regex).length;
}

function scoreLix(str){
  return (nbMots(str)/nbPhrases(str))+(100*(nbMotsLongs(str)/nbMots(str)));
}

function niveauDifficulte(str){
  if (scoreLix(str) > 60) {
   return "Très difficile";
  }else if (scoreLix(str) >= 50) {
    return "Difficile";
  }else if (scoreLix(str) >= 40) {
        return "Moyenne";
  }else if (scoreLix(str) >= 30){
        return "Facile";
  }else {
        return "Très facile";}
}

let Mots = nbMots(input);
let MotsLongs = nbMotsLongs(input);
let Phrases = nbPhrases(input);
let Lix = scoreLix(input)
let Difficulte = niveauDifficulte(input)

console.log(
'Score LIX.................. ' + Lix+'\n'+
'Niveau de difficulté....... ' + Difficulte+'\n'+
'Nombre de mots............. ' + Mots+'\n'+
'Nombre de mots longs....... ' + MotsLongs+'\n'+
'Nombre de phrases.......... ' + Phrases
)