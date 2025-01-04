class Player:
    def init(self, name: str, player_number: int):
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


    def make_move(self, board: Board):
        while True:
            row = int(input(f"{self.name}, enter the row number: "))
            col = int(input(f"{self.name}, enter the column number: "))
            if Board.array[row,col] == 1 or Board.array[row,col] == 2:
                raise ValueError("Dieses Feld ist besetzt , bitte wählen sie ein nicht belegtes Feld")
            if Board.array.shape[0] <= row or Board.array.shape[1] <= col:
                raise ValueError("Dieses Feld gibt es nicht")
            return (row, col)