class PokerScorer(object):
    def __init__(self, cartas):
        # Number of cartas
        if not len(cartas) == 7:
            return "Error: Wrong number of cards"
        self.cartas = cartas
# Mãos de poker: https://www.cartaplayer.com/rules-of-poker/hand-rankings
# Flush são 5 cartas do mesmo naipe

    def flush(self):
        copasCount = 0
        espadasCount = 0
        ourosCount = 0
        pausCount = 0

        naipes = [carta.naipe for carta in self.cartas]
        # naipes = ['Paus', 'Paus', 'Paus',
        #           'Paus', 'Paus', 'Espadas', 'Ouros']
        print(naipes)
        for naipe in naipes:
            if naipe == "Copas":
                copasCount = copasCount + 1

            elif naipe == "Espadas":
                espadasCount = espadasCount + 1

            elif naipe == "Ouros":
                ourosCount = ourosCount + 1

            elif naipe == "Paus":
                pausCount = pausCount + 1

        if copasCount >= 5 or espadasCount >= 5 or ourosCount >= 5 or pausCount >= 5:
            return True
        else:
            return False


# 5 Valores seguidos, utilizado .sort, e um set para validação


    def straight(self):
        valores = [carta.valor for carta in self.cartas]
        valores = list(set(valores))
        # print(valores)
        # valores = [2, 3, 10, 11, 12, 13, 14]
        # print(valores)

        if len(valores) < 5:
            return False
# Como o As pode ser tanto como o numero 1 inteiro tivemos que fazer esta condição.

        elif valores[0] == 2 and valores[1] == 3 and valores[2] == 4 and valores[3] == 5 and valores[4] == 14:
            return 5
        elif len(valores) >= 6 and valores[0] == 2 and valores[1] == 3 and valores[2] == 4 and valores[3] == 5 and valores[5] == 14:
            return 5
        elif len(valores) == 7 and valores[0] == 2 and valores[1] == 3 and valores[2] == 4 and valores[3] == 5 and valores[6] == 14:
            return 5

        else:
            if len(valores) == 7 and valores[2] + 4 == valores[3] + 3 == valores[4] + 2 == valores[5] + 1 == valores[6]:
                return valores[6]
            elif len(valores) >= 6 and valores[1] + 4 == valores[2] + 3 == valores[3] + 2 == valores[4] + 1 == valores[5]:
                return valores[5]
            elif valores[0] + 4 == valores[1] + 3 == valores[2] + 2 == valores[3] + 1 == valores[4]:
                return valores[4]
            else:
                return False

# Definição das cartas altas.
# O valor é definiddo por uma comparação dos valores respectivos aquele dicionário.

    def highCarta(self):
        valores = [carta.valor for carta in self.cartas]
        highcarta = None
        for carta in self.cartas:
            if highcarta is None:
                highcarta = carta
            elif highcarta.valor < carta.valor:
                highcarta = carta

        return highcarta

    def highestCount(self):
        count = 0
        highestCombination = 0
        valores = [carta.valor for carta in self.cartas]
        for valor in valores:
            if valores.count(valor) > count:
                count = valores.count(valor)
                highestCombination = valor
        return [count, highestCombination]
# Definição dos pares, utilizado uma lista para comparar o mesmo valor da carta.

    def pairs(self):
        pairs = []
        valores = [carta.valor for carta in self.cartas]
        for valor in valores:
            if valores.count(valor) == 2 and valor not in pairs:
                pairs.append(valor)
        return pairs
# Definição para definir se há uma quadrupla, ou seja, comparando o valor se há repetidamente 4 vezes.

    def fourKind(self):
        valores = [carta.valor for carta in self.cartas]
        for valor in valores:
            if valores.count(valor) == 4:
                return True

# Uma full house avalia se há 3 cartas iguais e 2 cartas iguais
    def fullHouse(self):
        two = False
        three = False

        valores = [carta.valor for carta in self.cartas]
        if valores.count(valores) == 2:
            two = True
        elif valores.count(valores) == 3:
            three = True

        if two and three:
            return True
        else:
            return False
