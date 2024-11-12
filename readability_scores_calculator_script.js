// Text analysis functions with Regex :

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
let regex = /(eau)|(oue)|(aie)/gi;
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
let motsLongs = str.match(regex);
if(motsLongs==null){
    motsLongs = 0;
}
else{
    motsLongs = str.match(regex).length;
}
return motsLongs;
}

function nbPhrases(str){
let regex = /\w\w+\.|!|\?/gi;
let phrases = str.match(regex);
if(phrases==null){
    phrases = 1;
}
else{
    phrases = str.match(regex).length;
}
return phrases;
}


// Readability formulas functions :

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
return 0.4*(nbMots(str)/nbPhrases(str)+100*(nbMotsPolysyllabiques(str)/nbMots(str)));
}

function scoreSMOG(str){
return 1.043*Math.sqrt((nbMotsPolysyllabiques(str)*(30/nbPhrases(str))))+3.1291;
}

function scoreColemanLiau(str){
return 0.0588*((nbCaracteres(str)/nbMots(str))*100)-0.296*((nbPhrases(str)/nbMots(str))*100)-15.8;
}

function scoreAri(str){
return 4.71*(nbCaracteres(str)/nbMots(str))+0.5*(nbMots(str)/nbPhrases(str))-21.43;
}

// Readability scores analysis function :

function scoreAnalysis(formula, score){
    let formula_scales = [['lix',59,50,40,30],
                    ['rix',7.1,5.3,2.9,1.8],
                    ['fkgl',15,12,5,1],
                    ['gunning',17,13,7,1],
                    ['smog',14,12,7,1],
                    ['ari',15,9,5,1],
                    ['coleman_liau',15,9,5,1]
                    ]
    for (let column in formula_scales) {
        for (let row in formula_scales) {
        if (formula_scales[column][row] == formula){
            if (score > formula_scales[column][1]){
                return "🔴 Très difficile";
            }
            if (score > formula_scales[column][2]){
                return "🟠 Difficile";
            }
            if (score > formula_scales[column][3]){
                return "🟡 Intermédiaire";
            }
            if (score > formula_scales[column][4]){
                return "🟢 Facile";
            }
            return "⚪️ Très facile";
                }
                }
            }
}