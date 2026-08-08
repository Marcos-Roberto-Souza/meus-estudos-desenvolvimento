'''
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo.
A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .

Exemplo de Entrada	   |      Exemplo de Saída
-----------------------|--------------------------------------
7 8 9 10	           |  O JOGO DUROU 2 HORA(S) E 2 MINUTO(S) |
_______________________|_____________________________________|
7 7 7 7                | JOGO DUROU 24 HORA(S) E 0 MINUTO(S)  |
_______________________|______________________________________|
7 10 8 9	           | O JOGO DUROU 0 HORA(S) E 59 MINUTO(S)|
_______________________|_____________________________________|

'''

horaInicial, minutoInicial, horaFinal , minutoFinal= map(int, input().split())

inicio = horaInicial*60 + minutoInicial
fim = horaFinal*60 + minutoFinal

if fim <=inicio:
    fim+= 24*60

duracao = fim - inicio

horas = duracao//60
minutos = duracao%60

print(f"O JOGO DUROU {int(horas)} HORA(S) E {int(minutos)} MINUTO(S)")

