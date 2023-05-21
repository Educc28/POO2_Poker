# Init - setting up the basic values of each card, value,
# suit, name, showing: que tem a intenção de mostrar para o usuário quando solicitado a sua carta
class Carta(object):
    def __init__(self, nome, valor, naipe, simbolo):
        self.nome = nome
        self.valor = valor
        self.naipe = naipe
        self.simbolo = simbolo
        self.showing = False

# def é utilizado para representar o objeto. Serve para mostrar customizar o que retorna - para saber o status de uma ação.

# se a funcao showing for chamada a pessoa vera as cartas na sua mao
# Caso não, ela só receberá a mensagem de "carta" que é como se fosse a carta virada
# retorna os valores da sua carta.
    def __repr__(self):
        if self.showing:
            return self.simbolo
        else:
            return "Carta"
