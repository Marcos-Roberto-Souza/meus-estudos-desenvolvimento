#Metodos mais utilizados da classe string
#upper() - Deixa todas as letras maiusculas
#lower() - Deixa todas as letras minusculas
#capitalize() - Deixa a primeira letra maiuscula e as demais minusculas
#title() - Deixa a primeira letra de cada palavra maiuscula e as demais minusculas
#strip() - Remove os espaços em branco no início e no final da string
#split() - Divide a string em uma lista de palavras
#join() - Junta os elementos de uma lista em uma string, utilizando um separador
#lstrip() - Remove os espaços em branco no início da string
#rstrip() - Remove os espaços em branco no final da string
#center() - Centraliza a string em um campo de largura especificada, preenchendo os espaços vazios com um caractere opcional


texto = "Olá, mundo!"
print(texto.upper(),"Upper")
print(texto.lower(),"Lower")
print(texto.capitalize(),"Capitalize")
print(texto.title(),"Title")
texto_com_espacos = "   Olá, mundo!   "
print(texto_com_espacos.strip(),"Strip")
texto_dividido = texto.split()
print(texto_dividido,"Split")
texto_junto = "-".join(texto_dividido)
print(texto_junto,"Join")
print(texto_com_espacos.center(10, "#"),"Center")

curso = "Python "
print(curso[0])
