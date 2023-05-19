class PokerScorer(object):
  def __init__(self, cartas):
    # Number of cartas
    if not len(cartas) == 5:
      return "Error: Wrong number of cartas"
    self.cartas = cartas
#Mãos de poker: https://www.cartaplayer.com/rules-of-poker/hand-rankings
#Flush são 5 cartas do mesmo naipe
  def flush(self):
    naipes = [carta.naipe for carta in self.cartas]
    if len( set(naipes) ) == 1:
      return True
    return False
#5 Valores seguidos, utilizado .sort, e um set para validação
  def straight(self):
    valores = [carta.valor for carta in self.cartas]
    valores.sort()

    if not len( set(valores)) == 5:
      return False 
#Como o As pode ser tanto como o numero 1 inteiro tivemos que fazer esta condição.
    if valores[4] == 14 and valores[0] == 2 and valores[1] == 3 and valores[2] == 4 and valores[3] == 5:
      return 5

    else:
      if not valores[0] + 1 == valores[1]: return False 
      if not valores[1] + 1 == valores[2]: return False
      if not valores[2] + 1 == valores[3]: return False
      if not valores[3] + 1 == valores[4]: return False

    return valores[4]
#Definição das cartas altas.
#O valor é definiddo por uma comparação dos valores respectivos aquele dicionário.
  def highCarta(self):
    valores = [carta.valor for carta in self.cartas]
    highcarta = None
    for carta in self.cartas:
      if highcarta is None:
        highcarta = carta
      elif highcarta.valor < carta.valor: 
        highcarta=carta

    return highcarta

  def highestCount(self):
    count = 0
    valores = [carta.valor for carta in self.cartas]
    for valor in valores:
      if valores.count(valor) > count:
        count = valores.count(valor)

    return count
#Definição dos pares, utilizado uma lista para comparar o mesmo valor da carta. 
  def pairs(self):
    pairs = []
    valores = [carta.valor for carta in self.cartas]
    for valor in valores:
      if valores.count(valor) == 2 and valor not in pairs:
        pairs.append(valor)

    return pairs
#Definição para definir se há uma quadrupla, ou seja, comparando o valor se há repetidamente 4 vezes.
  def fourKind(self):
    valores = [carta.valor for carta in self.cartas]
    for valor in valores:
      if valores.count(valor) == 4:
        return True

#Uma full house avalia se há 3 cartas iguais e 2 cartas iguais
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

    return False