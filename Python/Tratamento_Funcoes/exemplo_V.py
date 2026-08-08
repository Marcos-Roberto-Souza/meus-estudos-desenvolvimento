from random import randint
def CarregaLista(qtde, a, b):
    '''Carrega uma lista com a qtde de elementos aleatórios nos limites entre a e b.'''
    L = []
    for i in range(qtde):
        L.append(randint(a, b))
    return L

q = int(input('Digite a quantidade desejada: '))
lmin = int(input('Digite o Limite minimo: '))
lmax = int(input('Digite o Limite maximo: '))
valores = CarregaLista(q, lmin, lmax)
print(f'Lista Gerada >> {valores}')
print(f'A lista Gerada tem {q} elementos')

print('*** FIM DO PROGRAMA ***')
