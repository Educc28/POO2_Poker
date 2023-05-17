import random

class Baralho:
    def __init__(self):
        self.baralho = []
        simb = ['♠', '♣', '♥', '♦']
        valor = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        
        for a in simb:
            for b in valor:
                self.baralho.append(b+a)
    
    def embaralhar(self):
        random.shuffle(self.baralho)

class Partida:
    def __init__(self):
        self.total = int(input('\nDigite a quantidade de jogadores: '))
        while not (self.total > 0):
            print('\nValor inválido! Digite novamente!')
            self.total = int(input('Digite a quantidade de jogadores: '))
        self.deck = Baralho()
        self.cartas = []
   
        if (52-self.total) >= 0 :
            for i in range(self.total):
                self.cartas.append(i)
                self.cartas[i] = []
        else:
            print('\nQuantidade insuficiente de cartas!')
    
    def distribuir(self):
        c = 0
        d = 52 - (52 % self.total)
        
        while (c < d):
            for index, value in enumerate(self.cartas):
                self.cartas[index].append(self.deck.baralho[c])
                c += 1
            
        for e in range(d, 52):
            self.cartas[e-d].append(self.deck.baralho[e])
    
    def mostrar(self):
        for pos, val in enumerate(self.cartas):
            print('\nCartas do {}º jogador: {}'.format((pos + 1), val))