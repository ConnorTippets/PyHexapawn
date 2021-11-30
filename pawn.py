def debug_ai_move(position, pawn):
    pass

class Pawn:
    def __init__(self, tile:list, team):
        self.tile = tile
        self.move = None
        if str(team) == "AI":
            self.team = "AI"
            self.move = debug_ai_move
        if str(team) == "Human":
            self.team = "Human"
            self.move = None

    def convert_tile_to_verticies(self, tile):
        converter = {
            str([1,1]): [[5,5], [55, 5], [55, 55], [5, 55]],
            str([2,1]): [[10, 5], [60, 5], [60, 55], [10, 55]],
            str([3,1]): [[15, 5], [65, 5], [65, 55], [15, 55]],
            str([1,2]): [[5, 10], [55, 10], [55, 65], [5, 65]],
            str([2,2]): [[10, 10], [60, 10], [60, 65], [10, 65]]
            }
        return converter[str(tile)]
                
