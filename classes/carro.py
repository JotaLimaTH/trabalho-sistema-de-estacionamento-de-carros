class Carro:
    def __init__(self, placa, marca, cor, modelo, ano):
        self.placa = placa
        self.marca = marca
        self.cor = cor
        self.modelo = modelo
        self.ano = ano

    def __str__(self):
        return f"Modelo: {self.modelo} \nPlaca: {self.placa} \nCor: {self.cor} \nAno: {self.ano} \nMarca: {self.marca} "

# Só um teste
carro1 = Carro(4002, "Fiat", "azul", "Mobi", 2023)
print(carro1)