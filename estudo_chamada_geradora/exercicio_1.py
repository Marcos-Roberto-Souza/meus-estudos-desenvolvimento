''' Enunciado
Escreva uma funão Geradora capas de calcular e retornar números primos a partir do 2.
Escreva um programa para testá-la.
'''

def gerador_primos():
    yield 2
    v = 3
    while True:
        raiz = v ** 0.5
        i = 3
        while i <= raiz and v % i != 0:
            i += 2
        if i > raiz:
            yield v
        v += 2

gen = gerador_primos()
Qtde = int(input('Digite a Quantidade: '))
for _ in range(Qtde):
    print(next(gen), end = ' ')

print("\n*** FIM DO PROGRAMA ***")

