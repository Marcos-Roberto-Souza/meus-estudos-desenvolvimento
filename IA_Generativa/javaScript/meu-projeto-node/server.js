const http = require("http");
const fs = require("fs");
const url = require("url");

const server = http.createServer((req, res) => {

    // Rota principal (HTML)
    if (req.url === "/") {
        fs.readFile("index.html", (err, data) => {
            res.writeHead(200, { "Content-Type": "text/html" });
            res.end(data);
        });
    }

    // Rota de cálculo
    if (req.url.startsWith("/calcular")) {
        const query = url.parse(req.url, true).query;

        const salario = parseFloat(query.salario);
        const beneficio = parseFloat(query.beneficio);

        const imposto = calcularImposto(salario);
        const resultado = salario - imposto + beneficio;

        res.writeHead(200, { "Content-Type": "text/plain" });
        res.end(resultado.toFixed(2));
    }
});

function calcularImposto(salario) {
    let aliquota;

    if (salario < 1100) {
        aliquota = 0.05;
    } else if (salario < 2500) {
        aliquota = 0.10;
    } else {
        aliquota = 0.15;
    }

    return aliquota * salario;
}

server.listen(3000, () => {
    console.log("Servidor rodando em http://localhost:3000");
});