import pygame
import sys
import numpy as np
from Player import Player


class Board:
    
    def __init__(self, m: int, n: int, k: int):
        self._m: int = m
        self._n: int = n
        self._k: int = k
        self._array: np.array = np.zeros((m, n))
        self.board = [[" " for _ in range(self._m)] for _ in range(self._n)]
        
      
    @property
    def m(self):
        return self._m

    @m.setter
    def m(self, value: int):
        self._m = value

    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, value: int):
        self._n = value

    @property
    def k(self):
        return self._k

    @k.setter
    def k(self, value: int):
        self._k = value

    @property
    def array(self):
        return self._array

    @array.setter
    def array(self, value: np.ndarray):
        self._array = value
    

    def display(self):
        for row in self.board:
            print("|".join(row))
            print("-" * (2 * self._n - 1))





#Gewinnbedingung nochmal durchgehen 
    def has_won(self, player: Player):
        self.player = player
        #Überprüft Zeilen
        for row in range(self._m):
            for col in range(self._n - self._k + 1):
                if all(self._array[row , col + i] == player.player_number for i in range(self._k)):
                    return player.player_number
                

        #Überprüft Spalten
        for col in range(self._n):
            for row in range(self._m):
                if all(self._array[row + i , col] == player.player_number for i in range(self._k)):
                    return player.player_number

        #Überprüfen der Diagonale
        for diag in range(self._m * - 1, self._n): #
            for i in range(len(np.diag(self._array, k = diag))):#gibt eine Liste raus
                if len(np.diag(self._array, k=diag)) >= self._k:
                    if all(np.diag(self._array, k= diag)[i + j] == player.player_number for j in range(self._k) if
                           i + self._k <= len(np.diag(self._array, k= diag))):
                        return player.player_number

        # Überprüfen der Diagonale
        for diag in range(self._m * - 1, self._n):  #
            for i in range(len(np.diag(np.fliplr(self._array), k=diag))):  # gibt eine Liste raus
                if len(np.diag(np.fliplr(self._array), k=diag)) >= self._k:
                    if all(np.diag(np.fliplr(self._array), k=diag)[i + j] == player.player_number for j in range(self._k) if
                           i + self._k <= len(np.diag(np.fliplr(self._array), k=diag))):
                        return player.player_number

        #Überprüft ein Unentschieden
        if not np.argwhere(self.board == 0):
            return 0

        """for row in range(self._m):
            for col in range(self._n):
                if all(self._array[np.diag] == player.player_number for i in range(self._k)):
                    return 0
        return False"""

        #Überprüft ob alle Eingänge belegt sind
    def is_full(self):
        if all(self.board[row][col] != " " for row in range(self._m) for col in range(self._n)):
            return "Die sind alle belegt"
    
        

      
"""b = Board(5,5,3)
b.display()
b.is_full()
b.draw()
b.draw_stones()
pygame.display.update()"""

# if __name__ == '__main__':
#     x = np.arange(25).reshape((5,5))
#     print(x)
#     print(np.diag(x, _k=0))
#     print(np.diag(x, _k=-1))

