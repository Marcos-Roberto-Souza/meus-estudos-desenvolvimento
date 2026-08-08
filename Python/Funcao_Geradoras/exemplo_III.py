'''O incremento do send pode ser 1 ou 0 qualquer outro valor vai dar
erro ou gerar valor undefine'''

def fg():
    resto = 0
    num = 2
    while True:
        if num % 2 ==resto:
            dado = (yield num)
            if dado is not None:
                if dado not in (0,1):
                    raise ValueError(f'Esperado 0 ou 1 =  e foi passado {dado}')
                resto = dado
                num = 0
        num += 1

gen = fg()
print('Gera 5 valores pares')
for _ in range(5):
    print(next(gen), end=' ')

print('\n Gera 5 Valores Impares')
ret = gen.send(1)
print(ret, end=' ')
for _ in range(4):
    print(next(gen), end=' ')

#ret = gen.send(2)

print("*** Fim do Programa ***")

