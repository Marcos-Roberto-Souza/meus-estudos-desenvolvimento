'''Enunciado
Escreva uma função que receba como parâmetro de entrada um número inteiro de 5 digitos
de [10000,99999] que represente códigos de produtos vendidos em uma loja.
A função deve calcular e retornar o digito verificador utilizando a regra de calculo
explicada a seguir.
Escreva o programa principal para testar a função.
Considere o código 31483, em que cada digito é multiplicado por um peso começando em 2
e termina em 6.
Os valores obtidos são somados, e do total obtido calcula-se o resto de sua divisão por 7.

Dígito         3 1  4  8  3
peso           2 3  4  5  6
Multiplicação  6 3 16 40 18       Soma de todos = 83
                                  Resto de 83 por 7 = 6
'''
def CalculaDigito(cod):
    s = str(cod)
    peso = 2
    dv = 0
    for a in s:
        dv += peso *int(a)
        peso += 1
    return dv % 7
codigo = int(input('Digite o Código: '))
while codigo > 0:
    digito = CalculaDigito(codigo)
    print(f'Código: {codigo} --> digito: {digito}')
    codigo = int(input('Digite o código: '))

print('*** FIM DO PROGRAMA ***')
