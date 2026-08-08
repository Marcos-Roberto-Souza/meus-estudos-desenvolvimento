const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Digite o nome do herói: ", function (comando){ // Lê o comando enviado ao bot

if (comando === "start"){
  console.log("Bot started")
}else if (comando === "stop"){
  console.log("Bot stopped")
}else if (comando === "pause"){
  console.log("Bot paused")
}
else{console.log("Unknown command")
}

});