 #Lê a operação: 'S' para soma ou 'M' para média
operacao = input().strip().upper()

# Lê a matriz 12x12
matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)

# Calcula soma e quantidade dos elementos ACIMA da diagonal secundária (i + j < 11)
soma = 0.0
contador = 0

for i in range(12):
    for j in range(12):
        if i + j < 11:
            soma += matriz[i][j]
            contador += 1

# Imprime resultado com 1 casa decimal
if operacao == 'S':
    print(f"{soma:.1f}")
elif operacao == 'M':
    media = soma / contador
    print(f"{media:.1f}")
else:
    print("Operação inválida. Use 'S' ou 'M'.")
