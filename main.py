from baralhoFrio import BaralhoFrio
from player import Player
from mesa import Mesa
from pontuacao import Pontuacao

#Função que faz todo o jogo, chamando outras funções e utilizando de classes quando necessário
def Jogo():
    allPoints = []
    num_player = 0
    pot = 0

#Pede um input para saber quantos jogadores jogarão
    while num_player <= 0 or num_player > 23:
        num_player = int(input("Numero de jogadores: "))
        if num_player <= 0 or num_player > 23:
            print("Numero inválido, tente novamente.")
    
#Cria a quantidade de jogadores segundo o input do usuário
    player = [Player() for i in range(0, num_player)]

#Cria a mesa
    mesa = Mesa()


#Cria o baralho e o embaralha
    baralho = BaralhoFrio()
    baralho.shuffle()


#Entrega duas cartas para cada jogador
    for everyPlayer in range(0, num_player):
        player[everyPlayer].addCarta(baralho.deal())
        player[everyPlayer].addCarta(baralho.deal())




#Imprime a mão dos jogadores
    for everyPlayer in range(0, num_player):
        print(player[everyPlayer].cartas)

#Pergunta para cada jogador quantas fichas ele quer apostar e adiciona ao pot
    for everyPlayer in range(0, num_player):
        fichasApostadas = int(input((f"Quantas fichas você quer apostar jogador{everyPlayer + 1}: ")))
        pot = pot + fichasApostadas
        player[everyPlayer].fichas = player[everyPlayer].fichas - fichasApostadas

#Adiciona cartas a mesa e imprime todas as cartas da mesa
    for i in range(3):
        mesa.addCarta(baralho.deal())
    print(f'Mesa: {mesa.cartas}')

#Pergunta para cada jogador quantas fichas ele quer apostar e adiciona ao pot
    for everyPlayer in range(0, num_player):
        fichasApostadas = int(input((f"Quantas fichas você quer apostar jogador{everyPlayer + 1}: ")))
        pot = pot + fichasApostadas
        player[everyPlayer].fichas = player[everyPlayer].fichas - fichasApostadas

#Adiciona cartas a mesa e imprime todas as cartas da mesa
    for i in range(1):
        mesa.addCarta(baralho.deal())
    print(f'Mesa: {mesa.cartas}')

#Pergunta para cada jogador quantas fichas ele quer apostar e adiciona ao pot
    for everyPlayer in range(0, num_player):
        fichasApostadas = int(input((f"Quantas fichas você quer apostar jogador{everyPlayer + 1}: ")))
        pot = pot + fichasApostadas
        player[everyPlayer].fichas = player[everyPlayer].fichas - fichasApostadas

#Adiciona cartas a mesa e imprime todas as cartas da mesa
    for i in range(1):
        mesa.addCarta(baralho.deal())
    print(f'Mesa: {mesa.cartas}')

#Pergunta para cada jogador quantas fichas ele quer apostar e adiciona ao pot
    for everyPlayer in range(0, num_player):
        fichasApostadas = int(input((f"Quantas fichas você quer apostar jogador{everyPlayer + 1}: ")))
        pot = pot + fichasApostadas
        player[everyPlayer].fichas = player[everyPlayer].fichas - fichasApostadas


#Para cada jogador, vê a mão que ele possui e adiciona a pontuação relativa para cada mão em um array
    for everyPlayer in range(0, num_player):
        points = Pontuacao(player[everyPlayer], mesa)
        allPoints.append(points)

#Vê qual jogador venceu ou se há multiplos vencedores
    maiorPontos = max(allPoints)
    vencedores = [i for i, j in enumerate(allPoints) if j == maiorPontos]

#Confere se um jogador venceu sozinho ou se houve um empate, também mostra quantas fichas eles ganharam
    if len(vencedores) == 1:
        print(f'Jogador {vencedores[0] + 1} venceu a rodada e recebe {pot} fichas')

    else:
        for i in vencedores:
            print(f'Jogador {vencedores[i] + 1}')
        print(f"Empataram e recebem {pot/len(vencedores)} fichas cada")

#Inicia o Jogo
Jogo()
