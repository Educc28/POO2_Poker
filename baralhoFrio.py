from baralho import Baralho
from carta import Carta


#Classe responsável por criar o baralho
class BaralhoFrio(Baralho):
    def __init__(self):
        self.cartas = []
        naipes = {"Copas": "♡", "Espadas": "♠", "Ouros": "♢", "Paus": "♣"}
        valores = {"Dois": 2,
                   "Três": 3,
                   "Quatro": 4,
                   "Cinco": 5,
                   "Seis": 6,
                   "Sete": 7,
                   "Oito": 8,
                   "Nove": 9,
                   "Dez": 10,
                   "J": 11,
                   "Q": 12,
                   "K": 13,
                   "A": 14}
        for nome in valores:
            for naipe in naipes:
                simboloIcone = naipes[naipe]
                if valores[nome] < 11:
                    simbolo = str(valores[nome])+simboloIcone
                else:
                    simbolo = nome + simboloIcone
                self.cartas.append(Carta(nome, valores[nome], naipe, simbolo))
