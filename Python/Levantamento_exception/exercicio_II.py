''' Enunciado
Escreva uma função que recebe uma lista ou tupla com valores numéricos e retorne uma
lista contendo o quadrado dos valores recebidos.
Utilize exceções para as situações de possivel erro.
Possiveis Erros:
1. O argumento pode não ser lista ou tupla.
2. Um dos elementos do argumento pode não ser numérico.
'''
def AoQuadrado(dados):
    if not isinstance(dados, list | tuple):
        raise TypeError(f'Lista ou Tupla esperados. Foi usado {type(dados)}')
    if not all(isinstance(x, int | float ) for x in dados):
        raise ValueError('Os elementos de dados devem ser todos numéricos')
    return [v**2 for v in dados]

A = [2, 3, 4,10.0]

'''x = 'text'

A.append(x)'''

print(AoQuadrado(A))
