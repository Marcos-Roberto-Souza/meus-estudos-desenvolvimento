'''Enunciado
Escreva um programa que leia quatro notas de um aluno, calcule a média e mostre a situação do aluno
que será 'APROVADO' ou 'REPROVADO'.
O programa deve ler as quatro notas separadas por um espaço em branco em uma mesma linha de digitação.
As notas lidas devem ser separadas, convertidas para número Real e inseridas em uma lista,
junto com a média e a situação do aluno.
Isso tudo deverá ser feito dentro de uma função.
Médias apartir de 7.0 indicam aprovação; menor que isso é Reprovação.

A ordem das notas na digitação deve ser: P1 P2 P3 NT

Escreva o programa principal para testar sua função, A saída deste programa deve
mostrar todas as notas, a média e a situação (Você é livre para elaborar o layout de saída).

Cálculo Média MF = 0,3*P1 + 0,3*P2 + 0,3*P3 + 0,1*NT '''

def CalculaMedia(pNotas):
    #Recebe a string pNotas, faz a separação dos valores, calcula e retorna a média
    pNotas = pNotas.split()
    for i in range(len(pNotas)):
        pNotas[i] = float(pNotas[i])
    media = (pNotas[0] + pNotas[1] + pNotas[2])*0.3 + pNotas[3] * 0.1
    situacao = 'APROVADO' if media >= 7 else 'REPROVADO'
    pNotas.append(media)
    pNotas.append(situacao)
    return pNotas
notas = input('Digite 4 Notas (P1 P2 P3 NT): ')
Resultado = CalculaMedia(notas)
print(f'P1 = {Resultado[0]:.1f}; ',end='')
print(f'P2 = {Resultado[1]:.1f}; ',end='')
print(f'P3 = {Resultado[2]:.1f}; ',end='')
print(f'NT = {Resultado[3]:.1f}; ',end='')
print(f'MÉDIA = {Resultado[4]:.1f}; ',end='')
print(f'SITUAÇÃO = {Resultado[5]}')


print('*** FIM DO PROGRAMA ***')
