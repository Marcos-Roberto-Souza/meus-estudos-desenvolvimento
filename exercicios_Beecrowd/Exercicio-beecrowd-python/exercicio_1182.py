coluna = int(input())
operacao = input().strip().upper()

# Leitura da matriz 12x12
matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)

# Soma dos elementos da coluna indicada
soma = 0
for i in range(12):
    soma += matriz[i][coluna]

# Saída conforme operação
if operacao == 'S':
    print(f'{soma:.1f}')
elif operacao == 'M':
    media = soma / 12
    print(f'{media:.1f}')
