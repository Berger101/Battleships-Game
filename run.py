from random import choice, randint
from colorama import Fore, Style


class Player:
    """
    Main Player class. Displaying the board and place ships on the board,
    """

    def __init__(self, name):
        """Initialize the board with the given size."""
        self.name = name
        self.board = [["." for R in range(10)] for C in range(10)]
        self.ships = {
            "carrier": 5,
            "battleship": 4,
            "cruiser": 3,
            "submarine": 3,
            "destroyer": 2,
        }

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

    def display_board(self, hide_computer_ships=True):
        """Print the board with numbers indicating the indexes"""
        print(f"\n{self.name}'s Board:")
        print("  0 1 2 3 4 5 6 7 8 9")
        for i, row in enumerate(self.board):
            if hide_computer_ships and self.name == "Computer":
                row_display = [
                    "." if cell != "X" and cell != "M" else cell for cell in row
                ]
            else:
                row_display = row
            print(f"{i} {' '.join(row_display)}")

    def take_turn(self, other_player):
        """
        Take turn method, where the player may enter the row and column to target and error handling for invalid input
        """
        guessed_coordinates = set()  # Set to store previously guessed coordinates
        while True:
            try:
                guess_row = int(input("Enter target row (0-9): "))
                guess_col = int(input("Enter target column (0-9): "))

                if guess_row not in range(0, 10) or guess_col not in range(0, 10):
                    print("Please choose numbers between 0 and 9.")
                elif (guess_row, guess_col) in guessed_coordinates:
                    print("Already targeted. Try again.")
                elif other_player.board[guess_row][guess_col] in ["X", "M"]:
                    # Add guessed coordinates to the set
                    guessed_coordinates.add((guess_row, guess_col))
                    print("Already targeted. Try again.")
                else:
                    guessed_coordinates.add(
                        (guess_row, guess_col)
                    )  # Add guessed coordinates to the set
                    return guess_row, guess_col
            except ValueError:
                print("Invalid input. Enter integers only.")

    def mark_hit(self, row, col, other_player, source):
        """
        Mark hit method where every hit and miss is printed out
        """
        if other_player.board[row][col] != ".":
            print(Fore.RED + f"{source} Hit!\U0001F525")
            other_player.board[row][col] = "X"
            print(Style.RESET_ALL)
        else:
            print(Fore.GREEN + f"{source} Miss!\U0001F61E")
            other_player.board[row][col] = "M"
            print(Style.RESET_ALL)

    def check_win(self, other_player):
        """
        Check win method where the game checks if someone wins the game after hitting all the ships
        """
        # Iterate through each ship
        for ship in other_player.ships.items():
            # Check if all cells of the ship are marked as hit
            if all(
                other_player.board[row][col] == "X"
                for row in range(10)
                for col in range(10)
                if other_player.board[row][col] == ship[0]
            ):
                continue
            else:
                return False
        return True


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
    """
    Play game function, where each player takes it's turn
    """
    player = Player("Player")
    computer = Computer()

    player.place_ships()
    computer.place_ships()

    while True:
        player.display_board(hide_computer_ships=True)
        computer.display_board()

        # Player's turn
        player_guess_row, player_guess_col = player.take_turn(computer)
        player.mark_hit(player_guess_row, player_guess_col, computer, source="Player")
        if player.check_win(computer):
            print("Congratulations! You sank all computer's ships. You win!")
            break

        # Computer's turn
        computer_guess_row, computer_guess_col = computer.take_turn(player)
        computer.mark_hit(
            computer_guess_row, computer_guess_col, player, source="Computer"
        )
        if computer.check_win(player):
            print("Oh no! Computer sank all your ships. You lose!")
            break


# Checks whether the Python script is being run as the main program or if it is being imported as a module into another script.
if __name__ == "__main__":
    print("Welcome to Battleships game!")
    print(
        "You're mission is to destroy all enemy ships placed on the battlefield, good luck!"
    )
    play_game()
