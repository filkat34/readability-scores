const input= "Il était une fois un personnage très probrablement affreux anticonstitutionnellement.";


// Text analysis with Regex :

function nbCaracteres(str) {
  str = str.normalize("NFD").replace(/[\u0300-\u036f]/gi, "");
  let regex = /(\w)/gi;
  return str.match(regex).length;
}

function nbVoyelles(str) {
  str = str.normalize("NFD").replace(/[\u0300-\u036f]/gi, "");
  let regex = /[aeiouœ]/gi;
  let voyelles = str.match(regex)
  if(voyelles==null){
    voyelles = 0
  }
  else{
    voyelles = str.match(regex).length
  }
  return voyelles;
}

function nbDigrammes(str) {
  str = str.normalize("NFD").replace(/[\u0300-\u036f]/gi, "");
  let regex = /(au)|(eu)|(ou)|(oi)|(œu)|(ei)|(ai)|(ee)|(que)|(qui)/gi;
  let digrammes = str.match(regex);
  if(digrammes==null){
    digrammes = 0
  }
  else{
    digrammes = str.match(regex).length
  }
  return digrammes;
}

function nbTrigrammes(str) {
  str = str.normalize("NFD").replace(/[\u0300-\u036f]/gi, "");
  let regex = /(eau)|(oue)/gi;
  let trigrammes = str.match(regex)
  if(trigrammes==null){
    trigrammes = 0;
  }
  else{
    trigrammes = str.match(regex).length
  }
  return trigrammes;
}

function nbSyllabesGraphiques(str) {
  return nbVoyelles(str) - (nbDigrammes(str)+nbTrigrammes(str));
}

function nbMots(str) {
  str = str.normalize("NFD").replace(/[\u0300-\u036f]/gi, "");
  let regex = /(\w+)/gi;
  let mots = str.match(regex)
  if(mots==null){
    mots = 0
  }
  else{
    mots = str.match(regex).length
  }
  return mots;
}

function nbMotsPolysyllabiques(str) {
  let punctuation = /[.,?!;:]/g;
  str = str.normalize("NFD").replace(/[\u0300-\u036f]/gi, "").replace(punctuation, "").replace("  ", " ");
  let mots = str.split(' ');
  let motsPolysyllabiques = 0;
  for (const mot in mots){
    if (nbSyllabesGraphiques(mots[mot])>=3){
    motsPolysyllabiques++;
  }
    }
  return motsPolysyllabiques
  }
  

function nbMotsLongs(str) { 
  str = str.normalize("NFD").replace(/[\u0300-\u036f]/gi, "");
  let regex = /(\w{7,})/g;
  let motsLongs = str.match(regex)
  if(motsLongs==null){
    motsLongs = 0
  }
  else{
    motsLongs = str.match(regex).length
  }
  return motsLongs;
}

function nbPhrases(str){
  let regex = /(\w\w+\s?[.?!])/gi;
  let phrases = str.match(regex)
  if(phrases==null){
    phrases = 1;
  }
  else{
    phrases = str.match(regex).length;
  }
  return phrases;
}


// Readability formulas :



// Print text statistics and readability scores :

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