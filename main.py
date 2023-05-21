from baralhoFrio import BaralhoFrio
from player import Player
from pokerScorer import PokerScorer
from mesa import Mesa
import sys

# Para se iniciar o Jogo, precisa utilizar no seu emulador o interpreterVideoPoker()


def interpreterVideoPoker():
    player = Player()
    mesa = Mesa()

    end = False

    while not end:
        # utilizado para assim que iniciar o jogo, voce recebe um deck, e ele recebe uma misturada.
        # Hand Loop
        baralho = BaralhoFrio()
        baralho.shuffle()

        # Deal Out
        # para entregar ao jogador 5 cartas
        for i in range(2):
            player.addCarta(baralho.deal())

          # para carta nas mãos deste jogador para este jogador ele verá suas cartas
          # Make them visible
        for carta in player.cartas:
            carta.showing = True
        for carta in mesa.cartas:
            carta.showing = True
        print(player.cartas)

        # validInput = False
        # while not validInput:

        while len(mesa.cartas) < 5:
            print("Digite 1 para ir para a proxima etapa ou 0 para sair: ")
            inputStr = input()

            if inputStr == "1" and len(mesa.cartas) == 0:
                for i in range(3):
                    mesa.addCarta(baralho.deal())
                for carta in mesa.cartas:
                    carta.showing = True
                print(f'Mesa: {mesa.cartas}')

            elif inputStr == "1" and len(mesa.cartas) == 3:
                for i in range(1):
                    mesa.addCarta(baralho.deal())
                for carta in mesa.cartas:
                    carta.showing = True
                print(f'Mesa: {mesa.cartas}')

            elif inputStr == "1" and len(mesa.cartas) == 4:
                for i in range(1):
                    mesa.addCarta(baralho.deal())
                for carta in mesa.cartas:
                    carta.showing = True
                print(f'Mesa: {mesa.cartas}')

            elif inputStr == "0":
                sys.exit()

        for carta in mesa.cartas:
            player.cartas.append(carta)

        print(player.cartas)
        points = Score(player)
        print(points)
        player.cartas = []
        end = True

# Score
# Seu cálculo é feito a partir dos pontos que você ganha com cada poder da mão.


def Score(player):
    score = PokerScorer(player.cartas)
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
        print(points)
        return points

    # Straight flush
    elif straight and flush:
        print("Straight Flush!")
        points = 1500
        print(points)
        return points

    # 4 of a kind
    elif score.fourKind():
        print("Four of a kind!")
        points = 1000
        print(points)
        return points

    # Full House
    elif score.fullHouse():
        print("Full House!")
        points = 500
        print(points)
        return points

    # Flush
    elif flush:
        print("Flush!")
        points = 200
        print(points)
        return points

    # Straight
    elif straight:
        print("Straight!")
        points = straight + 100
        print(points)
        return points

    # 3 of a kind
    elif highestCount == 3:
        print("Three of a Kind!")
        points = highestCombination + 50
        print(points)

    # 2 pair
    elif len(pairs) == 2:
        print("Two Pairs!")
        points = max(pairs) + 30
        points += min(pairs)
        print(points)
        return points

    # Jacks or better
    elif pairs:
        print("Pair")
        points = max(pairs) + 15
        print(points)
        return points
    else:
        print("High Card")
        points = 0
        points = points + highcard.valor
        print(points)
        return points


interpreterVideoPoker()
