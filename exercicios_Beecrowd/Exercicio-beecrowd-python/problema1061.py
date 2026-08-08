dia_inicio = int(input().split()[1])

horaInicio, minutoInicio, segundoInicio = map(int, input().split(" : "))

diaFim = int(input().split()[1])

horaFinal, minutoFinal, segundoFinal = map(int, input().split(" : "))

inicio_total = (
    dia_inicio * 24 * 3600 +
    horaInicio * 3600 +
    minutoInicio * 60 +
    segundoInicio
)

fim_total = (
    diaFim * 24 * 3600 +
    horaFinal * 3600 +
    minutoFinal * 60 +
    segundoFinal
)

diferenca = fim_total - inicio_total

dias = diferenca // (24*3600)
diferenca %= (24*3600)

horas = diferenca // 3600
diferenca %= 3600

minutos = diferenca // 60
diferenca %= 60

segundos = diferenca

print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')