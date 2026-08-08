class Veiculo():
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o Motor")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def esta_carregado(self):
        print("Não estou carregado")

moto = Motocicleta("Vermelha", "AEB-2H55", 2)
print(moto)
moto.ligar_motor()

carro = Carro("Branco", "EEF-6I43", 4)
carro.ligar_motor()

caminhao = Caminhao("Preto", "DDI-6254", 8)
caminhao.ligar_motor()
caminhao.esta_carregado()
