import random
from colorama import Fore, Back, Style

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
            self.spikes.append(Spike(i))

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
        self.top_spikes_indexes = [13,14,15,16,17,18,'BAR',19,20,21,22,23,24]
        self.bottom_spikes_indexes = [12,11,10,9,8,7,'BAR',6,5,4,3,2,1]
        self.top_spikes = [12,13,14,15,16,17,'BAR',18,19,20,21,22,23]
        self.bottom_spikes = [11,10,9,8,7,6,'BAR',5,4,3,2,1,0]
        

    #     #!TEST
    #     # for key, value in player1_starter_positions.items():
    #     #     print(f'key: {key}')
    #     #     for i in range(value):
    #     #         print(f'{key} klice => {i}. opakovani')













# INITI LINE -------------------------------------







    def add_to_bar(self, player, stone):
        if player == 1:
            self.player1.pieces[stone].position = 99
            self.player1.bar.add_to_bar(player, stone)
            board.spikes[stone.position].pop()
            # print(f'Player 1: {len(self.player1.pieces)}', end='')
            # print(f'kamen {self.player1.pieces[stone.stone_index]} byl presunut do baru')
        elif player == 2:
            self.player2.pieces[stone].position = 99
            self.player2.bar.add_to_bar(player, stone)
            board.spikes[stone.position].pop()
            # print(f'Player 2: {len(self.player2.pieces)}', end='')
            # print(f'kamen {self.player2.pieces[stone.stone_index]} byl presunut do baru')

    def display_board(self):
        

        self.print_border()
        self.print_spike_indexes(self.top_spikes_indexes)

        self.print_top_gameboard(self.top_spikes)

        self.print_middle_bar_row()
        
        self.print_bottom_gameboard(self.bottom_spikes)

        self.print_spike_indexes(self.bottom_spikes_indexes)
        self.print_border()

    def piece_moved_out(self, piece, player_number):
        if(player_number == 1):
            self.pieces_in.remove(piece)
            self.pieces_out.append(piece)
        else:
            self.pieces_in_o.remove(piece)
            self.pieces_out_o.append(piece)

    def roll_dice(self):
        self.dice.roll()
        return self.dice.value

    def print_border(self):
        print(Fore.GREEN + '|~~~~~~~~~~~~~~~~~~~~~~~~|~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~|' + Style.RESET_ALL)



    def print_top_gameboard(self, spikes_side) -> None:
        for row_index in range(0, 5, 1):
            print(Fore.GREEN + '|' + Style.RESET_ALL, end='')
            for spike_positions_index, spike in enumerate(spikes_side):
                if spike_positions_index == 6:
                    print(Fore.GREEN + '|' + Style.RESET_ALL, end='')
                    if len(board.player1.bar) > row_index:
                        print(Fore.RED + f"{'X':^3}", end='')
                    else:
                        print(f"{'':^3}", end='')
                    print(Fore.GREEN + '|' + Style.RESET_ALL, end='')
                    continue

                if not board.spikes[spike].is_empty():
                    if len(board.spikes[spike]) > row_index:
                        kamen = board.spikes[spike].peek()
                        if kamen.owner() == 1:
                            print(Fore.RED + f"{'X':>4}", end='')
                        else:
                            print(Fore.BLUE + f"{'O':>4}", end='')
                    elif len(board.spikes[spike]) <= row_index:
                        print(f"{'':>4}", end='')
                        
                else:
                    print(f"{'':>4}", end='')
            print(Fore.GREEN + '  |' + Style.RESET_ALL)


    def print_bottom_gameboard(self, spikes_side) -> None:
        for row_index in range(5, 0, -1):
            print(Fore.GREEN + '|' + Style.RESET_ALL, end='')
            for spike_positions_index, spike in enumerate(spikes_side):
                if spike_positions_index == 6:
                    print(Fore.GREEN + '|' + Style.RESET_ALL, end='')
                    if len(board.player2.bar) >= row_index:
                        print(Fore.BLUE + f"{'O':^3}", end='')
                    else:
                        print(f"{'':^3}", end='')
                    print(Fore.GREEN + '|' + Style.RESET_ALL, end='')
                    continue      

                if not board.spikes[spike].is_empty():
                    if len(board.spikes[spike]) >= row_index:
                        kamen = board.spikes[spike].peek()
                        if kamen.owner() == 1:
                            print(Fore.RED + f"{'X':>4}", end='')
                        else:
                            print(Fore.BLUE + f"{'O':>4}", end='')
                    elif len(board.spikes[spike]) < row_index:
                        print(f"{'':>4}", end='')

                else:
                    print(f"{'':>4}", end='')
            print(Fore.GREEN + '  |' + Style.RESET_ALL)


    def print_middle_bar_row(self):
        print(Fore.GREEN + '|                        |BAR|                          |' + Style.RESET_ALL)
    



    def print_spike_indexes(self, spikes_side):
        print(Fore.GREEN + '|', end='' + Style.RESET_ALL)
        for column in range(0, 6):
            print(f'{spikes_side[column]:>4}', end='')
        board.print_bar()
        for column in range(7, 13):
            print(f'{spikes_side[column]:>4}', end='')
        print(Fore.GREEN + '  |' + Style.RESET_ALL)




    #TODO - PRIO - nefunguje barrovnai piecue a obcas se pokazi hrani piece ven z herniho pole ? Problem s delkou asi je potreba resit nejak pushovani a popovani



    #TODO - Prio
    #display board in cosole

    def print_bar(self):
        print(Fore.GREEN + '|   |' + Style.RESET_ALL, end='')


    #TODO   
    def load_state():
        pass

    #TODO   
    def save_state():
        pass


    def movePiece(self, player, originSpike, targetSpike):
        if player == 1:
            print('PLAYER 1 MOVE')
            
            # if targetSpike > 23:
            #     print(f'Delka origin SpikE ____ {len(self.spikes[originSpike])}')
            #     print('PIECE OUT')
            #     self.spikes[originSpike].pop()
            if len(self.spikes[targetSpike]) == 1 and (self.spikes[targetSpike].peek().owner() == 2):
                    print('POSUNOUT NA BAR')
                    # print(f'Delka origin spike before ____ {len(self.spikes[originSpike])}')
                    # print(f'Delka target spike before ____ {len(self.spikes[targetSpike])}')

                    self.addToBar(2, targetSpike)
                    piece = self.spikes[originSpike].pop()
                    self.spikes[targetSpike].push(piece)
                    # print(f'Delka origin spike after ____ {len(self.spikes[originSpike])}')
                    # print(f'Delka target spike after ____ {len(self.spikes[targetSpike])}')
            else:
                # print(f'Delka origin spike before ____ {len(self.spikes[originSpike])}')
                # print(f'Delka target spike before ____ {len(self.spikes[targetSpike])}')

                piece = self.spikes[originSpike].pop()
                self.player1.move_piece(piece, targetSpike)
                self.spikes[targetSpike].push(piece)
                # print(f'Delka origin spike after ____ {len(self.spikes[originSpike])}')
                # print(f'Delka target spike after ____ {len(self.spikes[targetSpike])}')

        elif player == 2:
            print('PLAYER 2 MOVE')
            # if targetSpike < 0:
            #     print(f'Delka origin SPIKE ____ {len(self.spikes[originSpike])}')
            #     print('PIECE OUT')
            #     self.spikes[originSpike].pop()
            if len(self.spikes[targetSpike]) == 1 and (self.spikes[targetSpike].peek().owner() == 1):
                    print('POSUNOUT NA BAR')
                    # print(f'Delka origin spike before ____ {len(self.spikes[originSpike])}')
                    # print(f'Delka target spike before ____ {len(self.spikes[targetSpike])}')

                    self.addToBar(1, targetSpike)
                    piece = self.spikes[originSpike].pop()
                    self.spikes[targetSpike].push(piece)
                    # print(f'Delka origin spike after ____ {len(self.spikes[originSpike])}')
                    # print(f'Delka target spike after ____ {len(self.spikes[targetSpike])}')

            else:
                # print(f'Delka origin spike before ____ {len(self.spikes[originSpike])}')
                # print(f'Delka target spike before ____ {len(self.spikes[targetSpike])}')

                piece = self.spikes[originSpike].pop()
                self.player2.move_piece(piece, targetSpike)
                self.spikes[targetSpike].push(piece)
                # print(f'Delka origin spike after ____ {len(self.spikes[originSpike])}')
                # print(f'Delka target spike after ____ {len(self.spikes[targetSpike])}')



    #? Argument -- player is number of player we are attacking 
    def addToBar(self, player, spike):
        if player == 1:
            piece = self.spikes[spike].pop()
            print(piece)
            self.player1.add_piece_to_bar(piece)
        elif player == 2:
            piece = self.spikes[spike].pop()
            print(piece)
            self.player2.add_piece_to_bar(piece)

    def main(self):
        
        playerOnTurn = 0
        startingDice = self.dice.whoStarts()
        if startingDice[0] > startingDice[1]:
            self.player1.diceValues = startingDice
            playerOnTurn = 0
        else:
            self.player2.diceValues = startingDice
            playerOnTurn = 1
        self.display_board()
        while self.player1.pieces or self.player2.pieces:
            if playerOnTurn == 0:
                print(Fore.RED + f'Player {self.player1.name} is on turn | X | 1' + Style.RESET_ALL)
                self.player1.moveSetPlayer1(self.spikes, self)
                self.display_board()
                playerOnTurn = 1
            else:
                print(Fore.BLUE + f'Player {self.player2.name} is on turn | O | 2' + Style.RESET_ALL)
                self.player2.moveSetPlayer2(self.spikes, self)
                self.display_board()
                playerOnTurn = 0

        #? Tohle je prozatimni konecny stav hry check
        #! Čti tak že v moment kdy hráč má všechny svoje kameny na homeboardu -> nelze mu vygenerovat platne tahy
        #! Teda hra skončí v nekonečné smyčce



        #? Tohle bude finalni konecný stav hry check
        if self.player1.pieces.__len__ == 0:
            print("Player 1 has won!")
        else:
            print("Player 2 has won!")

board = Board(Player('Petr', 1), Player('Jirka', 2))

# board.addToBar(2,23)


board.main()








# HRAC 1 == X
# HRAC 2 == O