import random

class Baralho(object):
    #shuffle: it randomizes the order of items in a list, we call it a randomizes the elements of a list in place
  def shuffle(self, times=1 ):
    random.shuffle(self.cartas)
    #This is a convenience alias to resample(*arrays, replace=False) to do random permutations of the collections.
    print("Deck Shuffled")

  def deal(self):
    return self.cartas.pop(0)
    #The pop() method removes the item at the given index from the list and returns the removed item.
    #pop utilizei para pegar a última carta do deck