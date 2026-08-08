'''Enunciado
Escreva um programa que permaneça em laço lendo números inteiros até que seja digitado 0
todos os valores digitados, exceto o zero, devem ser gravados em um arquivo em disco, um por linha.
Usar o método .write()'''

arq = open('saída_er_11.1.txt', 'w')
A = int(input(' Digite um Inteiro:'))
while A != 0:
    arq.write(f'{A}\n')
    A = int(input('Digite um inteiro: '))
arq.close()


print('\n*** FIM DO PROGRAMA ***')
