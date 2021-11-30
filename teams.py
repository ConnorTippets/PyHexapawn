from pawn import Pawn
possible_tiles = [[1,1], [2,1], [3,1], [1,2], [2,2]]

class Team:
    def __init__(self, type):
        self.type = type
        self.pawns = [Pawn(tile, self) for tile in possible_tiles]

    def str(self):
        return self.type
