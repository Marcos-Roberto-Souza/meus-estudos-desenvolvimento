Lista = [31, -17, 26, 15, -35, -9, 20]
modo1 = []
#modo lista simples
for x in Lista:
    modo1.append(x * 2)
print(f'ESTE É O MODO 1\n {modo1}')

#modo list comprehension
modo2 = [x * 2 for x in Lista]
print(f'\nESTE É O MODO 2\n {modo2}')

#modo list comprehension com if
modo3 = [x * 2 for x in Lista if x > 0] #pegando só os positivos modo Comprehension
print(f'\nESTE É O MODO 3\n {modo3}')

#modo simples com if
modo4 = []
for x in Lista:
    if x > 0:
        modo4.append(x * 2) #pegando só os positivos modo simples
print(f'\nESTE É O MODO 4\n {modo4}')
