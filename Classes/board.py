import random
import os
import json
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
        # place holder for player on turn
        self.playerOnTurn = 15

        # Vytvori 24 poli pro hraci desku
        for i in range(24):
            self.spikes.append(Spike(i))



    # ! DEFAULT STARTER POSITIONS
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


    #! BEAR OFF STARTER POSITIONS
        # # player1_starter_positions = [0, 11, 16, 18]
        # player2_starter_positions = {   0: 5,
        #                                 1: 5,
        #                                 2: 3, 
        #                                 6: 2}
        # # player2_starter_positions = [5, 7, 12, 23]
        # player1_starter_positions = {   17: 2,
        #                                 21: 3,
        #                                 22: 5,
        #                                 23: 5}


    #! FINISH GAME TEST POSITIONS
        # player2_starter_positions = {   3: 2,
        #                                 4: 2,
        #                                 5: 2,}
        # player1_starter_positions = {   20: 2,
        #                                 21: 2,
        #                                 22: 2,
        #                                 23: 2,
        #                                 8: 2}




        #! Pokud nejsou jeste vytvoreny figury/kameny, vytvori je
        #! Pro pripad load/continue hry z minulosti
        if self.player1.pieces == [] and self.player2.pieces == []:
            #! Vytvori 15 figurek/kamenu pro hrace 1
            index = 0
            for key, value in player1_starter_positions.items():
                for counter in range(value):
                    self.player1.pieces.append(Stone(self.player1.player_number, index, int(key), self.player1.name))
                    self.spikes[int(key)].push(self.player1.pieces[index])  
                    index += 1
            #! Vytvori 15 figurek/kamenu pro hrace 2
            index = 0
            for key, value in player2_starter_positions.items():
                for counter in range(value):
                    self.player2.pieces.append(Stone(self.player2.player_number, index, int(key), self.player2.name))    
                    self.spikes[int(key)].push(self.player2.pieces[index])  
                    index += 1

        #! Display indexy 
        self.top_spikes_indexes = [13,14,15,16,17,18,'BAR',19,20,21,22,23,24]
        self.bottom_spikes_indexes = [12,11,10,9,8,7,'BAR',6,5,4,3,2,1]
        #! Value indexy -> proto obcas -1/+1
        self.top_spikes = [12,13,14,15,16,17,'BAR',18,19,20,21,22,23]
        self.bottom_spikes = [11,10,9,8,7,6,'BAR',5,4,3,2,1,0]


#! Metoda pro ukladani stavu hry do JSON souboru
    def save_game(self):
        gameData = {
            'player1': {
                'pieces': {},
                'stats': {}
            },
            'player2': {
                'pieces': {},
                'stats': {}
            },
            'playerOnTurn': self.playerOnTurn
        }

        for piece in self.player1.pieces:
            gameData['player1']['pieces'][piece.stone_index] = {'player_number': piece.player_number, 'index': piece.stone_index, 'position': piece.position, 'name': piece.player_name, 'history': piece.history}

        for piece in self.player2.pieces:
            gameData['player2']['pieces'][piece.stone_index] = {'player_number': piece.player_number, 'index': piece.stone_index, 'position': piece.position, 'name': piece.player_name, 'history': piece.history}


        gameData['player1']['stats'] = {'name': self.player1.name, 'player_number': self.player1.player_number, 'finishedPieces': self.player1.FinishedPieces, 'diceValues': self.player1.diceValues, 'piecesSentToBar': self.player1.piecesSentToBar}
        gameData['player2']['stats'] = {'name': self.player2.name, 'player_number': self.player2.player_number, 'finishedPieces': self.player2.FinishedPieces, 'diceValues': self.player2.diceValues, 'piecesSentToBar': self.player1.piecesSentToBar}

        # os.remove('../assets/saveGame.json')

        with open('../assets/saveGame.json', 'w') as saveFile:
            json.dump(gameData, saveFile, indent=4)
            saveFile.close()



#! Metoda pro clearovani CLI
    def clear(self):
        clear = os.system('cls' if os.name=='nt' else 'clear')

#! Hlavni metoda printeni boardu do CLI
    def display_board(self):
        self.print_border()
        self.print_spike_indexes(self.top_spikes_indexes)
        self.print_top_gameboard(self.top_spikes)
        self.print_middle_bar_row()
        self.print_bottom_gameboard(self.bottom_spikes)
        self.print_spike_indexes(self.bottom_spikes_indexes)
        self.print_border()


#! Metoda pro printeni borderu hraci desky
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


#! Vytiskne prostredni radku hraci desky
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

    def print_bar(self):
        print(Fore.GREEN + '|   |' + Style.RESET_ALL, end='')

    def print_bar(self):
        print(Fore.GREEN + '|   |' + Style.RESET_ALL, end='')


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

    #? Argument -- player is the number of player we are attacking 
    def addToBar(self, player, spike):
        if player == 1 and len(self.spikes[spike]) > 0:
            piece = self.spikes[spike].pop()
            # print(piece)
            piece.add_to_history('BAR')
            piece.position = 'BAR'
            self.player1.add_piece_to_bar(piece)
        elif player == 2 and len(self.spikes[spike]) > 0:
            piece = self.spikes[spike].pop()
            # print(piece)
            piece.add_to_history('BAR')
            piece.position = 'BAR'
            self.player2.add_piece_to_bar(piece)

    def bearOffState(self, player):
        if player == 1:
            for spike in self.spikes[0:18:1]:
                if spike.myLen() > 0 and spike.peek().owner() == 1:
                    return False
        elif player == 2:
            for spike in self.spikes[23:5:-1]:
                if spike.myLen() > 0 and spike.peek().owner() == 2:
                    return False
        return True

#! Method for statistics
    def getStats(self):
        averageTTL_player1 = 0
        averageTTL_player2 = 0

        averageTTL_player1 = self.player1.allFinishedPieces.getHistoryAverage()
        averageTTL_player2 = self.player2.allFinishedPieces.getHistoryAverage()
        print(Fore.RED + f'{board.player1.name} ~ average stone hops before reaching finish: {averageTTL_player1}' + Style.RESET_ALL)
        print(Fore.RED + f'{board.player1.name} ~ amount of pieces finished: {board.player1.FinishedPieces}' + Style.RESET_ALL)
        print(Fore.RED + f'{board.player1.name} ~ amount of enemy stones u kicked to bar: {self.player1.piecesSentToBar}' + Style.RESET_ALL)
        print(Fore.BLUE + f'{board.player2.name} ~ average stone hops before reaching finish: {averageTTL_player2}' + Style.RESET_ALL)
        print(Fore.BLUE + f'{board.player2.name} ~ amount of pieces finished: {board.player2.FinishedPieces}' + Style.RESET_ALL)
        print(Fore.BLUE + f'{board.player2.name} ~ amount of enemy stones u kicked to bar: {self.player2.piecesSentToBar}' + Style.RESET_ALL)



#! Method for checking what type of win has been achieved gammon/backgammon/normal
    def typeOfWin(self):
        if len(self.player1.bar) > 0 or self.player1.bareState == False:
            print(Fore.BLUE + f'{board.player2.name} ~ is the WINNER ~ Backgammon type of win' + Style.RESET_ALL)
            print(Fore.BLUE + f'{board.player2.name} ~ wins TRIPLE the value of the stake' + Style.RESET_ALL)
        elif len(self.player2.bar) > 0 or self.player2.bareState == False:
            print(Fore.RED + f'{board.player1.name} ~ is the WINNER ~ Backgammon type of win' + Style.RESET_ALL)
            print(Fore.RED + f'{board.player1.name} ~ wins TRIPLE the value of the stake' + Style.RESET_ALL)
        elif self.player1.FinishedPieces == 0:
            print(Fore.BLUE + f'{board.player2.name} ~ is the WINNER ~ Gammon type of win' + Style.RESET_ALL)
            print(Fore.BLUE + f'{board.player2.name} ~ wins DOUBLE the value of the stake' + Style.RESET_ALL)
        elif self.player2.FinishedPieces == 0:
            print(Fore.RED + f'{board.player1.name} ~ is the WINNER ~ Gammon type of win' + Style.RESET_ALL)
            print(Fore.RED + f'{board.player1.name} ~ wins DOUBLE the value of the stake' + Style.RESET_ALL)
        elif self.player1.FinishedPieces == len(self.player1.pieces):
            print(Fore.RED + f'{board.player1.name} ~ is the WINNER ~ Normal type of win' + Style.RESET_ALL)
            print(Fore.RED + f'{board.player1.name} ~ wins the value of the stake' + Style.RESET_ALL)
        elif self.player2.FinishedPieces == len(self.player2.pieces):
            print(Fore.BLUE + f'{board.player2.name} ~ is the WINNER ~ Normal type of win' + Style.RESET_ALL)
            print(Fore.RED + f'{board.player2.name} ~ wins the value of the stake' + Style.RESET_ALL)
    

#! Main game loop
    def main(self):
        self.clear()
        if self.playerOnTurn == 0 or self.playerOnTurn == 1:
            print(Fore.CYAN + 'Continuing game' + Style.RESET_ALL)
        else:
            startingDice = self.dice.whoStarts()
            if startingDice[0] > startingDice[1]:
                self.player1.diceValues = startingDice
                self.playerOnTurn = 0
            else:
                self.player2.diceValues = startingDice
                self.playerOnTurn = 1
        self.display_board()
        while (self.player1.FinishedPieces < len(self.player1.pieces)) and (self.player2.FinishedPieces < len(self.player2.pieces)):
            if self.playerOnTurn == 0:
                self.player1.bareState = self.bearOffState(1)
                print(Fore.RED + f'Player {self.player1.name} is on turn | X | 1' + Style.RESET_ALL)
                self.player1.moveSetPlayer1(self.spikes, self)
                self.display_board()
                self.playerOnTurn = 1
            else:
                self.player2.bareState = self.bearOffState(2)
                if self.player2.AIstate == True:
                    self.clear()
                print(Fore.BLUE + f'Player {self.player2.name} is on turn | O | 2' + Style.RESET_ALL)
                self.player2.moveSetPlayer2(self.spikes, self)
                self.display_board()
                self.playerOnTurn = 0

    #! Method for checking who won and what type of win
        self.typeOfWin()

        print(Fore.GREEN + '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + Style.RESET_ALL)
        
        self.getStats()
        if os.path.isfile('../assets/saveGame.json'):
            os.remove('../assets/saveGame.json')



#! Function for loading the save file
def loadGame():
    with open('../assets/saveGame.json', 'r') as saveFile:
        gameData = json.load(saveFile)
        board = Board(Player(gameData['player1']['stats']['name'], 1), Player(gameData['player2']['stats']['name'], 2))
        board.player1.pieces = []
        board.player2.pieces = []
        board.spikes = []
        board.player1.diceValues = gameData['player1']['stats']['diceValues']
        board.player2.diceValues = gameData['player2']['stats']['diceValues']

        for i in range(24):
            board.spikes.append(Spike(i))
        board.player1.FinishedPieces = gameData['player1']['stats']['finishedPieces']
        board.player2.FinishedPieces = gameData['player2']['stats']['finishedPieces']
        for piece in gameData['player1']['pieces']:
            kamen = Stone(gameData['player1']['pieces'][piece]['player_number'], gameData['player1']['pieces'][piece]['index'], gameData['player1']['pieces'][piece]['position'], gameData['player1']['pieces'][piece]['name'])
            board.player1.pieces.append(kamen)
            board.player1.pieces[int(piece)].history = gameData['player1']['pieces'][piece]['history']
            if kamen.position == 'BAR':
                board.player1.add_piece_to_bar(kamen)
                continue
            elif kamen.position == 'FINISH':
                board.player1.allFinishedPieces.push(kamen)
                continue
            else:
                board.spikes[kamen.position].push(board.player1.pieces[kamen.stone_index])
        
        for piece in gameData['player2']['pieces']:
            kamen = Stone(gameData['player2']['pieces'][piece]['player_number'], gameData['player2']['pieces'][piece]['index'], gameData['player2']['pieces'][piece]['position'], gameData['player2']['pieces'][piece]['name'])
            board.player2.pieces.append(kamen)
            board.player2.pieces[int(piece)].history = gameData['player2']['pieces'][piece]['history']
            if kamen.position == 'BAR':
                board.player2.add_piece_to_bar(kamen)
                continue
            elif kamen.position == 'FINISH':
                board.player2.allFinishedPieces.push(kamen)
                continue
            else:
                board.spikes[kamen.position].push(board.player2.pieces[kamen.stone_index])
        
        board.playerOnTurn = gameData['playerOnTurn']

    return board


#! Start of the game

if os.path.isfile('../assets/saveGame.json'):
    while True:
        continueGame = input(Fore.CYAN + 'Do you wish to load saved game? (yes/no): ' + Style.RESET_ALL)
        if continueGame == 'yes' or continueGame == 'no':
            if continueGame == 'yes':
                print(Fore.CYAN + 'Loading saved game...' + Style.RESET_ALL)
                board = loadGame()
                board.clear()
                board.display_board()
                break
            elif continueGame == 'no':
                player1_name = input(Fore.RED + 'Player 1 name: ' + Style.RESET_ALL)
                opponentType = input(Fore.CYAN +'Do you wish to play against AI? (yes/no): ' + Style.RESET_ALL)
                while True:
                    if opponentType == 'yes':
                        player2_name = 'AI'
                        break
                    elif opponentType == 'no':
                        player2_name = input(Fore.BLUE + 'Player 2 name: ' + Style.RESET_ALL)
                        break
                    else:
                        print(Fore.CYAN + 'Please enter yes or no!' + Style.RESET_ALL)
                        continue
                board = Board(Player(player1_name, 1), Player(player2_name, 2))
                break
else:
    player1_name = input(Fore.RED + 'Player 1 name: ' + Style.RESET_ALL)
    while True:
        opponentType = input(Fore.CYAN + 'Do you wish to play against AI? (yes/no): ' + Style.RESET_ALL)
        if opponentType == 'yes':
            player2_name = 'AI'
            break
        elif opponentType == 'no':
            player2_name = input(Fore.BLUE + 'Player 2 name: ' + Style.RESET_ALL)
            break
        else:
            print(Fore.CYAN + 'Please enter yes or no!' + Style.RESET_ALL)
            continue
    board = Board(Player(player1_name, 1), Player(player2_name, 2))
    


board.main()





# HRAC 1 == X
# HRAC 2 == O