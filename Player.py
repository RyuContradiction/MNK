

class Player:

    def __init__(self, name: str, player_number: int):
        self._name:str = name
        self._player_number:int = player_number

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def player_number(self):
        return self._player_number

    @player_number.setter
    def player_number(self, value):
        self._player_number = value


    def make_move(self, board):
        while True:
            row = int(input(f"{self.name}, enter the row number: "))
            col = int(input(f"{self.name}, enter the column number: "))
            try:
                board.array[row,col]
            except IndexError:
                print("Dieses Feld gibt es nicht")
                continue
            if board.array[row,col] == 1 or board.array[row,col] == 2:
                print("Dieses Feld ist besetzt , bitte wählen sie ein nicht belegtes Feld")
            else:
                break
        return (row, col)