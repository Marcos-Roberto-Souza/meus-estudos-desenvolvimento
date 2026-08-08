
valor1, valor2, valor3 = input().split()
valor1, valor2, valor3 = int(valor1), int(valor2), int(valor3)

maiorAB = ((valor1 + valor2)+ abs(valor1-valor2))/2

maior = (maiorAB + valor3 + abs(maiorAB-valor3))/2

print(f"{maior:.0f} eh o maior")