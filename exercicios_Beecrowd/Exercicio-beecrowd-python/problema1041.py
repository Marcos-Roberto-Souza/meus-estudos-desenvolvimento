'''
Leia 2 valores com uma casa decimal (x e y),
que devem representar as coordenadas de um ponto em um plano.
A seguir, determine qual o quadrante ao qual pertence o ponto,
ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).



Se o ponto estiver na origem, escreva a mensagem “Origem”.

Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação.

Entrada
A entrada contem as coordenadas de um ponto.

Saída
A saída deve apresentar o quadrante em que o ponto se encontra.

Exemplo de Entrada	   Exemplo de Saída
4.5 -2.2            | Q4

Raciocinio para aprimorar o desenvolvimento da condição

| x        | y        | Resultado |
| -------- | -------- | --------- |
| 0        | 0        | Origem    |
| 0        | qualquer | Eixo Y    |
| qualquer | 0        | Eixo X    |
| +        | +        | Q1        |
| -        | +        | Q2        |
| -        | -        | Q3        |
| +        | -        | Q4        |

'''

eixoX, eixoY = map(float, input().split())

if eixoX==0 and eixoY == 0:
    print("Origem")
elif eixoX==0:
    print("Eixo Y")
elif eixoY==0:
    print("Eixo X")
elif eixoX > 0 and eixoY > 0:
    print("Q1")
elif eixoX < 0 and eixoY > 0:
    print("Q2")
elif eixoX < 0 and eixoY < 0:
    print("Q3")
elif eixoX > 0 and eixoY < 0:
    print("Q4")
