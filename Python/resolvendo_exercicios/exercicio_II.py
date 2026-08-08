'''Enunciado
Escreva um programa que permaneça em laço lendo números reais até que seja digitado 0,
todos os valores digitados, exceto o zero, devem ser gravados em um arquivo em disco.
Um por linha, com três casas decimais.
Usar o Método .writelines()'''
Lst = []
X = float(input('Digite um Numero Real: '))
while X !=0:
    Lst.append(f'{X:.3f}\n')
    X = float(input('Digite um real: '))
print(Lst)
arq = open('saída_er_11.3.txt', 'w')
arq.writelines(Lst)
arq.close()

print('\n *** FIM DO PROGRAMA ***')
