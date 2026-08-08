'''
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.

Exemplo de Entrada	        |Exemplo de Saída
----------------------------------------------------
7 21 -14                    |
                            |   -14
                            |  7
                            | 21
                            |
                            |   7
                            |  21
                            | -14
---------------------------------------------------
'''
'''
primeiroNumero, segundoNumero, terceiroNumero = map(int, input().split())

if primeiroNumero < segundoNumero < terceiroNumero:
    print(f"{primeiroNumero}")
    print(f"{segundoNumero}")
    print(f"{terceiroNumero}")

elif segundoNumero < terceiroNumero < primeiroNumero:
    print(f"{segundoNumero}")
    print(f"{terceiroNumero}")
    print(f"{primeiroNumero}")

elif terceiroNumero < primeiroNumero < segundoNumero:
    print(f"{terceiroNumero}")
    print(f"{primeiroNumero}")
    print(f"{segundoNumero}")

elif segundoNumero < primeiroNumero < terceiroNumero:
    print(f"{segundoNumero}")
    print(f"{primeiroNumero}")
    print(f"{terceiroNumero}")
elif primeiroNumero < terceiroNumero < segundoNumero:
    print(f"{primeiroNumero}")
    print(f"{terceiroNumero}")
    print(f"{segundoNumero}")
elif terceiroNumero < primeiroNumero < segundoNumero:
    print(f"{terceiroNumero}")
    print(f"{primeiroNumero}")
    print(f"{segundoNumero}")

print(f"\n{primeiroNumero}")
print(f"{segundoNumero}")
print(f"{terceiroNumero}")
'''

#Resolver Usando Lista
numeros = list(map(int, input().split()))

original = numeros[:]

numeros.sort()

for n in numeros:
    print(n)
print()

for n in original:
    print(n)