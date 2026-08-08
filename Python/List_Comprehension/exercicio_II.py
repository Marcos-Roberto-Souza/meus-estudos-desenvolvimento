'''Enunciado
Escreva um programa que converta uma lista de temperaturas registradas na escala
Fahrenheit para graus na escala Celsius.
Exibir os Valores resultantes com uma casa decimal.
A conversão é feita com uso da seguinte fórmula:
        *** Celsius = (Fahrenheit - 32)* 5/9
'''
#TempF = [83, 91, 79, 95, 104, 100, 98]

TempF = []
a = int(input('Digite a Quantidade de Temperatura para adicionar a Lista: '))
for i in range (a): # quantidade a ser adicionada
    x = float(input('Digite a Temperatura: '))
    TempF.append(x) #adicionando as temperatura Fahrenheit
    

print('\n *** Mostrando a Conversão de Fahrenheit em Graus Celsius ***\n')
TempC = [(lambda fahr: (fahr-32)*5/9)(x) for x in TempF] #Fazendo a Conversão para Graus Celsius
for tc in TempC:#mostrando na tela em sequência de linha
    print(f'A temperatura em Graus C é {tc:.1f}',end='\n')


print('\n*** FIM DO PROGRAMA ***')

