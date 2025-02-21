from datetime import datetime

import sys
sys.path.append("./classes")

from classes.Arvore import *
from classes.carro import *
from classes.queue import *
from classes.stack import *
from classes.double_linked_list import *

filaDeEntrada = Queue()
pilhaDeSaida = Stack()

def adicionarCarroFila():
    placa = input("Digite a placa do carro: ")
    marca = input("Digite a marca do carro: ")
    cor = input("Digite a cor do carro: ")
    modelo = input("Digite o modelo do carro: ")
    ano = input("Digite o ano do carro: ")
    novoCarro = Carro(placa, marca, cor, modelo, ano)

    dataEHora = datetime.now()
    dataEHora = dataEHora.strftime('%d/%m/%Y %H:%M')

    dadosCarroFila = DoubleLinkedList()
    dadosCarroFila.append(novoCarro)
    dadosCarroFila.append("Momento de adição: {dataEHora}")

    filaDeEntrada.append(dadosCarroFila)
    

print("Bem vindo ao SECCOS: Sistema de Estacionamento de Carros Ozzy OSborne\n")

while True:
    print("Selecione uma opção\n")
    print("1. Adicionar um carro à fila de entrada.")
    print("2. Permitir entrada de carro no estacionamento")
    print("3. Ver fila de entrada")
    print("4. Ver pilha de saída")
    print("5. Retirar carro em pilha e gerar preço")
    escolha = int(input("Escolha: "))
    if escolha == 1:
        adicionarCarroFila()