import numpy
from Board import Board
from Player import Player
import keyboard  # using module keyboard
import time


class Game:
    def __init__(self, m: int = 5, n: int = 5, k: int= 4):
        self._m: int = m
        self._n: int = n
        self._k: int = k
        self._board: Board = Board(self._m, self._n, self._k)
        self._player1: Player = Player(name= "1",player_number = 1)
        self._player2: Player = Player(name= "1",player_number = 2)
        self._indexierung: int = 0

    def start(self) -> None:
        print('Dieses Spiel heisst MNK.\nEin Spiel bei dem in einem Feld, welches M Anzahl Zeilen und N Anzahl Spalten besteht,\nK Anzahl an Markierungen gesetz werden soll, welche nebeneinander stehen muessen, um zu gewinnen. ')
        time.sleep(10)
        print(f'Die Default werte sind: M = {self._m}, N = {self._n}, K = {self._k}.\nMöchten Sie diese ändern?')
        time.sleep(4)
        decision: str = input('enter y/n to decide:')
        if decision == 'y':
            while True:
                try:
                    self._m = int(input('Welcher int Wert soll M haben?: '))
                    self._n = int(input('Welcher int Wert soll N haben?: '))
                    self._k = int(input('Welcher int Wert soll K haben?: '))
                    break
                except ValueError:
                    print('Die Eingabe muss eine ganze Zahl sein! Versuchen Sie es erneut.')
        self._board.display()
        print('Die zwei Spieler setzen abwechselnd Markierungen.')
        time.sleep(4)
        print('Um eine Markierungen zu setzen, werden die jeweilige indexe im Feld benötigt.')
        time.sleep(4)
        print('Um nun nicht in Verwirrung zu gelangen, ob z.b der erste eintrag den index 0:0 oder 1:1,')
        print('wird gebeten sich fuer eins zu entscheiden.')
        time.sleep(4)
        decision: str = input('Normale Array indexierung beibehalten? y/n')
        if decision == 'y':
            self._indexierung = 1
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
            self._board.array[move_player1[0] + self._indexierung, move_player1[1] + self._indexierung] = self._player1.player_number
            gewonnen = self._board.has_won(self._player1)
            print(self._board.array)
            if gewonnen == self._player1.player_number:
                print('Player 1 hat gewonnen!')
                break
            elif gewonnen == 0:
                print('Ein Unentschieden, da alle Felder belegt sind')
                break
            move_player2 = self._player2.make_move(self._board)
            self._board.array[move_player2[0] + self._indexierung, move_player2[1] + self._indexierung] = self._player2.player_number
            gewonnen = self._board.has_won(self._player2)
            print(self._board.array)
            if gewonnen == self._player2.player_number:
                print('Player 2 hat gewonnen!')
                break
            elif gewonnen == 0:
                print('Ein Unentschieden, da alle Felder belegt sind')
                break

   





if __name__ == '__main__':
    game: Game = Game()
    game.start()
    game.game_loop()