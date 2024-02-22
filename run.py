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

class Player:
    def take_shot(self):
        while True:
            try:
                row = int(input("Enter the row (0-9): "))
                col = int(input("Enter the column (0-9): "))
                if 0 <= row <= 9 and 0 <= col <= 9:
                    return row, col
                else:
                    print("Invalid input. Row and column must be between 0 and 9.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def check_shot(self, board, row, col):
        # Code to check if the shot hits or misses goes here
        pass

board = Board(10)
board.place_ship(3)
board.print_board()

player = Player()
shot_row, shot_col = player.take_shot()
