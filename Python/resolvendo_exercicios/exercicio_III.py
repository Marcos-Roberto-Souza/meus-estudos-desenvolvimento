'''Enunciado
Escreva um program que permaneça que leia um arquivo de entrada, sabendo que esse arquivo tem
um número inteiro em cada linha. Todos os números lidos devem ser mostrados na tela.
Mostrar também a soma dos valores, a quantidade, a média aritmética, o menor valor e o maior valor.
Usar um laço while e na leitura usar o método .readline()
'''
Lst = []
arqEnt = open('entrada_er_11.4.txt', 'r')
linha = arqEnt.readline()
while linha != '':
    Lst.append(int(linha))
    linha = arqEnt.readline()
arqEnt.close()
print('Lista lida do arquivo')
print(Lst)
Soma = sum(Lst) #calcula a soma dos elementos da lista
print(f'Soma dos VALORES = {Soma}')
Qtde = len(Lst) #determia a quantidade dos elementos da lista
print(f'Quantidade = {Qtde}')
print(f'Média dos VALORES = {Soma/Qtde}')
Minimo = min(Lst)   #determina o menor elemento da lista
print(f'Minimo dos VALORES = {Minimo}')
Maximo = max(Lst)   #determina o maior elemento da lista
print(f'Maximo dos VALORES = {Maximo}')
print('\n*** FIM DO PROGRAMA ***')
