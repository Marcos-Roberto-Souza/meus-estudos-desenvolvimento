def funcao1():
    print('dentro da funcao1 temos >>', a, b)

def funcao2():
    a = 100 #objeto de escopo local
    b = 200 #objeto de escopo local
    print('dentro da funcao2 temos >> ', a, b)

#parte principal - define os objetos de escopo global
a = 10
b = 20
funcao1()
funcao2()
print('fora da funções temos >>', a, b)

''' Nunca defina o mesmo nome da função local com mesmo nome da global,
sempre defina nomes diferentes da local ou global.'''

