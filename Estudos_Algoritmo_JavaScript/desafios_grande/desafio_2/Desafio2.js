const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
let vitorias = 0
let derrotas = 0
let nivel = ""    

rl.question("Digite a quantidade de vitórias: ", function (vitorias){ // Lê o comando enviado ao bot
rl.question("Digite a quantidade de Derrotas: ", function (derrotas){ // Lê o comando enviado ao bot

    let resultado = vitorias - derrotas
    function nivelHeroi(nivel){
        if (resultado <= 10){
            return "Ferro"
    }else if (resultado > 10 && resultado <=20){
            return "Bronze"
    }else if (resultado > 20 && resultado <=50){
            return "Prata"
    }   else if (resultado > 50 && resultado <=80){         
            return "Ouro"
    }else if (resultado > 80 && resultado <=90){
            return "Diamante"
    }else if (resultado > 90 && resultado <=100){
            return "Lendário"
    }else if (resultado > 100){
            return "Imortal"
    }
    }

    console.log("O Herói tem saldo de **" + resultado + "** está no nível de ** " + nivelHeroi(nivel) + "**");
});

});