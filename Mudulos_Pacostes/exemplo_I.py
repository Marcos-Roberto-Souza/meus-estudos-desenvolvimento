import numpy

matriz = numpy.empty([12,12])

for linha in range(0,11):
    for coluna in range(0,11):
        print("Digite o valor da linha -->", linha, 'valor da Coluna -->', coluna)
        matriz[linha][coluna] = int(input()) 

