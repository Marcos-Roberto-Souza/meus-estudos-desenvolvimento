Lista = [31, -17, 26, 15, -35, -9, 20]
#modo add list simples
modo1 = []
for x in Lista:
    modo1.append(x*2)
print(f'{modo1}\n')

print('*** MODO LIST COMPREHENSION ***\n')
#modo add list comprehension
modo2 = [x * 2 for x in Lista]

print(modo2)

