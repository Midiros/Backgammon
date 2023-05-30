import random
from stone import Stone
from dice import Dice
from player import Player
from stack import Stack
from spike import Spike

class Board():
    def __init__(self, player1: Player, player2: Player):
        self.board = []
        self.player1 = player1
        self.player2 = player2
        self.dice = Dice()
        self.spikes = []

        # Vytvori 24 poli pro hraci desku
        for i in range(24):
            self.spikes.append(Spike())

        # for i in range(24):
        #     self.spikes.append(Stack())
        

        
        #!  CISTE PRO TESTING
        # self.player1 = Player('Petr', 1)
        # self.player2 = Player('Jirka', 2)
        #!  CISTE PRO TESTING
        
        # player1_starter_positions = [0, 11, 16, 18]
        player1_starter_positions = {   0: 2,
                                        11: 5,
                                        16: 3, 
                                        18: 5}
        # player2_starter_positions = [5, 7, 12, 23]
        player2_starter_positions = {   5: 5,
                                        7: 3,
                                        12: 5,
                                        23: 2}

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



    def add_to_bar(self, player, stone):
        if player == 1:
            self.player1.pieces[stone].position = -1
            self.player1.bar.add_to_bar(player, stone)
            board.spikes[stone.position].pop()
            # print(f'Player 1: {len(self.player1.pieces)}', end='')
            # print(f'kamen {self.player1.pieces[stone.stone_index]} byl presunut do baru')
        elif player == 2:
            self.player2.pieces[stone].position = -1
            self.player2.bar.add_to_bar(player, stone)
            board.spikes[stone.position].pop()
            # print(f'Player 2: {len(self.player2.pieces)}', end='')
            # print(f'kamen {self.player2.pieces[stone.stone_index]} byl presunut do baru')

    #     return board
    def _show_init_state(self):
        # print out the initial state of the board
        print('                       --')
        print('INITIAL STATE OF THE BOARD')
        print('                       --')
        for i in range(24):
            if self.spikes[i].is_empty():
                print(f'Position {i} is empty')
            else:
                print(f'Position {i} has {len(self.spikes[i])} pieces')
                print(f'Player {self.spikes[i].peek().player_number} has the top piece')
        print('                       --')

    def _show_state(self):
        print('                       --')
        print('CURRENT STATE OF THE BOARD')
        print('                       --')
        for i in range(24):
            if self.spikes[i].is_empty():
                print(f'Position {i} is empty')
            else:
                print(f'Position {i} has {len(self.spikes[i])} pieces')
                print(f'Player {self.spikes[i].peek().player_number} has the top piece')
        print('                       --')


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
        print('|                        |---|                        |')

    def display_board(self):
        top_spikes_indexes = [13,14,15,16,17,18,'BAR',19,20,21,22,23,24]
        bottom_spikes_indexes = [12,11,10,9,8,7,'BAR',6,5,4,3,2,1]
        top_spikes = [12,13,14,15,16,17,'BAR',18,19,20,21,22,23]
        bottom_spikes = [11,10,9,8,7,6,'BAR',5,4,3,2,1,0]


        #FIXME - MAIN BOARD
        board.print_border()
        board.print_spike_indexes(top_spikes)

        board.print_top_gameboard(top_spikes)
        # board.print_playfield(top_spikes_indexes)

        board.print_middle_bar_row()
        
        board.print_bottom_gameboard(bottom_spikes)
        # board.print_playfield(bottom_spikes_indexes)

        board.print_spike_indexes(bottom_spikes)
        board.print_border()


    def print_top_gameboard(self, spikes_side) -> None:
        for row_index in range(0, 5, 1):
            print('|', end='')
            for spike_positions_index, spike in enumerate(spikes_side):
                if spike_positions_index == 6:
                    board.print_bar()
                    continue

                if not board.spikes[spike].is_empty():
                    if len(board.spikes[spike]) > row_index:
                        kamen = board.spikes[spike].peek()
                        if kamen.owner() == 1:
                            print(f"{'X':>4}", end='')
                        else:
                            print(f"{'O':>4}", end='')
                    elif len(board.spikes[spike]) <= row_index:
                        print(f"{'':>4}", end='')
                        
                else:
                    print(f"{'':>4}", end='')
            print('|')


    def print_bottom_gameboard(self, spikes_side) -> None:
        for row_index in range(5, 0, -1):
            print('|', end='')
            for spike_positions_index, spike in enumerate(spikes_side):
                if spike_positions_index == 6:
                    board.print_bar()
                    continue       

                if not board.spikes[spike].is_empty():
                    if len(board.spikes[spike]) >= row_index:
                        kamen = board.spikes[spike].peek()
                        if kamen.owner() == 1:
                            print(f"{'X':>4}", end='')
                        else:
                            print(f"{'O':>4}", end='')
                    elif len(board.spikes[spike]) < row_index:
                        print(f"{'':>4}", end='')

                else:
                    print(f"{'':>4}", end='')
            print('|')


    def print_playfield(self, spikes_side) -> None:
        for row_index in range(5):
            # counter += 1
            spike_index_counter = 0
            for spike_index in range(0,6):
                current_spike_index = spikes_side[spike_index]
                current_spike = board.spikes[current_spike_index]
                print(current_spike_index)
                if not board.spikes[current_spike_index].is_empty():
                    if current_spike_index < row_index:
                        kamen = current_spike.peek()
                        if kamen.owner() == 1:
                            print('X', end='')
                        else:
                            print('O', end='')
                else:
                    print(' ', end='')
                spike_index_counter += 1

                # else:
                #     print(' ', end='')
            board.print_bar()
            for spike_index in range(5, 11):
                current_spike_index = spikes_side[spike_index_counter]
                current_spike = board.spikes[current_spike_index]
                print(current_spike_index)
                if not board.spikes[current_spike_index].is_empty():
                    if current_spike_index < row_index:
                        kamen = current_spike.peek()
                        if kamen.owner() == 1:
                            print('X', end='')
                        else:
                            print('O', end='')
                else:
                    print(' ', end='')
                spike_index_counter += 1

                # if current_spike_index < row_index:
                #     if board.spikes[current_spike_index].peek() == 1:
                #         print('X', end='')
                #     else:
                #         print('O', end='')
                # else:
                #     print(' ', end='')
            print('|')
        # print('counter: ', counter)
        # print('spikes_index counter: ', spike_index_counter)


    def print_middle_bar_row(self):
        print('|                        |BAR|                        |')
    



    def print_spike_indexes(self, spikes_side):
        print('|', end='')
        for column in range(0, 6):
            print(f'{spikes_side[column]:>4}', end='')
        board.print_bar()
        for column in range(7, 13):
            print(f'{spikes_side[column]:>4}', end='')
        print('|')






    #TODO - Prio
    #display board in cosole

    def print_bar(self):
        print('|   |', end='')


    #TODO   
    def load_state():
        pass

    #TODO   
    def save_state():
        pass


    def movePiece(self, player, originSpike, targetSpike):
        if player == 1:
            piece = self.spikes[originSpike].pop()
            self.player1.move_piece(piece, targetSpike)
            self.spikes[targetSpike].push(piece)
        elif player == 2:
            piece = self.spikes[originSpike].pop()
            self.player2.move_piece(piece, targetSpike)
            self.spikes[targetSpike].push(piece)



# create a 2 dimensional array for the board (24 positions) based on the pieces positions

board = Board(Player('Petr', 1), Player('Jirka', 2))

# board._show_init_state()
board.display_board()


print(len(board.spikes[0]))
    
board.player1.add_piece_to_bar(board.player1.pieces[1])


print(board.player1.pieces[1])

print(len(board.spikes[0]))



board.movePiece(1, 0, 1)
board.movePiece(1, 0, 1)

board.movePiece(2, 5, 3)
board.movePiece(2, 5, 3)
board.movePiece(2, 5, 3)
board.movePiece(2, 5, 3)


board.display_board()







# board.player1.move_piece(3, 3)
# board.player1.add_piece_to_bar(board.player1.pieces[3])
# board.player1.move_piece(3, 5)


# board.add_to_bar(1, board.player1.pieces[3])
# print(board.player1.pieces[3])
# board.player1.move_piece(3, 3)
# board.player1.move_piece(3, 5)
# board.add_to_bar(1, board.player1.pieces[0])
# board.player1.roll_dice()
#!TEST
# for index,spike in enumerate(board.spikes):
#     if(len(spike)) > 0:
#         print(index, end=' ')
#         print(len(spike))

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


# for index, spike in enumerate(board.spikes):
#     if len(spike) > 0:
#         print(index, end=' ')
#         print(len(spike))
#         kamen = spike.peek()
#         print(kamen.owner())
