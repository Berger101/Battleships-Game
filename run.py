from random import randint

class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [['O' for _ in range(size)] for _ in range(size)]

    def print_board(self):
        for row in self.grid:
            print(" ".join(row))

    def place_ship(self, ship_size):
      
        pass

board = Board(10)
board.place_ship(3)
board.print_board()