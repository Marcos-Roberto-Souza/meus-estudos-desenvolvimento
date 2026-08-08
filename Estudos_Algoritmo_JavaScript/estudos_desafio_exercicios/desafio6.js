const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
rl.question("Digite Seu canal: ", function (canal){ // Lê o comando enviado ao bot
function rSocial(canal){
    if(canal === "whatsapp"){
        return "Ola, este e o WhatsAppBot!";
    }else if(canal === "telegram"){
        return "Ola, este e o TelegramBot!";
    }else if(canal === "webchat"){
        return "Ola, este e o WebChatBot!";
    }else {
        return "Canal nao suportado ";}
}

console.log(rSocial(canal));
});
