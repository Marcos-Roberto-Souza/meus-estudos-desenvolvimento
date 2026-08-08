# Lê a operação: 'S' para soma ou 'M' para média
operacao = input().strip().upper()

# Lê os 144 elementos da matriz 12x12
matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

# Soma e conta os elementos na ÁREA SUPERIOR (i < j)
soma = 0.0
contador = 0

for i in range(12):
    for j in range(12):
        if i < j:  # área superior
            soma += matriz[i][j]
            contador += 1

# Imprime o resultado com 1 casa decimal
if operacao == 'S':
    print(f"{soma:.1f}")
elif operacao == 'M':
    print(f"{soma / contador:.1f}")
else:
    print("Operação inválida.")
