# Operadores Aritméticos 
# + Adição
# - Subtração
# * Multiplicação
# / Divisão
# // Divisão Inteira
# % Resto da Divisão ou modulo
# ** Exponenciação  

print(10 + 5)
print(10 - 5)   
print(10 * 5)
print(10 / 5)
print(10 // 3)
print(10 % 3) 
print(2 ** 3)
saldo = 500

def sacar(valor:float):
    
    
    if saldo >= valor:
        print("Valor sacado com sucesso!")
        print("Retire o seu dinheiro no caixa eletrônico.")
           
sacar(200)
saldo_atual = saldo - 200
print("Saldo atual:", saldo_atual)