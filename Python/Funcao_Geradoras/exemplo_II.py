def le_arquivo(nome_arq):
    for uma_linha in open(nome_arq, 'r'):
        uma_linha = uma_linha.split(';')
        yield uma_linha[0]
        #yield uma_linha.rstrip()

arquivo = input("Digite o nome do arquivo: ")# passar local e tipo do arquivo para o programa ler e imprimir "exemplo.txt"
for linha in le_arquivo(arquivo):
    print(linha)

print('\n *** FIM DE LINHA ***')
