#Classe que representa as cartas que estão na mesa, cartas comuns para todos os jogadores
class Mesa(object):
    def __init__(self):
        self.cartas = []


#Método que adiciona uma carta a mesa
    def addCarta(self, carta):
        self.cartas.append(carta)
