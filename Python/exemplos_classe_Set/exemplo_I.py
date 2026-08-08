'''jeito simples de criar um conjunto com dados'''
c1 = {16 , 8, 21, 30, 41, 28}

'''comando para saber o tipo da variavel ou objeto'''
type(c1)
'''comndo para saber o tamanho da variavel ou objeto'''
len(c1)
'''comando set() só aceita um argumento, para colocar mais de um elemento tem que
ser feito uma tupla set((1,2,3)) ou uma lista set([1,2,3]) o construtor criará
o conjunto sem problemas'''
c2 = set((1,2,3))

'''criando conjunto vazio'''
c2 = set()

'''adicionando elemento no conjunto vazio add'''
c2.add(2)

''' Se o algoritmo precisar de ser ordenado não utilize o set, utilize o list'''

'''para limpar utilize o metodo clear'''
c2.clear()

'''para fazer um clone do objeto'''
c2.copy()

''' para verificar o ID do objeto'''
id(c2)

''' para verificar o hash do objeto'''
hash(c2)

''' metodo mostra o que estão em um conjunto mas não esta o outro conjunto'''
c1 = {26, 32, 45, 58, 63}
c2 = {19, 34, 58, 67, 82}
c1.difference(c2)
{32, 26, 45, 63}

'''metodo atualiza o objeto com a diferenca'''
c1.difference_update(c2)

'''metodo remove um elemento'''
c2.discard(58)

''' metodo mostra a interseção'''
c1.intersection(c2)
c1.intersection_update

''' metodo que mostra se o conjunto e dijunto'''
c1.isdisjoint(c2)
'''retorna True se for verdadeir ou False se for Falso.'''

'''metodo que retorna verdadeiro se for subconjunto do outro'''
c1.issubset(c2)

'''metodo quer retorna verdadeiro se o c1 conter todos os elementos do c2'''
c1.issuperset(c2)

'''metodo que remove automaticamente'''
c1.pop()

'''metodo que remove o elemento que digitar e se estiver no conjunto'''
c2.remove(58)

'''metodo que uni dois conjuntos'''
a = c1.union(c2)

'''metodo que mostra a diferença simetrica'''
c1.symmetric_difference(c2)

'''metodo que retorna a união de dois conjuntos'''
c1.update(c2)





