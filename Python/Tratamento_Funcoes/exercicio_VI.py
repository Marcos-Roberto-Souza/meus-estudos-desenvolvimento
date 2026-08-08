'''Enunciado
Escreva um programa que verifique se um número inteiro lido é primo.
Lembrando que um número primo é divisivel apenas por 1 e por ele mesmo.
A verificação do primo deve ser feita dentro de uma função. '''
def NumPrimo(A):
    '''Se A for primo retorna True, senão retorna False'''
    if A == 2:
        return True
    elif A % 2 == 0:
        return False
    else:
        raiz = pow(A,0.5) #raiz quadrada de A
        i = 3
        while i <= raiz:
            if A % i == 0:
                return False
            i+= 2
        return True

N = int(input('Digite um inteiro: '))
if NumPrimo(N):
    print(f'{N} é Primo')
else:
    print(f'{N} Não é Primo')
    
    
