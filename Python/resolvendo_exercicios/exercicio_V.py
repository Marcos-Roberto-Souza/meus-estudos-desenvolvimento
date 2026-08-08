'''Enunciado
Escreva um programa que leia um arquivo de entrada carregando seus dados em um dicionário
e ao final exibindo-os na tela.
A figura 11.1 mostra do lado esquerdo a natureza dos dados que serão lidos edo lado direito
mostra o formato do arquivo.
Esse formato é conhecido como CSV, Arquivos CSV são muito usados em diversas áreas da computação,
em especial em Análise de Dados. O que caracteriza um arquivo CSV é que cada linha tem um
conjunto de dados de alguma forma relacionados e separados por um caractere delimitador.
No arquivo deste exercicio o delimitador é um ponto-e-virgula ( ; ) .
Neste caso, cada linha tem: código de produto(int), a quantidade em estoque(int),
preço(float)'''

Estoque = {}
for linha in open('entrada_er_11.5.txt', 'r'):
    lst = linha.rstrip().split(';')
    print(lst)
    cod = int(lst[0])
    qtde = int(lst[1])
    pcunit = float(lst[2])

    Estoque[cod] = (qtde, pcunit)
print('VALORES CARREGADOS NO DICIONÁRIO')
print(Estoque)

print('\n\nExibição dos dados na forma de tabela')
TotalGeral = 0
for cod, dados in Estoque.items():
    tot = dados[0] * dados[1]
    TotalGeral += tot
    print(f' {cod}: {dados[0]:5d} x {dados[1]:6.2f} = {tot:8.2f}')
print(' ' * 24, f'{TotalGeral:8.2f}')
print('\n *** FIM DO PROGRAMA ***')
