class Player:
    def _init_(self, name, player_number):
        self.name = name
        self.player_number = player_number

    def make_move(self, board):
        row = int(input(f"{self.name}, enter the row number: "))
        col = int(input(f"{self.name}, enter the column number: "))
        return (row, col)