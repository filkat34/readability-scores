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
  let regex = /(au)|(eu)|(ou)|(oi)|(œu)|(ei)|(ai)|(ee)|(ue)|(ui)|(ua)/gi;
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

function scoreLix(str){
  return nbMots(str)/nbPhrases(str)+100*(nbMotsLongs(str)/nbMots(str));
}

function scoreRix(str){
  return nbMotsLongs(str)/nbPhrases(str);
}

function scoreFkgl(str){
  return 0.39*(nbMots(str)/nbPhrases(str))+11.8*(nbSyllabesGraphiques(str)/nbMots(str))-15.59;
}

function scoreGunningFog(str){
  return 0.4*(nbMots(str)/nbPhrases(str))+100*(nbMotsPolysyllabiques(str)/nbMots(str));
}

function scoreSMOG(str){
  return 1.043*(Math.sqrt((nbMotsPolysyllabiques(str)*(30/nbPhrases(str)))))+3.1291;
}

function scoreColemanLiau(str){
  return 0.0588*((nbCaracteres(str)/nbMots(str))*100)-0.296*((nbPhrases(str)/nbMots(str))*100)-15.8;
}

function scoreAri(str){
  return 4.71*(nbCaracteres(str)/nbMots(str))+0.5*(nbMots(str)/nbPhrases(str))-21.43;
}

// Readability scores analysis :

function scoreAnalysis(formula, score){
  let formula_scales = [['lix',60,56,44,36,32,28,24],
                  ['rix',8,7.2,4.5,3.0,2.4,1.8,1.3],
                  ['fkgl',16,13,10,8,7,6,5],
                  ['gunning',16,13,10,8,7,6,5],
                  ['smog',16,13,10,8,7,6,5],
                  ['ari',16,13,10,8,7,6,5],
                  ['coleman_liau',17,13,12,10,7,6,5]
                ]
  for (const x in formula_scales.length) {
    for (const y in formula_scales.length) {
      if (formula_scales[x][y] == formula){
        if (score > formula_scales[x][y+1]){
            return "Très difficile (>Bac+3)";
          }
        if (score >= formula_scales[x][y+2]){
            return "Difficile (Bac+3)";
          }
        if (score >= formula_scales[x][y+3]){
            return "Plutôt difficile (lycée)";
          }
        if (score >= formula_scales[x][y+4]){
            return "Niveau moyen (4e-3e)";
          }
        if (score >= formula_scales[x][y+5]){
            return "Plutôt facile (5e)";
          }
        if (score >= formula_scales[x][y+6]){
            return "Facile (6e)";
          }
        if (score >= formula_scales[x][y+7]){
            return "Très facile (CM2)";
          }
        return "Extrêmement facile (>CM1)"
              }
            }
          }
        }
      

// Print text statistics and readability analysis :

let Caracteres = nbCaracteres(input);
let Voyelles = nbVoyelles(input);
let Digrammes = nbDigrammes(input);
let Trigrammes = nbTrigrammes(input);
let Syllabes = nbSyllabesGraphiques(input)
let Mots = nbMots(input);
let MotsLongs = nbMotsLongs(input);
let MotsPolysyllabiques =  nbMotsPolysyllabiques(input);
let Phrases = nbPhrases(input);

let lix = scoreLix(input).toFixed(1)
let rix = scoreRix(input).toFixed(1)
let fkgl = scoreFkgl(input).toFixed(1)
let gunnningFog = scoreGunningFog(input).toFixed(1)
let smog = scoreSMOG(input).toFixed(1)
let colemanLiau = scoreColemanLiau(input).toFixed(1)
let ari = scoreAri(input).toFixed(1)

let lixAnalysis = scoreAnalysis('lix',lix)


console.log(
'STATISTIQUES DU TEXTE'+'\n'+
'---------------------'+'\n\n'+
'Nombre de caractères.................. ' + Caracteres+'\n'+
'Nombre de voyelles.................... ' + Voyelles+'\n'+
'Nombre de digrammes................... ' + Digrammes+'\n'+
'Nombre de trigrammes.................. ' + Trigrammes+'\n'+
'Nombre de syllabes.................... ' + Syllabes+'\n'+
'Nombre de mots........................ ' + Mots+'\n'+
'Nombre de mots longs.................. ' + MotsLongs+'\n'+
'Nombre de mots polysyllabiques........ ' + MotsPolysyllabiques+'\n'+
'Nombre de phrases..................... ' + Phrases+'\n\n\n'+
'INDICES DE LISIBILITE'+'\n'+
'---------------------'+'\n\n'+
'LIX................................... ' + lix+' : '+ lixAnalysis + '\n'+
'RIX................................... ' + rix+'\n'+
'Flesch-Kincaid grade level............ ' + fkgl+'\n'+
'Gunning Fog index..................... ' + gunnningFog+'\n'+
'Simple Measure of Gobbledygook index.. ' + smog+'\n'+
'Coleman-Liau index.................... ' + colemanLiau+'\n'+
'Automated Readability Index........... ' + ari
)