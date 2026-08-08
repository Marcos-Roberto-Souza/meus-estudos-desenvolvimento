//Código base de Entrada para JavaScript

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let valores = [];

rl.on('line', (input) => {
    valores.push(input);
    
    if (valores.length === 2) {
//const valorSalario =  parseFloat(valores[0]);  #aqui é onde você coloca a variavel de entrada,
//const valorBeneficio = parseFloat(valores[1]); #para fazer a inserçã dos valores digitados.

const valorImposto = calcularImposto(valorSalario);

//const saida = valorSalario - valorImposto + valorBeneficio; #aqui foi definido uma variável para Mostrar na tela o calculo,
// para o console.log(saida.toFixed(2));

console.log(saida.toFixed(2));
rl.close();
    }
});