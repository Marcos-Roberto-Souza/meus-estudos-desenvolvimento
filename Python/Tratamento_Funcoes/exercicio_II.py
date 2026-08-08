'''Enunciado
Escreva uma função que receba dois números inteiros A e B como parâmetros de entrada
e retorne TRUE se A for divisível por B e False caso contrário.
Escreva o programa principal para testar a função. '''

def Divisivel(A , B):
    return True if A%B==0 else False

x = int(input('Digite o Primeiro Valor: '))
y = int(input('Digite o Segundo Valor: '))

if Divisivel(x, y):
    print(f'{x} é divisivel por {y}')
else:
    print(f'{x} não é divisivel por {y}')

