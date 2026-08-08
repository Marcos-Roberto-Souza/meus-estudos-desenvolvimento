''' Enunciado
Escreva uma função recursiva para calcular a somatória dos termos de uma Progressão Aritmética
defina pelos parâmetros Prim(primeiro termo), Razão e Qtde(quantidade de elementos).
Esses parâmetros devem ser lidos do teclado.
Escreva o programa principal para testar a função que deve exibir na tela o valor dessa soma.
Teste seu programa com os casos de teste a seguir.

Caso de teste:
        Prim = 7; Razão = 4; Qtde = 7 --> Soma = 133
        Prim = 12 Razão = 8; Qtde = 15 -> Soma = 1020
        Prim = 2; Razão = 3; Qtde = 6 --> Soma = 57
'''

def soma(P, R, Q):
    if Q > 0:
        return P + soma(P+R, R, Q-1)
    else:
        return 0

Prim = int(input('Digite o Primeiro termo: '))
Razao = int(input('Digite a Razao: '))
Qtde = int(input('Digite a Quantidade: '))
Resultado = soma (Prim, Razao, Qtde)
print(f'para Prim = {Prim}; Razao = {Razao}; Qtde = {Qtde} --> Soma = {Resultado}')
