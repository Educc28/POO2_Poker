from baralho import Baralho
from carta import Carta


class BaralhoFrio(Baralho):
    # Esta classe Faz a criação do Deck de Cartas, onde utilizamos 2 dicts para referirmos o primeiro para a sua representação,
    # E o segundo para representar o seu valor, que vai ser útil para podermos avaliar depois quais são as cartas altas e entender
    # toda a lógica do poker
    def __init__(self):
        self.cartas = []
        naipes = {"Copas": "♡", "Espadas": "♠", "Ouros": "♢", "Paus": "♣"}
        valores = {"Two": 2,
                   "Three": 3,
                   "Four": 4,
                   "Five": 5,
                   "Six": 6,
                   "Seven": 7,
                   "Eight": 8,
                   "Nine": 9,
                   "Ten": 10,
                   "Jack": 11,
                   "Queen": 12,
                   "King": 13,
                   "Ace": 14}
# Para cada nome nos valores, para cada simbolo, será atribuido como string o valor concatenado com seu respectivo símbolo
        for nome in valores:
            for naipe in naipes:
                simboloIcone = naipes[naipe]
                if valores[nome] < 11:
                    simbolo = str(valores[nome])+simboloIcone
                else:
                    # Como o deck vai até o 10 e depois começa o Jack, então adicionamos o nome e o símbolo.
                    simbolo = nome[0]+simboloIcone
                self.cartas.append(Carta(nome, valores[nome], naipe, simbolo))

    def __repr__(self):
        return "Standard deck of cartas:{0} remaining".format(len(self.cartas))
# Agora para representar o tanto de cartas que estão restando.
