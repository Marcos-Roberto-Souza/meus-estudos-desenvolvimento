'''
Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo
em qual dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra.
Obviamente se o valor não estiver em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.

O símbolo ( representa "maior que". Por exemplo:
[0,25]  indica valores entre 0 e 25.0000, inclusive eles.
(25,50] indica valores maiores que 25 Ex: 25.00001 até o valor 50.0000000

Entrada
O arquivo de entrada contém um número com ponto flutuante qualquer.

Saída
A saída deve ser uma mensagem conforme exemplo abaixo.

Exemplo de Entrada	      Exemplo de Saída
25.01                  |    Intervalo (25,50]
                       |
Exemplo de Entrada          Exemplo de Saída
25.00                  |     Intervalo [0,25]
                       |
Exemplo de Entrada         Exemplo de Saída
100.00                 |   Intervalo (75,100]
                       |
Exemplo de Entrada         Exemplo de Saída
-25.02                 |    Fora de intervalo

'''

valorDigitado = float(input())

if valorDigitado >= 0 and valorDigitado<=25:
    print("Intervalo [0,25]")
elif valorDigitado > 25 and valorDigitado<= 50:
    print("Intervalo (25,50]")
elif valorDigitado > 50 and valorDigitado<=75:
    print("Intervalo (50,75]")
elif valorDigitado > 75 and valorDigitado<= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")