'''
entrada = input()
temperatura = float(entrada)

if temperatura < 36.0:
    print("Hypothermia")
elif temperatura >= 36.0 and temperatura <= 37.5:
    print("Normal")
elif temperatura > 37.5:
    print("Fever")
'''
# Converte a entrada para float para permitir comparação decimal
temperatura = float(input())

# TODO: Implemente a decisão condicional para imprimir "Atendimento imediato" se a temperatura for maior ou igual a 37.5, ou "Aguardar" caso contrário.
if temperatura <= 37.5:
  print("Atendimento imediato")
