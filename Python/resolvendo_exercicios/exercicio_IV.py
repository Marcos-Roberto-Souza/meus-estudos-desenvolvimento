'''Enunciado
Escreva um programa que permaneça, que leia um arquivo de entrada, sabendo que esse arquivo
tem um número inteiro em cada linha.
Todods os números lidos devem ser mostrados na tela.
Mostrar também a **soma dos valores, **a quantidade, **a média aritmética, ** o menor valor e o maior valor.
Usar aqui o mesmo arquivo de entrada do exercicio anterior.
Usar um iterador for e o arquivo como iterável. '''

Lst = []


for linha in open('entrada_er_11.4.txt', 'r'):
    Lst.append(int(linha))

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
