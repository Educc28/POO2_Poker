class Mesa(object):
    def __init__(self):
        self.cartas = []
# Uma lista para darmos ao player o seu deck.

    def cartaCount(self):
        return len(self.cartas)
# Um contador das suas cartas

    def addCarta(self, carta):
        self.cartas.append(carta)
# uma função de dar a carta ao jogador
