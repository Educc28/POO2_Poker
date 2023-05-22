from maos import Maos

#Função referente a pontuação do jogador, retorna a pontuação mais alta e imprime qual mão ele tem
def Pontuacao(player, mesa):
    for carta in mesa.cartas:
        player.cartas.append(carta)

    pontos = Maos(player.cartas)
    four = pontos.four()
    flush = pontos.flush()
    sequencia = pontos.sequencia()
    maiorRepeticaoFunction = pontos.maiorRepeticao()
    maiorRepeticao = maiorRepeticaoFunction[0]
    maiorCombinacao = maiorRepeticaoFunction[1]
    pares = pontos.pares()
    cartaAlta = pontos.cartaAlta()

    #Confere se é um Royal flush
    if sequencia and flush and sequencia == 14:
        print("Royal Flush!")
        points = 10000
        return points

    #Confere se é um straight flush
    elif sequencia and flush:
        print("Straight Flush!")
        points = 1500 + sequencia
        return points

    #Confere se é um four
    elif four:
        print("Four!")
        points = 1000 + four
        return points

    #Confere se é um Full House
    elif pontos.fullHouse():
        print("Full House!")
        points = 500
        return points

    #Confere se é um Flush
    elif flush:
        print("Flush!")
        points = 200
        return points

    #Confere se é uma Sequencia
    elif sequencia:
        print("Sequencia!")
        points = sequencia + 100
        return points

    #Confere se é uma Trinca
    elif maiorRepeticao == 3:
        print("Trinca!")
        points = maiorCombinacao + 50
        return points
    
    #Confere se são 2 pares
    elif len(pares) >= 2:
        print("Dois pares!")
        points = max(pares) + 30
        points += min(pares)
        return points

    #Confere se é um Par
    elif pares:
        print("Par!")
        points = max(pares) + 15
        return points

    #Caso não for uma combinação, retorna a carta mais alta
    else:
        print("Carta Alta")
        points = 0
        points = points + cartaAlta.valor
        return points
