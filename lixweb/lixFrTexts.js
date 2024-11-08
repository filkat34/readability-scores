const input= "Il était une fois une petite fille de village : si beau probablement.";


// Text analysis with Regex :

function nbCaracteres(str) {
  str = str.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
  let regex = /(\w)/gi;
  return str.match(regex).length;
}

function nbVoyelles(str) {
  str = str.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
  let regex = /[aeiouœ]/gi;
  return str.match(regex).length;
}

function nbDigrammes(str) {
  str = str.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
  let regex = /(au)|(eu)|(ou)|(oi)|(œu)|(ei)|(ai)|(ee)|(que)|(qui)/gi;
  return str.match(regex).length;
}

function nbTrigrammes(str) {
  str = str.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
  let regex = /(eau)|(oue)/gi;
  return str.match(regex).length;
}

function nbSyllabesGraphiques(str) {
  return nbVoyelles(str) - (nbDigrammes(str)+nbTrigrammes(str));
}

function nbMots(str) {
  str = str.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
  let regex = /(\w+)/gi;
  return str.match(regex).length;
}

function nbMotsPolysyllabiques(str) {
  let punctuation = /[\.,?!;:]/g;
  str = str.normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(punctuation, "").replace("  ", " ");
  let mots = str.split(' ');
  let motsPolysyllabiques = 0;
  let voyelles = 0
  for (const mot in mots){
    if ((nbVoyelles(mot) - nbDigrammes(mot) - nbTrigrammes(mot)) >= 3){
      motsPolysyllabiques++;}
return voyelles;}
    }

function nbMotsLongs(str) { 
  str = str.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
  let regex = /(\w{7,})/g;
  return str.match(regex).length;
}

function nbPhrases(str){
  let regex = /(\w\w+\s?[.?!])/g;
  return str.match(regex).length;
}


let Caracteres = nbCaracteres(input);
let Voyelles = nbVoyelles(input);
let Digrammes = nbDigrammes(input);
let Trigrammes = nbTrigrammes(input);
let Syllabes = nbSyllabesGraphiques(input)
let Mots = nbMots(input);
let MotsLongs = nbMotsLongs(input);
let MotsPolysyllabiques =  nbMotsPolysyllabiques(input);
let Phrases = nbPhrases(input);


console.log(
'Nombre de caractères.............. ' + Caracteres+'\n'+
'Nombre de voyelles................ ' + Voyelles+'\n'+
'Nombre de digrammes............... ' + Digrammes+'\n'+
'Nombre de trigrammes.............. ' + Trigrammes+'\n'+
'Nombre de syllabes................ ' + Syllabes+'\n'+
'Nombre de mots.................... ' + Mots+'\n'+
'Nombre de mots longs.............. ' + MotsLongs+'\n'+
'Nombre de mots polysyllabiques.... ' + MotsPolysyllabiques+'\n'+
'Nombre de phrases................. ' + Phrases
)