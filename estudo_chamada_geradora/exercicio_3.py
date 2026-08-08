'''Enunciado
Reescreva a função geradora do exercicio_2 de modo que ele passe a receber um
Inteiro através de uma expressão yield.
Esse inteiro deve ser usado para resetar o valor inicial para o qual calcularemos o fatorial.
No programa principalmente leia a quantidade de tuplas a serem geradas e faça um
laço para gerar várias sequências e assim verificar se os retornos da função geradora
estão corretos. '''

def funcao_fatorial():
    num, fat = 0, 1
    while True:
        i = (yield num, fat)
        num += 1
        fat *= num
        if i is not None:
            num, fat = i, 1
            for a in range(1, num+1):
                fat *= num

qtde = int(input('Digite a Quantidade de Fatoriais Desejados: '))
gen = funcao_fatorial()
next(gen)
pm = int(input('\nDigite o valor inicial para os Fatoriais: '))
while pm >= 0:
    r = gen.send(pm)
    fatoriais = [r]
    for _ in range(qtde-1):
        fatoriais.append(next(gen))

    print(f'\nSequência de fatoriais iniciado em {pm}')
    print(fatoriais)

    pm = int(input('\nDigite o valor inicial novamente para os fatoriais: '))

print('\n\n*** FIM DO PROGRAMA ***')
