''' Busca Binária '''
def Buscabin(valor, lista, ini, fim):
    #procura em lista, entre as posições ini:fim
    print(f'ini = {ini} e fim = {fim}')
    if ini > fim:
        return False
    meio = (ini + fim) // 2
    print(f'meio = {meio} eo valor nessa posição é {lista[meio]}')
    if valor == lista[meio]:
        return True
    elif valor < lista[meio]:
        return Buscabin(valor, lista, ini, meio-1)
    else:
        return Buscabin(valor,lista,meio+1,fim)


L = [14,17,20,22,23,25,28,29,31,35,40,45,50,53,56,59,62,65]
X = int(input('Digite um valor para pesquisa na lista: '))
while X != 0:
    Achou = Buscabin(X, L, 0, len(L)-1)
    if Achou != 0:
        #chamada para verificar a metade esquerda da lista
        print(f'{X} está na Lista')
    else:
        #chamada apra verificar a medade direita da lista
        print('{X} não está na lista')
    X = int(input('Digite um valor para pesquisar na lista: '))

print('*** FIM DO PROGRAMA ***')
