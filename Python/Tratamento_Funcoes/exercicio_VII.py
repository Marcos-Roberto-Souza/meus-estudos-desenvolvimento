''' Enunciado
Escreva um programa que utilize uma função recursiva para realizar uma contagem regressiva,
Este programa deve ler do teclado um inteiro que representa a quantidade de toques dessa contagem
regressiva.
Quando a contagem chegar em zero o programa deve exibir na tela a mensagem *NO AR!!!* '''
from time import sleep

def Contagem(Cont):
    if Cont == 0:
        print('NO AR!!!')
    else:
        print(Cont)
        sleep(1)
        Contagem(Cont-1)


toque = int(input('Digite a quantidade de toques: '))
print(f'Atenção para o toque de {toque} segundos')
Contagem(toque)
