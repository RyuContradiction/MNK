import numpy
from Board import Board
from Player import Player

class Game:
    def __init__(self, m: int, n: int, k: int):
        self._m: int = m
        self._n: int = n
        self._k: int = k
        self._board: Board = Board(self._m, self._n, self._k)
        self._player1: Player = Player(name= "1",player_number = 1)
        self._player2: Player = Player(name= "1",player_number = 2)

    def start(self) -> None:
        self._board.display()
        self._player1.name = input('Name des Player 1 eingeben:')
        self._player2.name = input('Name des Player 2 eingeben:')
        self._player1.player_number = 1
        self._player2.player_number = 2




    def game_loop(self) -> None:
        print(self._board.array)
        move_player1: tuple[int, int]
        move_player2: tuple[int, int]
        gewonnen: int
        while True:
            move_player1 = self._player1.make_move(self._board)
            print(self._player1.player_number)
            self._board.array[move_player1[0]:move_player1[1]] = self._player1.player_number
            gewonnen = self._board.has_won(self._player1)
            print(self._board.array)
            if gewonnen == self._player1.player_number:
                print('Player 1 hat gewonnen!')
                break
            elif gewonnen == 0:
                print('Ein Unentschieden, da alle Felder belegt sind')
                break
            move_player2 = self._player2.make_move(self._board)
            self._board.array[move_player2[0]:move_player2[1]] = self._player2.player_number
            gewonnen = self._board.has_won(self._player2)
            print(self._board.array)
            if gewonnen == self._player2.player_number:
                print('Player 2 hat gewonnen!')
                break
            elif gewonnen == 0:
                print('Ein Unentschieden, da alle Felder belegt sind')
                break



if __name__ == '__main__':
    game: Game = Game(4, 5, 4)
    game.start()
    game.game_loop()