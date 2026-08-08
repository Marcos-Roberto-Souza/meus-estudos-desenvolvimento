
'''nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

print(nome, idade)
print(nome, idade, end="...\n")
print(nome, idade, sep="#")
print(5//2)'''
entrada = input()
abertura_str, fechamento_str = entrada.split()

# Converte os valores para inteiros
abertura = int(abertura_str)
fechamento = int(fechamento_str)

if abertura < fechamento:
    print("ALTA")
elif abertura > fechamento:
    print("BAIXA")
elif abertura == fechamento:
    print("ESTAVEL")