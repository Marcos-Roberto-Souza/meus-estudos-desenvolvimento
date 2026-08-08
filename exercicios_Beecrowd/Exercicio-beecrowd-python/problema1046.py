'''
Leia a hora inicial e a hora final de um jogo.
A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro,
tendo uma duração mínima de 1 hora e máxima de 24 horas.

Entrada
A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.

Saída
Apresente a duração do jogo conforme exemplo abaixo.

Exemplo de Entrada	        Exemplo de Saída
-----------------------------------------------
16 2                |O JOGO DUROU 10 HORA(S)
____________________|_________________________
0 0                 |O JOGO DUROU 24 HORA(S)
____________________|___________________________
2 16                |O JOGO DUROU 14 HORA(S)
____________________|___________________________

'''

horaInicial, horaFinal = map(int, input().split())

if horaInicial == horaFinal :
    termino = 24
elif horaInicial < horaFinal:
    termino = horaFinal-horaInicial
else:
    termino = (24-horaInicial) + horaFinal

print(f"O JOGO DUROU {int(termino)} HORA(S)")

