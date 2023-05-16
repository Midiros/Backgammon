import random
from stone import Stone
from dice import Dice
from player import Player
from stack import Stack

class Board():
    def __init__(self, player1: Player, player2: Player):
        self.board = []
        self.player1 = player1
        self.player2 = player2
        self.dice = Dice()
        self.spikes = []

        # Vytvori 24 poli pro hraci desku
        for i in range(24):
            self.spikes.append(Stack())

        # for i in range(24):
        #     self.spikes.append(Stack())

        
        #!  CISTE PRO TESTING
        # self.player1 = Player('Petr', 1)
        # self.player2 = Player('Jirka', 2)
        #!  CISTE PRO TESTING
        
        # player1_starter_positions = [0, 11, 16, 18]
        player1_starter_positions = {   '0': 2,
                                        '11': 5,
                                        '16': 3, 
                                        '18': 5}
        # player2_starter_positions = [5, 7, 12, 23]
        player2_starter_positions = {   '5': 2,
                                        '7': 5,
                                        '12': 3,
                                        '23': 5}

        # Vytvori 15 figurek/kamenu pro hrace 1
        index = 0
        for key, value in player1_starter_positions.items():
            for counter in range(value):
                self.player1.pieces.append(Stone(self.player1.player_number, index, int(key)))
                self.spikes[int(key)].push(self.player1.pieces[index])  
                index += 1
        # Vytvori 15 figurek/kamenu pro hrace 2
        index = 0
        for key, value in player2_starter_positions.items():
            for counter in range(value):
                self.player2.pieces.append(Stone(self.player2.player_number, index, int(key)))    
                self.spikes[int(key)].push(self.player2.pieces[index])  
                index += 1

        self.pieces_X = self.player1.pieces
        self.pieces_in_X = self.pieces_X
        self.pieces_out_X = []
        self.pieces_Y = self.player2.pieces
        self.pieces_in_Y = self.pieces_Y
        self.pieces_out_Y = []

    #     #!TEST
    #     # for key, value in player1_starter_positions.items():
    #     #     print(f'key: {key}')
    #     #     for i in range(value):
    #     #         print(f'{key} klice => {i}. opakovani')

    #     return board

    def piece_moved_out(self, piece, player_number):
        if(player_number == 1):
            self.pieces_in.remove(piece)
            self.pieces_out.append(piece)
        else:
            self.pieces_in_o.remove(piece)
            self.pieces_out_o.append(piece)

    def piece_finished(self, piece, player_number):
        pass

    def roll_dice(self):
        self.dice.roll()
        return self.dice.value

    def move_piece(self, piece, move_position, player_number):
        self.board[piece] = '' # odstrani kamen z puvodni pozice
        self.piece.set_position(move_position) # nastavi novou pozici kamene

        if(player_number == 1): 
            self.board[move_position] = 'X'
        else:
            self.board[move_position] = 'O'
            
        return self.board 



    #TODO - Prio
    #display board in cosole


    #TODO   
    def load_state():
        pass

    #TODO   
    def save_state():
        pass


board = Board(Player('Petr', 1), Player('Jirka', 2))


# print(f'player1: {board.player1.name}')
# board.player1.list_pieces()

# index = 0
# for piece in board.pieces_X:
#     print(piece.player_number)
#     index +=1 
# print(index)

# print('------------------')
# index = 0
# for piece in board.pieces_Y:
#     print(piece.player_number)
#     index +=1 
# print(index)

#FIXME test pro spikes
# print(len(board.spikes))
# kamen14 = board.spikes[23].pop()
# kamen15 = board.spikes[23].pop()

# print(kamen14)
# print(kamen15)
# print(board.player1.pieces[12])


# for figurka in board.player1.pieces:
#     print(figurka.position)
# print('------------------')
# for figurka in board.player2.pieces:
#     print(figurka.position)