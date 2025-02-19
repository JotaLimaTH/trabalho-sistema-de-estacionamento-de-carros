class NoArvore:
    def __init__(self, pergunta, sim=None, nao=None, horas=0):
        self.pergunta = pergunta
        self.sim = sim
        self.nao = nao
        self.horas = horas

class ArvoreValor:
    def __init__(self):
        self.raiz = self.criar_arvore()

    def criar_arvore(self):
        refeicao = NoArvore("Fez uma refeição no shopping?", horas=1)
        cinema = NoArvore("Foi ao cinema?", sim=refeicao, nao=None, horas=2)
        loja = NoArvore("Visitou alguma loja?", sim=cinema, nao=refeicao, horas=1)

        supermercado = NoArvore("Fez compras no supermercado?", horas=1)
        valor_compra = NoArvore("As compras custaram R$ 40,00 ou mais?", sim=loja, nao=loja)

        supermercado.sim = valor_compra
        supermercado.nao = loja

        return supermercado

    def decidir_preco(self):
        nodo_atual = self.raiz
        total_horas = 0
        gratuidade = False

        while nodo_atual:
            if nodo_atual.pergunta is None:
                break

            resposta = input(nodo_atual.pergunta + " (s/n) ").strip().lower()
            if resposta == "s":
                total_horas += nodo_atual.horas
                if nodo_atual.pergunta == "As compras custaram R$ 40,00 ou mais?":
                    gratuidade = True

                nodo_atual = nodo_atual.sim
            else:
                nodo_atual = nodo_atual.nao
        if gratuidade:
            preco = 0
        else:
            preco = max(10, total_horas * 5)
        print(f"Preço do estacionamento: R$ {preco},00")

arvore = ArvoreValor()
arvore.decidir_preco()
