from random import randint
def CarregaLista():
    L = []
    for i in range(10):
        L.append(randint(1,1000))
    return L

print('***INICIO DO PROGRAMA***\n')
print('PRIMEIRA LISTA GERADA\n')
valores = CarregaLista()
print(f'Lista Gerada >> {valores}')


print('\nSEGUNDA LISTA GERADA\n')
valores2 = CarregaLista()
print(f'Lista Gerada >> {valores2}')

print('\n*** FIM DE PROGRAMA ***')
