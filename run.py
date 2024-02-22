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

    def take_turn(self, other_player):
        while True:
            try:
                guess_row = int(input("Enter guess row (0-9): "))
                guess_col = int(input("Enter guess column (0-9): "))
                if 0 <= guess_row <= 9 and 0 <= guess_col <= 9 and other_player.board[guess_row][guess_col] != "X":
                    return guess_row, guess_col
                else:
                    print("Invalid guess. Try again.")
            except ValueError:
                print("Invalid input. Enter integers only.")

    def mark_hit(self, row, col, other_player):
        if other_player.board[row][col] != ".":
            print("Hit!")
            other_player.board[row][col] = "X"
        else:
            print("Miss!")
    

class Computer(Player):
    """
    Computer class so two players may play the game.
    """
    def __init__(self):
        super().__init__("Computer")

    def take_turn(self, other_player):
        guess_row = randint(0, 9)
        guess_col = randint(0, 9)
        return guess_row, guess_col


def play_game():
  player = Player("Player")
  computer = Computer()

  player.place_ships()
  computer.place_ships()

  while True:
      player.display_board()
      computer.display_board()

      # Player's turn
      player_guess_row, player_guess_col = player.take_turn(computer)
      player.mark_hit(player_guess_row, player_guess_col, computer)
      if player.check_win(computer):
          print("Congratulations! You sank all computer's ships. You win!")
          break

      # Computer's turn
      computer_guess_row, computer_guess_col = computer.take_turn(player)
      computer.mark_hit(computer_guess_row, computer_guess_col, player)
      if computer.check_win(player):
          print("Oh no! Computer sank all your ships. You lose!")
          break

# Checks whether the Python script is being run as the main program or if it is being imported as a module into another script.
if __name__ == "__main__":
    play_game()