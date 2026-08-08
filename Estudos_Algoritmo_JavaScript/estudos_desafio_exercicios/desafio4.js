
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Digite o nome do herói: ", function (mensagem){ // Lê o comando enviado ao bot
function usuario(mensagem){
    return mensagem.toUpperCase();
}
console.log(usuario(mensagem));
});


