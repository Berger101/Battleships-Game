from random import choice, randint

class Player:
    """
    Main Player class. Displaying the board and place ships on the board,
    """
    def __init__(self, name):
        """Initialize the board with the given size."""
        self.name = name
        self.board = [["." for _ in range(10)] for _ in range(10)]
        self.ships = {"carrier": 5, "battleship": 4, "cruiser": 3, "submarine": 3, "destroyer": 2}

    def place_ships(self):
        for ship, size in self.ships.items():
            self.place_ship(ship, size)

    def place_ship(self, ship, size):
        """Randomly place a ship of the given size on the board."""
        while True:
            orientation = choice(["horizontal", "vertical"])
            if orientation == "horizontal":
                row = randint(0, 9)
                col = randint(0, 10 - size)
                if all(self.board[row][col + i] == "." for i in range(size)):
                    for i in range(size):
                        self.board[row][col + i] = ship[0]
                    break
            else:
                row = randint(0, 10 - size)
                col = randint(0, 9)
                if all(self.board[row + i][col] == "." for i in range(size)):
                    for i in range(size):
                        self.board[row + i][col] = ship[0]
                    break

    def display_board(self):
        """Print the board with numbers indicating the indexes"""
        print(f"\n{self.name}'s Board:")
        print("  0 1 2 3 4 5 6 7 8 9")
        for i, row in enumerate(self.board):
            print(f"{i} {' '.join(row)}")

    def check_shot(self, board, row, col):
        pass

def play_game():
  player = Player("Player")
  player.place_ships()

  # Display the initial board
  player.display_board()

# Checks whether the Python script is being run as the main program or if it is being imported as a module into another script.
if __name__ == "__main__":
    play_game()