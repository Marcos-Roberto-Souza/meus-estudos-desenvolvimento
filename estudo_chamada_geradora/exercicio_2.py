'''Enunciado
Escreva uma função geradora capaz de calcular e retornar o fatorial de um número natural.
Essa função deve retornar uma tupla com o prório número natural e seu fatorial.
Escreva um programa para testá-la.
Lembre-se que 0! = 1
'''

def funcao_fatorial():
    num, fat = 0, 1
    while True:
        yield num, fat
        num += 1
        fat *= num

N = int(input('Digite a Quantidade: '))
gen = funcao_fatorial()
for _ in range(N):
    print(next(gen))

print('\n\n*** FIM DO PROGRAMA ***')
