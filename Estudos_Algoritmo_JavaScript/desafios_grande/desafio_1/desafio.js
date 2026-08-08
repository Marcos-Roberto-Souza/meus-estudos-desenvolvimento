const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Digite o nome do herói: ", function (Nome) {
  rl.question("Digite a quantidade de XP: ", function (Xp) {
    Xp = Number(Xp);
    let Nivel = "";

if (Xp <= 1000){
    Nivel = " Ferro "
}else if(Xp > 1000 && Xp <= 2000){
    Nivel = " Bronze "
}else if(Xp > 2000 && Xp <= 5000){
    Nivel = " Prata "
}else if(Xp > 5000 && Xp <= 7000){
    Nivel = " Ouro "
}else if(Xp > 7000 && Xp <= 8000){
    Nivel = " Platina "
}else if(Xp > 8000 && Xp <= 9000){
    Nivel = " Ascendente "

}else if(Xp > 9000 && Xp <= 10000){
    Nivel = " Imortal "
}else {
  Nivel = "Radiante"
}

console.log("\nO Herói de Nome: ** " +  Nome  + " ** \n\nEstá no Nível Nv.** " + Nivel + "**\n")
  });
});