# Lê a operação: 'S' (soma) ou 'M' (média)
operacao = input().strip().upper()

# Lê os 144 valores da matriz 12x12
matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

# Soma e conta os elementos ABAIXO da diagonal secundária (i + j > 11)
soma = 0.0
contador = 0

for i in range(12):
    for j in range(12):
        if i + j > 11:          # abaixo (parte inferior) da diagonal secundária
            soma += matriz[i][j]
            contador += 1

# Exibe a saída com 1 casa decimal
if operacao == 'S':
    print(f"{soma:.1f}")
elif operacao == 'M':
    print(f"{soma / contador:.1f}")
else:
    print("Operação inválida (use 'S' ou 'M').")
