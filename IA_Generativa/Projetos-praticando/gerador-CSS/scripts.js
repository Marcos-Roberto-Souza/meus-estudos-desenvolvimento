/*
Variável - Pedacinho de memória que eu posso guardar o que eu quiser

Lógica de Programação - Seguir a Receita do Bolo par fazer o bolo
Algoritmo - Receita do Bolo
Função é um pedaço de cógdigo que é executado quando for chamado

Lógica do Código

[] Saber quem é o botão
[] Saber quando o botão foi clicado
[] Saber quem é o textarea
[] Pegar o que tem dentro dele
[] Enviar para a IA
[] Pegar a resposta da IA e colocar na tela
[] Deixar a resposta da IA bonitinha (formatar o código)
[] Mostrar o resultado do código no (iframe)

// Ir no HTML e pegar o botão
// HTML = documet(documento)
// Selecionar (querySelector)
// Quem é ? Botão
// colocar apelido (adicionar uma classe no button do HTML para chamar o botão)
//fetch - ferramenta do JS para se comunicar com o servidor
*/

//Descobri quem é o botão
let botao = document.querySelector(".botao-gerar")
let chave = "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"
let endereco = "https://api.groq.com/openai/v1/chat/completions"
//Explicação rápida,
//criei uma função que sera chamada
//Sempre que for acessar um servidor, tem que avisar  para o JS que é algo que demora um pouco, 
// tem dois comandos async e await, que avisam o JS que tem que esperar a resposta do servidor para continuar o código

async function gerarCodigo() {
    let textoUsuario = document.querySelector(".caixa-texto").value
    let blocoCodigo = document.querySelector(".bloco-codigo")
    let resultadoCodigo = document.querySelector(".resultado-codigo")

    let resposta = await fetch(endereco, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",

            "Authorization": "Bearer " + chave

        },
        body: JSON.stringify({
            model: "llama-3.3-70b-versatile",
            messages: [
                {
                    role: "system",
                    content: "Você é um gerador de código HTML e CSS. Responda SOMENTE com código puro. NUNCA use crases, markdown ou explicações. Formato: primeiro <style> com o CSS, depois o HTML. Siga EXATAMENTE o que o usuário pedir. Se pedir algo quicando, use translateY no @keyframes. Se pedir algo girando, use rotate."

                },
                {
                    role: "user",
                    content: textoUsuario
                }]
        })
    })//tem que mandar o endereço e configuração

    let dados = await resposta.json() //pegar a resposta e transformar em um formato que o JS entenda
    let resultado = dados.choices[0].message.content //pegar a resposta da IA
    blocoCodigo.textContent = resultado //colocar a resposta da IA no bloco de código
    resultadoCodigo.srcdoc = resultado //colocar a resposta da IA no iframe para mostrar o resultado do código
    
    console.log(dados)
}

//fica de olho no botão, e chama a função quando clicado
botao.addEventListener("click", gerarCodigo)


// Vizinho curioso(addEventListener)
//adicionar ouvinte de eventos
// Evento = Clique, digite ....