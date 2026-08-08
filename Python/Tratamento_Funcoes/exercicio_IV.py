'''Enunciado
Escreva uma função que receba como parâmetro de entrada dois números Reais Min e Max.
Essa função deve ler do teclado um número Real e retorná-lo caso esteja dentro do intervalo
fechado [Min, Max].
Caso contrário, a função deve exibir uma mensagem de erro e ler um novo valor. '''

def lerReal(pMin, pMax):
    a = float(input('Digite um valor Real: '))
    while a < pMin or a > pMax:
        print(f'O valor de {a} está fora dos limites [{pMin}, {pMax}]')
        a = float(input('Digite um valor Real: '))
    return a

Lmin = float(input('Digite o Valor Mínimo: '))
Lmax = float(input('Digite o Valor Máximo: '))

controle = 's'
while controle == 's' or controle == 'S':
    valor = lerReal(Lmin, Lmax)
    print(f'o valor lido é {valor}')
    controle = input('\nQuer digitar outro valor (S/N)? ')

print('*** FIM DO PROGRAMA ***')
