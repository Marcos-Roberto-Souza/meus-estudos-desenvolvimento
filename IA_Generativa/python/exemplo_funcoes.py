def hello_nome(nome, idade, ano_atual, ano_nascimento):
    print("\nO Ano atual é: ", ano_atual)
    print("Seu Ano de nascimento é: ", ano_nascimento)
    print("\nSeu Nome é, ", nome, "\nSua idade atual é: ", idade, "anos")

entrada = str(input("Digite seu nome: "))
ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = ano_atual - ano_nascimento
hello_nome(entrada,idade, ano_atual, ano_nascimento)