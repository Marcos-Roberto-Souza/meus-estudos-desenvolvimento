from random import randint
def CarregaLista(qtde):
    '''Carrega uma lista com a qtde de elementos aleatórios entre 1 e 1000'''
    L = []
    for i in range(qtde):
        L.append(randint(1,1000))
    return L

q = int(input('Digite a quantidade desejada: '))
valores = CarregaLista(q)
print(f'Lista Gerada >> {valores}')
print(f'A lista Gerada tem {q} elementos')

print('*** FIM DO PROGRAMA ***')
