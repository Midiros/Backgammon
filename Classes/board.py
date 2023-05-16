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
    def _show_init_state(self):
        # print out the initial state of the board
        print('-------------------------')
        print('INITIAL STATE OF THE BOARD')
        print('-------------------------')
        for i in range(24):
            if self.spikes[i].is_empty():
                print(f'Position {i} is empty')
            else:
                print(f'Position {i} has {len(self.spikes[i])} pieces')
                print(f'Player {self.spikes[i].peek().player_number} has the top piece')
        print('-------------------------')

    def _show_state(self):
        print('-------------------------')
        print('CURRENT STATE OF THE BOARD')
        print('-------------------------')
        for i in range(24):
            if self.spikes[i].is_empty():
                print(f'Position {i} is empty')
            else:
                print(f'Position {i} has {len(self.spikes[i])} pieces')
                print(f'Player {self.spikes[i].peek().player_number} has the top piece')
        print('-------------------------')


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
    
    def print_border(self):
        print('|-----------------------|---|-----------------------|')

    def print_spikes_index(self, spikes_side) -> None:
        print('|', end='')
        for _ in spikes_side:
            if(_ == 1):
                print(f' {_}', end=' ')
                continue
            elif _ == spikes_side[-1]:
                print(_, end=' ') #(f'{_} ')
                continue
            elif _ == spikes_side[6]:
                if len(str(_)) == 1:
                    print(f'|   | {_}', end=' ')
                    print(' ', end='')
                else:
                    print(f'|   |{_}', end='  ')
                continue
            elif _ == spikes_side[5]:
                if len(str(_)) == 1:
                    print(f' {_}', end=' ')
                else:
                    print(f'{_}', end=' ')
                continue
            elif len(str(_)) == 1:
                print(f' {_}', end='  ')
                continue
            elif _ == spikes_side[5]:
                print(f' {_}', end='')
                continue    
            else:
                print(_, end='  ') #(f'{_}  ')
        print('|')


    def display_board(self):
        top_spikes = [13,14,15,16,17,18,19,20,21,22,23,24]
        bottom_spikes = [12,11,10,9,8,7,6,5,4,3,2,1]

        # index pozice v commandline 2,6,10,14,18,22,26,30,34,38,42,46,50 kazda pozice je X/O hrac 1/2
        top_position_index = {
            '13': 2,
            '14': 6,
            '15': 10,
            '16': 14,
            '17': 18,
            '18': 22,
            '19': 30,
            '20': 34,
            '21': 38,
            '22': 42,
            '23': 46,
            '24': 50,
            # HORNI STRANA BOARDU
        }

        bottom_position_index = {
            '12': 50,
            '11': 46,
            '10': 42,
            '9': 38,
            '8': 34,
            '7': 30,
            '6': 22,
            '5': 18,
            '4': 14,
            '3': 10,
            '2': 6,
            '1': 2
        }

        # musim alokovat spikes -1, protoze indexy zacinaji od 0
        for row in range(15):
            if row == 0 or row == 14:
                self.print_border()
                continue
            elif row == 2:
                self.print_spikes_index(top_spikes)
            elif row == 13:
                self.print_spikes_index(bottom_spikes)

            print('|', end='')
            for column in range(51):
                if row in range(2,13):
                    if(column == 23 or column == 27):
                        print('|', end='')
                    elif(column in range(24,27)):
                        print(' ', end='')
                    elif row == 7:
                        print(' ', end='')
                        continue
                    elif column in top_position_index.values():
                        for key, value in top_position_index.items():
                            if value == column:
                                #!TODO TEST PRO VYPSANI FIGUREK
                                # if column == 22:
                                #     print(int(key), end=' ')
                                #     continue
                                # elif column == 50:
                                #     print(int(key), end=' ')
                                #     continue
                                # else:
                                #     print(int(key), end='  ')
                                
                                if column == 22:
                                    print(' X', end=' ')
                                    continue
                                elif column == 50:
                                    print(' X', end=' ')
                                    continue
                                else:
                                    print(' X', end='  ')
                                


                # elif column in bottom_position_index.values():
                #     for key, value in bottom_position_index.items():
                #         if value == column:
                #             print(int(key), end='  ')

                


                elif(column in [23,24,25,26,27]):
                    if(column == 23 or column == 27):
                        print('|', end='')
                    elif(row == 7):
                        if(column == 24):
                            print('B', end='')
                        elif(column == 25):
                            print('A', end='')
                        elif(column == 26):
                            print('R', end='')
                        continue
                    else:
                        print(' ', end='')
                else:
                    print(' ', end='')
            print('|')

                

    #TODO - Prio
    #display board in cosole


    #TODO   
    def load_state():
        pass

    #TODO   
    def save_state():
        pass


# create a 2 dimensional array for the board (24 positions) based on the pieces positions

board = Board(Player('Petr', 1), Player('Jirka', 2))

# board._show_init_state()
board.display_board()

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