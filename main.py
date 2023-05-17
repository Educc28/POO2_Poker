from baralho import Baralho, Partida

while True:

    # Instanciação
    p = Partida()

    # 1º Método
    p.deck.embaralhar()

    # 2º Método
    p.distribuir()

    # 3º Método
    p.mostrar()

    c = str(input('\nDigite "0" para encerrar o programa: '))
    if (c == '0'):
        break

print('\nPrograma Encerrado!')
