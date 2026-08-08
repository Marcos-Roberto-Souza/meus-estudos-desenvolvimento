''' Função Recursiva '''
def Fatorial(N): # N = 4 - N = 3  - N = 2  <---
    if N <= 1:
        return 1
    else:
        return N * Fatorial(N-1) # preste muita atenção a essa linha
            # 4 * Fatorial(3) = 4 * 6 = 24
            # 3 * Fatorial(2) = 3 * 2 = 6
            # 2 * Fatorial(1) = 2 * 1 = 2

Entrada = int(input('Digite um inteiro: '))
F = Fatorial(Entrada) #valor 24 é carregado em F e é impresso na chamanda print
print(f'O Fatorial de {Entrada} é {F}')
