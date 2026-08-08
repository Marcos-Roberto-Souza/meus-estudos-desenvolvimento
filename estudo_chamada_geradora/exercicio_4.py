''' Enunciado
Escreva um programa que implemente uma função geradora capaz de calcular a média móvel
de uma sequência de números.
A média móvel é calculada e apresentada a cada valor que é fornecido.
utilize uma função geradora que contenha uma expressão yield e use o método, send()
para enviar os valores para a função.
Exibir os valores com 3 casa decimais ex. (1.263).'''

def media_movel():
    total = qtde = 0
    while True:
        novo_dado = (yield total / qtde if qtde > 0 else 0)
        if novo_dado is not None:
            total += novo_dado
            qtde +=1

gen = media_movel()
next(gen)
valor = input('Digite um valor ( ou Fim para encerrar): ')
while valor.upper()!= 'FIM':
    resultado = gen.send(float(valor))
    print(f'Média Móvel Atual == {resultado:.3f}')
    valor = input('Digite um valor (ou FIM para encerrar: ')

print(f'VALOR FINAL DA MÉDIA = {resultado:.3f}')

print('\n\n*** FIM DO PROGRAMA ***')
