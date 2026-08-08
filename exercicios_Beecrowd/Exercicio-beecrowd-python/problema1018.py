from unittest import result

deposito = int(input())

print(deposito)

cedulas = [100, 50, 20, 10, 5, 2, 1]

for cedula in cedulas:
    quantidade = deposito // cedula
    print(f"{quantidade} nota(s) de R$ {cedula},00")
    deposito %= cedula