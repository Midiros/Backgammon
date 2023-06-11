import random
import os

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

#! Hlavni metoda printeni boardu do CLI
    def display_board(self):
        self.print_border()
        self.print_spike_indexes(self.top_spikes_indexes)
        self.print_top_gameboard(self.top_spikes)
        self.print_middle_bar_row()
        self.print_bottom_gameboard(self.bottom_spikes)
        self.print_spike_indexes(self.bottom_spikes_indexes)
        self.print_border()

#? Zatim WIP
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



#! Projede vsechny radky v HORNI polovine hraci desky a vytiskne vsechny kaminky ktere jsou na HORNICH spikes
    def print_top_gameboard(self, spikes_side) -> None:
        for row_index in range(0, 5, 1):
            print(Fore.GREEN + '|' + Style.RESET_ALL, end='')
            for spike_positions_index, spike in enumerate(spikes_side):
                #! Pokud je spike_positions_index 6, tak se jedna o bar > viz nahore v top_spike_indexes
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


#! Projede vsechny radky v DOLNI polovine hraci desky a vytiskne vsechny kaminky ktere jsou na dolnich spikes
    def print_bottom_gameboard(self, spikes_side) -> None:
        for row_index in range(5, 0, -1):
            print(Fore.GREEN + '|' + Style.RESET_ALL, end='')
            for spike_positions_index, spike in enumerate(spikes_side):
                #! Pokud je spike_positions_index 6, tak se jedna o bar > viz nahore v bottom_spike_indexes
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
    


#! Printuje indexy spikeu na hraci desce
    def print_spike_indexes(self, spikes_side):
        print(Fore.GREEN + '|', end='' + Style.RESET_ALL)
        for column in range(0, 6):
            print(f'{spikes_side[column]:>4}', end='')
        board.print_bar()
        for column in range(7, 13):
            print(f'{spikes_side[column]:>4}', end='')
        print(Fore.GREEN + '  |' + Style.RESET_ALL)




    #TODO - PRIO - nefunguje barrovnai piecue a obcas se pokazi hrani piece ven z herniho pole ? Problem s delkou asi je potreba resit nejak pushovani a popovani

    def print_bar(self):
        print(Fore.GREEN + '|   |' + Style.RESET_ALL, end='')

    def print_bar(self):
        print(Fore.GREEN + '|   |' + Style.RESET_ALL, end='')


    #TODO   
    def load_state():
        pass

    #TODO   
    def save_state():
        pass

#!Bere startovni spike, cilovy spike a hrace a podle toho jestli je na cilovem spike nejaky kamen protihrace, tak ho bud vyhodi na bar a nebo presune svuj kamen 
    def movePiece(self, player, originSpike, targetSpike):
        if player == 1:
            if len(self.spikes[targetSpike]) == 1 and (self.spikes[targetSpike].peek().owner() == 2):
                    self.addToBar(2, targetSpike)
                    piece = self.spikes[originSpike].pop()
                    self.spikes[targetSpike].push(piece)
            else:
                piece = self.spikes[originSpike].pop()
                self.player1.move_piece(piece, targetSpike)
                self.spikes[targetSpike].push(piece)

        elif player == 2:
            if len(self.spikes[targetSpike]) == 1 and (self.spikes[targetSpike].peek().owner() == 1):
                    self.addToBar(1, targetSpike)
                    piece = self.spikes[originSpike].pop()
                    self.spikes[targetSpike].push(piece)
            else:
                piece = self.spikes[originSpike].pop()
                self.player2.move_piece(piece, targetSpike)
                self.spikes[targetSpike].push(piece)

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
            print(Fore.YELLOW + 'Player 1 has won!' + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + 'Player 2 has won!' + Style.RESET_ALL)

board = Board(Player('Petr', 1), Player('Jirka', 2))

board.main()





# HRAC 1 == X
# HRAC 2 == O