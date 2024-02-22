from random import randint

class Player:
    def __init__(self, name):
        self.name = name
        self.board = [["." for _ in range(10)] for _ in range(10)]
        self.ships = {"carrier": 5, "battleship": 4, "cruiser": 3, "submarine": 3, "destroyer": 2}

    def place_ships(self):
        for ship, size in self.ships.items():
            self.place_ship(ship, size)

    def check_shot(self, board, row, col):
        pass

player = Player(10)
