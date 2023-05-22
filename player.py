#Classe que representa todos os jogadores, suas fichas e suas cartas
class Player(object):
    def __init__(self):
        self.cartas = []
        self.fichas = 1000

#Método que adiciona cartas a mão do jogador
    def addCarta(self, carta):
        self.cartas.append(carta)
