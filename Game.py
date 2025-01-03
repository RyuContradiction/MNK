import numpy
from Board import Board
from Player import Player

class Game:
    def __init__(self, m: int, n: int, k: int):
        self.m: int = m
        self.n: int = n
        self.k: int = k
        self._board: Board = Board(self.m, self.n, self.k)
        self._player1: Player
        self._player2: Player

    def start(self) -> None:
        self._board.display()

        gewonnen: int  = self._board.has_won()
        pass

    def game_loop(self) -> None:
        pass


if __name__ == '__main__':
    game = Game(mnk=(4, 5, 4))