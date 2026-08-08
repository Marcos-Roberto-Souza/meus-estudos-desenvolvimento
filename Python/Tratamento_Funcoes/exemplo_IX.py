L = [8, 5, 3, 9, 7, 2]
def quadrado(a):
    return a ** 2

print('FUNÇÃO MAP LIST ELEVANDO AO QUADRADO')
L2 = list(map(quadrado, L))
for x in L2:
    print(x)
    
print('\n FUNÇÃO LAMBIDA ABAIXO ELEVANDO AO CUBO')    
L3 = list(map((lambda x: x ** 3), L))
for x in L3:
    print(x)
