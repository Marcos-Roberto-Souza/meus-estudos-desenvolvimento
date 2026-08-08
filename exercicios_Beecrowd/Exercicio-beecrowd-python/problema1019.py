'''
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica,
e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.
'''
tempoDuracao = int(input())

horas = tempoDuracao//3600
tempoDuracao = tempoDuracao%3600

minutos = tempoDuracao//60
segundos = tempoDuracao%60

print(f"horas: {horas:.0f} --> Minutos: {minutos:.0f} --> Segundos: {segundos:.0f}")