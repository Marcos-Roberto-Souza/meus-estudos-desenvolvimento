
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
rl.question("Digite Seu canal: ", function (canal){ // Lê o comando enviado ao bot
function rSocial(canal){
    return canal;
}
rl.question("Digite Seu Nome: ", function (mensagem){ // Lê o comando enviado ao bot
function usuario(mensagem){
    return mensagem;
}
console.log('ola, ' + usuario(mensagem) + '! Bem-vindo ao canal ' + rSocial(canal)+ '.' );
});
});
