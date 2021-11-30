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

    def convert_tile_to_verticies(tile):
        converter = {
            [1,1]: [[5,5], [55, 55]],
            [2,1]: [[10, 5], [60, 55]],
            [3,1]: [[15, 5], [65, 55]],
            [1,2]: [[5, 10], [55, 65]],
            [2,2]: [[10, 10], [60, 65]]
            }
        return converter[tile]
                
