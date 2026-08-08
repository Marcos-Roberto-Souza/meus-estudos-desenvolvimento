var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let x
let y

x = parseInt(lines.shift());
y = parseInt(lines.shift());
let resultado = x + y

console.log("X = " + resultado);