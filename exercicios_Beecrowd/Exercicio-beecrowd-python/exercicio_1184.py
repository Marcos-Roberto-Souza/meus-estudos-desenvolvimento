# Lê a operação: 'S' para soma, 'M' para média
operacao = input().strip().upper()

# Lê os 144 valores da matriz
matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)

# Calcula a soma dos elementos **abaixo da diagonal principal**
soma = 0.0
contador = 0

for i in range(12):
    for j in range(12):
        if i > j:  # Abaixo da diagonal principal (linha maior que a coluna)
            soma += matriz[i][j]
            contador += 1

# Exibe o resultado com 1 casa decimal
if operacao == 'S':
    print(f"{soma:.1f}")
elif operacao == 'M':
    media = soma / contador
    print(f"{media:.1f}")
