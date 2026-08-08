L = []
x = int(input())
valores = list(map(int, input().split()))

menor_valor = min(valores)
posicao_menor = valores.index(menor_valor)

print(f'Menor valor: {menor_valor}')
print(f'Posicao: {posicao_menor}')
