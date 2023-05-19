from baralhoFrio import BaralhoFrio
from player import Player
from pokerScorer import PokerScorer

#Para se iniciar o Jogo, precisa utilizar no seu emulador o interpreterVideoPoker()
def interpreterVideoPoker():
  player = Player()

  # Intial Amount
  points = 100

  # Cost per hand
  handCost = 10

  end = False
  while not end:
    print( "You have {0} points".format(points) )
    print()

    points-=10

    #utilizado para assim que iniciar o jogo, voce recebe um deck, e ele recebe uma misturada.
    #Hand Loop
    baralho = BaralhoFrio()
    baralho.shuffle()

    # Deal Out
    #para entregar ao jogador 5 cartas
    for i in range(5):
      player.addCard(baralho.deal())

    #para carta nas mãos deste jogador para este jogador ele verá suas cartas
    # Make them visible
    for card in player.cards:
      card.showing = True
    print(player.cards)

    validInput = False
    while not validInput:
      print("Quais Cartas você quer descartar? ( Ex. 1, 2, 3 )")
      print("Aperte Enter para segurar e escreva exit para sair do jogo ")
      inputStr = input()

      if inputStr == "exit":
        end=True
        break

        #um try para começo da verificação

      try:
        #Transformamos em inteiros, depois dividimos cada número pela virgula.
        inputList = [int(inp.strip()) for inp in inputStr.split(",") if inp]
        #validamos caso ele escreva corretamente
        for inp in inputList:
          if inp > 6:
            continue 
          if inp < 1:
            continue 
        #nesta lista, nós entregamos novas cartas e as mostramos para as pessoas
        for inp in inputList:
          player.cards[inp-1] = baralho.deal()
          player.cards[inp-1].showing = True

        validInput = True
      except:
        #caso o usuário erre tudo
        print("Você colocou um número errado")

    print(player.cards)
    #Score
    #Seu cálculo é feito a partir dos pontos que você ganha com cada poder da mão.
    score = PokerScorer(player.cards)
    straight = score.straight()
    flush = score.flush()
    highestCount = score.highestCount()
    pairs = score.pairs()

    # Royal flush
    if straight and flush and straight == 14:
      print("Royal Flush!!!")
      print("+2000")
      points += 2000

    # Straight flush
    elif straight and flush:
      print("Straight Flush!")
      print("+250")
      points += 250

    # 4 of a kind
    elif score.fourKind():
      print("Four of a kind!")
      print("+125")
      points += 125

    # Full House
    elif score.fullHouse():
      print("Full House!")
      print("+40")
      points += 40

    # Flush
    elif flush:
      print("Flush!")
      print("+25")
      points += 25

    # Straight
    elif straight:
      print("Straight!")
      print("+20")
      points += 20

    # 3 of a kind
    elif highestCount == 3:
      print("Three of a Kind!")
      print("+15")
      points += 15

    # 2 pair
    elif len(pairs) == 2:
      print("Two Pairs!")
      print("+10")
      points += 10

    # Jacks or better
    elif pairs and pairs[0] > 10:
      print ("Jacks or Better!")
      print("+5")
      points += 5

    player.cards=[]

interpreterVideoPoker()
