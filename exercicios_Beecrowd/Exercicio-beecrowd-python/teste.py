numeros=[]
numero1,numero2, numero3 = map(int, input().split(" "))

#numeros=[numero1, numero2, numero3] #Posso inlcuir os números digitados da variavel na lista ou adicionar Um a Um no append;

numeros.append(numero1)
numeros.append(numero2)
numeros.append(numero3)

print(f"{sum(numeros)}")
print(type(numeros))