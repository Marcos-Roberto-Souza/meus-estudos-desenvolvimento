''' Enunciado
Escreva um programa que verifique se um número lido é Primo.
Faça isso usando uma função e utilize exceções para controlar os erros.
O parâmetro da função deve ser um número inteiro maior ou igual a 2.

Se esse parâmetro for menor que dois use a exceção ValueError
Se esse parâmetro for de classe diferente de número inteiro use a exceção TypeError.
'''

def Primo(A):
    if not isinstance(A,int):
        raise TypeError('Tipo Inválido. O argumento deve ser um Inteiro')
    if A < 2:
        raise ValueError('Valor Inválido. O argumento deve ser no minimo 2')
    if A == 2:
        return True
    elif A %2==0:
        return False
    else:
        raiz = pow(A, 0.5)
        i = 3
        while i <= raiz:
            if A%i == 0:
                return False
            i += 2
        return True

# Programa principal
try:
    N = int(input('Digite um inteiro: '))
    if Primo(N):
        print(f'{N} é *** PRIMO ***')
    else:
        print(f'{N} Não é *** PRIMO ***')
except TypeError as te: #tratamento de Erro de Tipo (para testar o tipo é necessário tirar o int)
    print(f'** Erro!!! {te}')
except ValueError as ve: #tratamento de Erro de Valor
    print(f'** Erro!!! {ve}')
print('\n*** FIM DO PROGRAMA ***')

