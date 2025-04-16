import random
import copy

class Cromossomo:
    def __init__(self, rota):  
        self.rota = rota
        self.aptidao = self.calcular_aptidao()

    def calcular_aptidao(self):
        nota_restricao = 0

        # Penalidade por cidade maior antes de cidade menor (em qualquer posição seguinte)
        for i in range(len(self.rota)):
            for j in range(i + 1, len(self.rota)):
                if self.rota[i] > self.rota[j]:
                    nota_restricao += 10

        # Penalidade por repetição de cidades
        contagem = {}
        for cidade in self.rota:
            contagem[cidade] = contagem.get(cidade, 0) + 1

        for qtd in contagem.values():
            if qtd > 1:
                pares = (qtd * (qtd - 1)) // 2
                nota_restricao += pares * 20

        return nota_restricao
    
    def __str__(self):
        return f'Rota: {self.rota}. Aptidão com penalidade: {self.aptidao}'
    
    def __eq__(self, other):
        return isinstance(other, Cromossomo) and self.rota == other.rota

    @staticmethod
    def gerar_populacao(populacao, tamanho_populacao):
        rota = []
        for _ in range(tamanho_populacao):
            for i in range(1, 10):
                rota.append(i)
            random.shuffle(rota)
            populacao.append(Cromossomo(copy.deepcopy(rota)))
            rota.clear()    

    @staticmethod
    def exibir_populacao(populacao, numero_geracao):
        print(f'\nGeração {numero_geracao}')
        for individuo in populacao:
            print(individuo)

    @staticmethod
    def selecionar(populacao, nova_populacao, taxa_selecao):
        quantidade_selecionados = int(len(populacao) * taxa_selecao / 100)

        torneio = []
        nova_populacao.append(populacao[0])  # elitismo

        i = 1
        while i < quantidade_selecionados:
            c1 = populacao[random.randrange(len(populacao))]
            c2 = c3 = None

            while True:
                c2 = populacao[random.randrange(len(populacao))]
                if c1 != c2:
                    break

            while True:
                c3 = populacao[random.randrange(len(populacao))]
                if c3 != c1 and c3 != c2:
                    break
            
            torneio = [c1, c2, c3]
            torneio.sort(key=lambda c: c.aptidao)
            selecionado = torneio[0]

            if selecionado not in nova_populacao:
                nova_populacao.append(selecionado)
                i += 1

    @staticmethod
    def reproduzir(populacao, nova_populacao, taxa_reproducao):
        quantidade_reproduzidos = int(len(populacao) * taxa_reproducao / 100)

        for _ in range((quantidade_reproduzidos // 2) + 1):
            pai = populacao[random.randrange(len(populacao))].rota
            mae = populacao[random.randrange(len(populacao))].rota
            while pai == mae:
                mae = populacao[random.randrange(len(populacao))].rota

            # Cruzamento
            meio = len(pai) // 2
            filho1 = pai[:meio] + mae[meio:]
            filho2 = mae[:meio] + pai[meio:]

            nova_populacao.append(Cromossomo(filho1))
            nova_populacao.append(Cromossomo(filho2))

            # Podar excedente
            while len(nova_populacao) > len(populacao):
                nova_populacao.pop()

    @staticmethod
    def mutar(populacao):
        quantidade_mutantes = random.randint(1, len(populacao) // 5)

        for _ in range(quantidade_mutantes):
            mutante = random.choice(populacao)
            idx = random.randrange(len(mutante.rota))
            mutante.rota[idx] = random.randint(1, 9)
            mutante.aptidao = mutante.calcular_aptidao()

def algoritmo_genetico():
    TAMANHO_POP = 100
    TAXA_SELECAO = 50  # %
    TAXA_REPRODUCAO = 50  # %

    populacao = []
    Cromossomo.gerar_populacao(populacao, TAMANHO_POP)
    populacao.sort(key=lambda c: c.aptidao)

    geracao = 0
    while True:
        Cromossomo.exibir_populacao(populacao, geracao)

        if populacao[0].aptidao == 0:
            print("\nSolução ótima encontrada!")
            print(populacao[0])
            break

        nova_populacao = []
        Cromossomo.selecionar(populacao, nova_populacao, TAXA_SELECAO)
        Cromossomo.reproduzir(populacao, nova_populacao, TAXA_REPRODUCAO)
        Cromossomo.mutar(nova_populacao)

        # Atualizar aptidão após mutação
        for c in nova_populacao:
            c.aptidao = c.calcular_aptidao()

        nova_populacao.sort(key=lambda c: c.aptidao)
        populacao = nova_populacao
        geracao += 1

if __name__ == "__main__":
    algoritmo_genetico()


## testando algumas vezes o programa a media geral varia mt, as vezes chega em apenas 40 geracoes, e em outros casos leva 150 geracoes contendo 100 possiveis individuos considerando o metodo estocastico deterministico (o melhor sobrevive)