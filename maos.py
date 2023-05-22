#Classe que representa as mãos do poker (combinações)
class Maos(object):
    def __init__(self, cartas):
        self.cartas = cartas

#Confere se a mão do jogador faz um flush
    def flush(self):
        copasCount = 0
        espadasCount = 0
        ourosCount = 0
        pausCount = 0

        naipes = [carta.naipe for carta in self.cartas]

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


#Confere se a mão do jogador faz uma sequência, retorna falso ou o valor do número mais alto da sequência
    def sequencia(self):
        valores = [carta.valor for carta in self.cartas]
        valores = list(set(valores))

#Confere se a sequência é possível
        if len(valores) < 5:
            return False
        
#Confere se a sequência é de A a 5, retorna 5 se verdadeiro
        elif valores[0] == 2 and valores[1] == 3 and valores[2] == 4 and valores[3] == 5 and valores[4] == 14:
            return 5
        elif len(valores) >= 6 and valores[0] == 2 and valores[1] == 3 and valores[2] == 4 and valores[3] == 5 and valores[5] == 14:
            return 5
        elif len(valores) == 7 and valores[0] == 2 and valores[1] == 3 and valores[2] == 4 and valores[3] == 5 and valores[6] == 14:
            return 5

#Confere as outras sequências, retorna o valor do número mais alto da sequência se verdadeiro, ou falso
        else:
            if len(valores) == 7 and valores[2] + 4 == valores[3] + 3 == valores[4] + 2 == valores[5] + 1 == valores[6]:
                return valores[6]
            elif len(valores) >= 6 and valores[1] + 4 == valores[2] + 3 == valores[3] + 2 == valores[4] + 1 == valores[5]:
                return valores[5]
            elif valores[0] + 4 == valores[1] + 3 == valores[2] + 2 == valores[3] + 1 == valores[4]:
                return valores[4]
            else:
                return False


#Retorna o valor da carta mais alta da mão do jogador
    def cartaAlta(self):
        valores = [carta.valor for carta in self.cartas]
        cartaAlta = None
        for carta in self.cartas:
            if cartaAlta is None:
                cartaAlta = carta
            elif cartaAlta.valor < carta.valor:
                cartaAlta = carta
        return cartaAlta


#Confere se a maior quantidade de vezes que uma carta se repete, retorna a quantidade de vezes e o valor da carta
    def maiorRepeticao(self):
        count = 0
        maiorCombinacao = 0
        valores = [carta.valor for carta in self.cartas]
        for valor in valores:
            if valores.count(valor) > count:
                count = valores.count(valor)
                maiorCombinacao = valor
        return [count, maiorCombinacao]
    

#Confere os pares, retorna o valor dos pares
    def pares(self):
        pares = []
        valores = [carta.valor for carta in self.cartas]
        for valor in valores:
            if valores.count(valor) == 2 and valor not in pares:
                pares.append(valor)
        return pares
    

#Confere se a mão do jogador faz um four, retorna o valor da carta ou false
    def four(self):
        valores = [carta.valor for carta in self.cartas]
        for valor in valores:
            if valores.count(valor) == 4:
                return valor

#Confere se o jogador fez um full house, retorna verdadeiro ou falso
    def fullHouse(self):
        two = False
        three = False

        valores = [carta.valor for carta in self.cartas]

        same_cards = sorted([valores.count(a) for a in set(valores)])

        if 2 in same_cards and 3 in same_cards:
            return True
        else:
            return False