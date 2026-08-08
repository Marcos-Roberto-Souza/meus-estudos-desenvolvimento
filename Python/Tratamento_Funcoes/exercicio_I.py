'''Enunciado
Escreva uma função que recebe um número inteiro como parâmetro de entrada
e retorna o texto "PAR" ou "IMPAR".
Use-a em um programa principal '''

def Paridade(a):
    return 'PAR' if a%2 == 0 else 'IMPAR'
    
# parte principal
n = int(input('Digite um Inteiro: '))
print(Paridade(n))

