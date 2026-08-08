op = input().strip()
M = []

# Leitura da matriz 12x12
for _ in range(12):
    linha = []
    for _ in range(12):
        linha.append(float(input()))
    M.append(linha)

soma = 0.0
cont = 0

# Define os limites da área inferior corretamente
for i in range(7, 12):
    for j in range(12 - i, i):
        soma += M[i][j]
        cont += 1

# Mostra o resultado com uma casa decimal
if op == 'S':
    print(f"{soma:.1f}")
elif op == 'M':
    print(f"{soma / cont:.1f}")
