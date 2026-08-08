#Levantamento de Excessão not isinstance
def Paridade(pvalor):
    if not isinstance(pvalor, int):
        raise Exception('A função Paridade deve receber um Inteiro')
    if pvalor %2 == 0:
        return 'PAR'
    else:
        return 'IMPAR'

n = input('Digite algo: ')
r = Paridade(int(n))
print(f'valor de {n} é {r}')
