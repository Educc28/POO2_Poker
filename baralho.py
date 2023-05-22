import random

#Classe que representa o baralho de 52 cartas
class Baralho(object):
  def shuffle(self, times=1): #Função que embaralha o baralho
    random.shuffle(self.cartas)


#Método que deleta e retorna uma carta do baralho
  def deal(self):
    return self.cartas.pop(0)
