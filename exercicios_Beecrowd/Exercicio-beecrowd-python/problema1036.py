'''
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes,
mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada
Leia três valores de ponto flutuante (double) A, B e C.

Saída
Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.

Exemplos de Entrada	     | Exemplos de Saída
10.0 20.1 5.1            | R1 = -0.29788
                         | R2 = -1.71212

baskara b²+- raiz quadrada delta / 2.a

'''
import math
valorA, valorB, valorC = input().split()
valorA, valorB, valorC = float(valorA), float(valorB), float(valorC)

delta = pow(valorB,2) - (4*valorA*valorC)

if delta < 0 or valorB <= 0 or valorC <=0 or valorA <=0:
    print("Impossivel calcular")
else:
    R1 = (-valorB + math.sqrt(delta)) / (2 * valorA)
    R2 = (-valorB - math.sqrt(delta)) / (2 * valorA)
    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")

