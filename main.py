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
    dadosCarroFila.append(f"Momento de adição: {dataEHora}")
    #print(dadosCarroFila[0], dadosCarroFila[1])

    filaDeEntrada.append(dadosCarroFila)
    print("Carro adicionado à fila de entrada.\n")

def adicionarCarroPilha():
    pointer = filaDeEntrada.first
    if pointer is None:
        print("Não há carros na fila para se adicionar na pilha.\n")
        return
    dataEHora = datetime.now()
    dataEHora = dataEHora.strftime('%d/%m/%Y %H:%M')

    dadosCarro = pointer.data
    dadosCarro.tail.data = f"Momento de adição: {dataEHora}"
    pilhaDeSaida.append(dadosCarro)
    filaDeEntrada.remove()

    placa = dadosCarro.head.data.placa
    marcaModelo = f"{dadosCarro.head.data.marca} {dadosCarro.head.data.modelo}"
    cor = dadosCarro.head.data.cor
    print(f"Carro {marcaModelo} {cor} de placa {placa} removido da fila de entrada e adicionado à pilha de estacionamento.\n")

def retirarCarroPilha():
    pointer = pilhaDeSaida.last
    if pointer is None:
        print("A pilha está vazia.\n")
        return
    dadosCarro = pointer.data
    placa = dadosCarro.head.data.placa
    marcaModelo = f"{dadosCarro.head.data.marca} {dadosCarro.head.data.modelo}"
    cor = dadosCarro.head.data.cor

    pilhaDeSaida.remove()
    print(f"Carro {marcaModelo} {cor} de placa {placa} removido da pilha de estacionamento.\n")

    print("Gerando preço do estacionamento...\n")
    arvoreDePreco = ArvoreValor()
    arvoreDePreco.decidir_preco()
    

def mostrarFila():
    posicaoFila = 1
    pointer = filaDeEntrada.first
    if pointer is None:
        print("A fila está vazia.\n")
        return
    while pointer:
        dadosCarro = pointer.data
        carro = dadosCarro.head.data
        horaEData = dadosCarro.tail.data

        print(f"Posição na fila: {posicaoFila}\n{carro}\n{horaEData}\n")
        pointer = pointer.next
        posicaoFila += 1 
def mostrarPilha():
    posicaoPilha = 1
    pointer = pilhaDeSaida.last
    if pointer is None:
        print("A pilha está vazia.\n")
        return
    while pointer:
        dadosCarro = pointer.data
        carro = dadosCarro.head.data
        horaEData = dadosCarro.tail.data

        print(f"Posição na pilha: {posicaoPilha}\n{carro}\n{horaEData}\n")
        pointer = pointer.previous
        posicaoPilha += 1 

print("Bem vindo ao SECCOS: Sistema de Estacionamento de Carros Ozzy OSborne\n")

while True:
    print("Selecione uma opção\n")
    print("1. Adicionar um carro à fila de entrada.")
    print("2. Permitir entrada de carro no estacionamento")
    print("3. Ver fila de entrada")
    print("4. Ver pilha de saída")
    print("5. Retirar carro em pilha e gerar preço")
    print("6. Sair")
    escolha = int(input("Escolha: "))
    if escolha == 1:
        print("\n")
        adicionarCarroFila()
    elif escolha == 2:
        print("\n")
        adicionarCarroPilha()
    elif escolha == 3:
        print("\n")
        mostrarFila()
    elif escolha == 4:
        print("\n")
        mostrarPilha()
    elif escolha == 5:
        print("\n")
        retirarCarroPilha()
    elif escolha == 6:
        print("\nSaindo...")
        exit()
    else:
        print("\nDigite uma escolha válida.\n")