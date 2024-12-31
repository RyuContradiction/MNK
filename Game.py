import numpy
import Board

class Game:
    def __init__(self, mnk: tuple[int,int,int]):
        self._mnk: tuple[int,int,int] = mnk
        self._board: Board = Board(self._mnk)
        #self._player1: Player
        #self._player2: Player

    def start(self) -> None:
        self._board.display()
        gewonnen: int  = self._board.has_won()
        pass

    def game_loop(self) -> None:
        pass


if __name__ == '__main__':
    game = Game(mnk=(4, 5, 4))