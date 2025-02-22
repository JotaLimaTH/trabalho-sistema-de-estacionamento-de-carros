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
def pesquisarCarro():
    print("Digite por qual parâmetro você deseja pesquisar.\n")
    print("1. Placa")
    print("2. Marca")
    print("3. Cor")
    print("4. Modelo")
    print("5. Ano")
    print("6. Cancelar pesquisa.")
    escolha = int(input("Digite sua escolha: "))

    if escolha == 1:
        posicaoFila = 0
        posicaoPilha = 0
        placa = input("Digite a placa do carro: ")
        pointer = filaDeEntrada.first
        if pointer is None:
            pointer = pilhaDeSaida.last
        if pointer is None:
            print("A fila e a pilha estão vazias.\n")
            return
        while pointer:
            dadosCarro = pointer.data
            carro = dadosCarro.head.data
            horaEData = dadosCarro.tail.data
            if carro.placa == placa:
                print(f"Encontrado na fila de entrada.\n\nPosição na fila: {posicaoFila}\n{carro}\n{horaEData}")
                return
            pointer = pointer.next
            posicaoFila += 1
        pointer = pilhaDeSaida.last
        if pointer is None:
            print("A pilha está vazia.")
            return
        while pointer:
            dadosCarro = pointer.data
            carro = dadosCarro.head.data
            horaEData = dadosCarro.tail.data
            if carro.placa == placa:
                print(f"Encontrado na pilha de saída.\n\nPosição na fila: {posicaoPilha}\n{carro}\n{horaEData}")
                return
            pointer = pointer.previous
            posicaoPilha += 1
        print(f"Carro de placa {placa} não encontrado.")
        return

    elif escolha == 2:
        posicaoFila = 0
        posicaoPilha = 0
        marca = input("Digite a marca do carro: ")
        pointer = filaDeEntrada.first
        if pointer is None:
            pointer = pilhaDeSaida.last
        if pointer is None:
            print("A fila e a pilha estão vazias.\n")
            return
        while pointer:
            dadosCarro = pointer.data
            carro = dadosCarro.head.data
            horaEData = dadosCarro.tail.data
            if carro.marca == marca:
                print(f"Encontrado na fila de entrada.\n\nPosição na fila: {posicaoFila}\n{carro}\n{horaEData}")
            pointer = pointer.next
            posicaoFila += 1
        pointer = pilhaDeSaida.last
        if pointer is None:
            return
        while pointer:
            dadosCarro = pointer.data
            carro = dadosCarro.head.data
            horaEData = dadosCarro.tail.data
            if carro.marca == marca:
                print(f"Encontrado na pilha de saída.\n\nPosição na fila: {posicaoPilha}\n{carro}\n{horaEData}")
            pointer = pointer.previous
            posicaoPilha += 1
        return
    elif escolha == 3:
        posicaoFila = 0
        posicaoPilha = 0
        cor = input("Digite a cor do carro: ")
        pointer = filaDeEntrada.first
        if pointer is None:
            pointer = pilhaDeSaida.last
        if pointer is None:
            print("A fila e a pilha estão vazias.\n")
            return
        while pointer:
            dadosCarro = pointer.data
            carro = dadosCarro.head.data
            horaEData = dadosCarro.tail.data
            if carro.cor == cor:
                print(f"Encontrado na fila de entrada.\n\nPosição na fila: {posicaoFila}\n{carro}\n{horaEData}")
            pointer = pointer.next
            posicaoFila += 1
        pointer = pilhaDeSaida.last
        if pointer is None:
            return
        while pointer:
            dadosCarro = pointer.data
            carro = dadosCarro.head.data
            horaEData = dadosCarro.tail.data
            if carro.cor == cor:
                print(f"Encontrado na pilha de saída.\n\nPosição na fila: {posicaoPilha}\n{carro}\n{horaEData}")
            pointer = pointer.previous
            posicaoPilha += 1
    elif escolha == 4:
        posicaoFila = 0
        posicaoPilha = 0
        modelo = input("Digite o modelo do carro: ")
        pointer = filaDeEntrada.first
        if pointer is None:
            pointer = pilhaDeSaida.last
        if pointer is None:
            print("A fila e a pilha estão vazias.\n")
            return
        while pointer:
            dadosCarro = pointer.data
            carro = dadosCarro.head.data
            horaEData = dadosCarro.tail.data
            if carro.modelo == modelo:
                print(f"Encontrado na fila de entrada.\n\nPosição na fila: {posicaoFila}\n{carro}\n{horaEData}")
            pointer = pointer.next
            posicaoFila += 1
        pointer = pilhaDeSaida.last
        if pointer is None:
            return
        while pointer:
            dadosCarro = pointer.data
            carro = dadosCarro.head.data
            horaEData = dadosCarro.tail.data
            if carro.modelo == modelo:
                print(f"Encontrado na pilha de saída.\n\nPosição na fila: {posicaoPilha}\n{carro}\n{horaEData}")
            pointer = pointer.previous
            posicaoPilha += 1
    elif escolha == 5:
        posicaoFila = 0
        posicaoPilha = 0
        ano = input("Digite o ano do carro: ") 
        pointer = filaDeEntrada.first
        if pointer is None:
            pointer = pilhaDeSaida.last
        if pointer is None:
            print("A fila e a pilha estão vazias.\n")
            return
        while pointer:
            dadosCarro = pointer.data
            carro = dadosCarro.head.data
            horaEData = dadosCarro.tail.data
            if carro.ano == ano:
                print(f"Encontrado na fila de entrada.\n\nPosição na fila: {posicaoFila}\n{carro}\n{horaEData}")
            pointer = pointer.next
            posicaoFila += 1
        pointer = pilhaDeSaida.last
        if pointer is None:
            return
        while pointer:
            dadosCarro = pointer.data
            carro = dadosCarro.head.data
            horaEData = dadosCarro.tail.data
            if carro.ano == ano:
                print(f"Encontrado na pilha de saída.\n\nPosição na fila: {posicaoPilha}\n{carro}\n{horaEData}")
            pointer = pointer.previous
            posicaoPilha += 1
    else:
        return

print("Bem vindo ao SECCOS: Sistema de Estacionamento de Carros Ozzy OSborne\n")

while True:
    print("Selecione uma opção\n")
    print("1. Adicionar um carro à fila de entrada.")
    print("2. Permitir entrada de carro no estacionamento")
    print("3. Ver fila de entrada")
    print("4. Ver pilha de saída")
    print("5. Retirar carro em pilha e gerar preço")
    print("6. Pesquisar carro.")
    print("7. Sair")
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
        print("\n")
        pesquisarCarro()
    elif escolha == 7:
        print("\nSaindo...")
        exit()
    else:
        print("\nDigite uma escolha válida.\n")