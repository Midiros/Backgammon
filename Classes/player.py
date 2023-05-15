from dice import Dice
from stone import Stone

class Player():
    # player1_positions = [0, 0, 11, 11, 11, 11, 11, 16, 16, 16, 18, 18, 18, 18, 18]
    # player2_positions = [23, 23, 12, 12, 12, 12, 12, 7, 7, 7, 5, 5, 5, 5, 5]

    def __init__(self, name, player_number):
        while player_number != 1 and player_number != 2:
            raise ValueError('Player number must be 1 or 2')
        self.name = name
        self.player_number = player_number
        self.dice = Dice()
        self.score = 0
        self.pieces = []      
        # self.pieces_out = []
        # self.pieces_in = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14] # Na zacatku hry je vsech 15 figurek v poli
        # self.generate_pieces()

    # def generate_pieces(self):
    #     for i in range(15):
    #         if(self.player_number == 1):
    #             # Vytvori 15 figurek/kamenu pro hrace 1
    #             self.pieces.append(Stone(self.player_number, i, self.player1_positions[i]))
    #         else:
    #             # Vytvori 15 figurek/kamenu pro hrace 2
    #             self.pieces.append(Stone(self.player_number, i, self.player2_positions[i]))
                

    def move_piece(self, piece, move_position):
        piece.set_position(move_position)
        piece.add_to_history(move_position)
        print(piece.history)

    def roll_dice(self):
        self.dice.roll()
        return self.dice.value
    
    def list_pieces(self):
        for piece in self.pieces:
            print(piece)
    
    def my_score(self):
        return self.score
    
    def my_pieces(self):
        return self.pieces
    
    def __str__(self):
        return self.name

