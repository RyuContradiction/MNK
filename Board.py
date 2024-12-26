import pygame
import sys
import numpy as np




class Baord:
    
    def __init__(self, m: int, n: int, k: int):
        self.m: int = m
        self.n: int = n
        self.k: int = k
        self.array: np.array = np.array((m, n), dtype=int)
        self.board = [[" " for _ in range(self.m)] for _ in range(self.n)]
        
      

    

    def display(self):
        for row in self.board:
            print("|".join(row))
            print("-" * (2*self.n - 1))





#Gewinnbedingung nochmal durchgehen 
    def has_won(self, player):
        self.player = player
        #Überprüft Zeilen
        for row in range(self.m):
            for col in range(self.n - self.k + 1):
                if all(self.array[row][col + i] == player.player_number for i in range(self.k)):
                    return player.player_number
                

        #Überprüft Spalten
        for col in range(self.n):
            for row in range(self.m):
                if all(self.array[row + i][col] == player.player_number for i in range(self.k)):
                    return player.player_number

        #Überprüfen der Diagonale
        for diag in range(self.n * - 1, self.n): #
          for i in range(np.diag(self.array, k = diag)):#gibt eine Liste raus
              if np.diag(self.board, k=diag) >= self.k:
                  if all(np.diag(self.array, k= diag)[i + j] == player.player_number for j in range(self.k) if i + j + self.k <= len(np.diag(self.array, k= diag))):
                      return player.player_number

        #Überprüft ein Unentschieden
        if not np.argwhere(self.board == 0):
            return 0

        """for row in range(self.m):
            for col in range(self.n):
                if all(self.array[np.diag] == player.player_number for i in range(self.k)):
                    return 0
        return False"""

        #Überprüft ob alle Eingänge belegt sind
    def is_full(self):
        if all(self.board[row][col] != " " for row in range(self.m) for col in range(self.n)):
            return "Die sind alle belegt"
    
        

      
b = Baord(5,5,3)
b.display()
b.is_full()
b.draw()
b.draw_stones()
pygame.display.update()

# if __name__ == '__main__':
#     x = np.arange(25).reshape((5,5))
#     print(x)
#     print(np.diag(x, k=0))
#     print(np.diag(x, k=-1))

