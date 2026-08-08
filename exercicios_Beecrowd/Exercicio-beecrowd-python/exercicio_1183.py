# Leitura da operação
operacao = input().strip().upper()

# Leitura da matriz 12x12
matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)

# Processar somente os elementos acima da diagonal principal (j > i)
soma = 0
contador = 0
for i in range(12):
    for j in range(i+1, 12):
        soma += matriz[i][j]
        contador += 1

# Saída com base na operação
if operacao == 'S':
    print(f'{soma:.1f}')
elif operacao == 'M':
    media = soma / contador
    print(f'{media:.1f}')
