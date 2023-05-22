from baralhoFrio import BaralhoFrio
from player import Player
from pokerScorer import PokerScorer
from mesa import Mesa
import sys

# Para se iniciar o Jogo, precisa utilizar no seu emulador o interpreterVideoPoker()

def interpreterVideoPoker():
    allPoints = []
    num_player = 0
    pot = 0
    while num_player <= 0 or num_player > 23:
        num_player = int(input("Numero de jogadores: "))
        if num_player <= 0 or num_player > 23:
            print("Numero inválido, tente novamente.")
    
    player = [Player() for i in range(0, num_player)]
    print(player)

    # player = Player() 
    mesa = Mesa()

    end = False
    while not end:
        # utilizado para assim que iniciar o jogo, voce recebe um deck, e ele recebe uma misturada.
        # Hand Loop
        baralho = BaralhoFrio()
        baralho.shuffle()

        # Deal Out
        # para entregar ao jogador 5 cartas
        for everyPlayer in range(0, num_player):
            player[everyPlayer].addCarta(baralho.deal())
            player[everyPlayer].addCarta(baralho.deal())


          # para carta nas mãos deste jogador para este jogador ele verá suas cartas
          # Make them visible
        # for carta in player.cartas:
        #     carta.showing = True
        # for carta in mesa.cartas:
        #     carta.showing = True

        for everyPlayer in range(0, num_player):
            print(player[everyPlayer].cartas)

        # validInput = False
        # while not validInput:

        while len(mesa.cartas) < 5:
            for everyPlayer in range(0, num_player):
                fichasApostadas = int(input((f"Quantas fichas você quer apostar jogador{everyPlayer + 1}: ")))
                pot = pot + fichasApostadas
                player[everyPlayer].fichas = player[everyPlayer].fichas - fichasApostadas

            for i in range(3):
                mesa.addCarta(baralho.deal())
            for carta in mesa.cartas:
                carta.showing = True
            print(f'Mesa: {mesa.cartas}')

            for everyPlayer in range(0, num_player):
                fichasApostadas = int(input((f"Quantas fichas você quer apostar jogador{everyPlayer + 1}: ")))
                pot = pot + fichasApostadas
                player[everyPlayer].fichas = player[everyPlayer].fichas - fichasApostadas

            for i in range(1):
                mesa.addCarta(baralho.deal())
            for carta in mesa.cartas:
                carta.showing = True
            print(f'Mesa: {mesa.cartas}')


            for everyPlayer in range(0, num_player):
                fichasApostadas = int(input((f"Quantas fichas você quer apostar jogador{everyPlayer + 1}: ")))
                pot = pot + fichasApostadas
                player[everyPlayer].fichas = player[everyPlayer].fichas - fichasApostadas

            for i in range(1):
                mesa.addCarta(baralho.deal())
            for carta in mesa.cartas:
                carta.showing = True
            print(f'Mesa: {mesa.cartas}')

            for everyPlayer in range(0, num_player):
                fichasApostadas = int(input((f"Quantas fichas você quer apostar jogador{everyPlayer + 1}: ")))
                pot = pot + fichasApostadas
                player[everyPlayer].fichas = player[everyPlayer].fichas - fichasApostadas


        for everyPlayer in range(0, num_player):
            points = Score(player[everyPlayer], mesa)
            allPoints.append(points)
            # print(allPoints)
        maiorPontos = max(allPoints)
        vencedores = [i for i, j in enumerate(allPoints) if j == maiorPontos]

        if len(vencedores) == 1:
            print(f'Jogador {vencedores[0] + 1} venceu a rodada e recebe {pot} fichas')

        else:
            for i in vencedores:
                print(f'Jogador {vencedores[i] + 1}')
            print(f"Empataram e recebem {pot/len(vencedores)} fichas")

        end = True

# Score
# Seu cálculo é feito a partir dos pontos que você ganha com cada poder da mão.


def Score(player, mesa):
    for carta in mesa.cartas:
        player.cartas.append(carta)

    score = PokerScorer(player.cartas)
    four = score.fourKind()
    flush = score.flush()
    straight = score.straight()
    highestCountFunction = score.highestCount()
    highestCount = highestCountFunction[0]
    highestCombination = highestCountFunction[1]
    pairs = score.pairs()
    highcard = score.highCarta()


    # Royal flush
    if straight and flush and straight == 14:
        print("Royal Flush!!!")
        points = 10000
        return points

    # Straight flush
    elif straight and flush:
        print("Straight Flush!")
        points = 1500 + straight
        return points

    # 4 of a kind
    elif four:
        print("Four of a kind!")
        points = 1000 + four
        return points

    # Full House
    elif score.fullHouse():
        print("Full House!")
        points = 500
        return points

    # Flush
    elif flush:
        print("Flush!")
        points = 200
        return points

    # Straight
    elif straight:
        print("Straight!")
        points = straight + 100
        return points

    # 3 of a kind
    elif highestCount == 3:
        print("Three of a Kind!")
        points = highestCombination + 50
        return points
    
    # 2 pair
    elif len(pairs) >= 2:
        print("Two Pairs!")
        points = max(pairs) + 30
        points += min(pairs)
        return points

    # Jacks or better
    elif pairs:
        print("Pair")
        points = max(pairs) + 15
        return points
    else:
        print("High Card")
        points = 0
        points = points + highcard.valor
        return points


interpreterVideoPoker()
