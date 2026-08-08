const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let valores = [];

rl.on('line', (input) => {
    valores.push(input);
    
    if (valores.length === 2) {
const valorSalario =  parseFloat(valores[0]);
const valorBeneficio = parseFloat(valores[1]);

const valorImposto = calcularImposto(valorSalario);

const saida = valorSalario - valorImposto + valorBeneficio;

console.log(saida.toFixed(2));
rl.close();
    }
});

function calcularImposto(salario) {
let aliquota;

if (salario <= 1100) {
    aliquota = 0.05;
}else if (salario > 1100 && salario <= 2500) {
    aliquota = 0.10;
}else if (salario > 2500) {
    aliquota = 0.15;
}

return aliquota * salario;
}

