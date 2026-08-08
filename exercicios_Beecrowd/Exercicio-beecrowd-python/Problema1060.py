'''
Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

Entrada
Seis valores, negativos e/ou positivos.

Saída
Imprima uma mensagem dizendo quantos valores positivos foram lidos.
'''

count = 0;

for c in range(0, 6):
    digite = float(input())
    if digite >= 0:
        count += 1

print(f'{count} valores positivos')