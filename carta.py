#Classe que representa todas as cartas do jogo
class Carta(object):
    def __init__(self, nome, valor, naipe, simbolo):
        self.nome = nome
        self.valor = valor
        self.naipe = naipe
        self.simbolo = simbolo
        self.mostrar = True

#Retorna o valor da carta se mostrar for True
    def __repr__(self):
        if self.mostrar:
            return self.simbolo
        else:
            return "Carta"
