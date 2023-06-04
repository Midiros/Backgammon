import os
from dice import Dice
from stone import Stone
from bar import Bar
from spike import Spike
from colorama import Fore, Back, Style

class Player():
    def __init__(self, name, player_number):
        while player_number != 1 and player_number != 2:
            raise ValueError('Player number must be 1 or 2')
        self.name = name
        self.player_number = player_number
        self.dice = Dice()
        self.score = 0
        self.pieces = []
        self.bar = Bar()
        self.diceValues = []
        self.FinishedPieces = 0
    
    def clear(self):
        clear = os.system('cls' if os.name=='nt' else 'clear')

    def move_piece(self, stone, move_position):
        stone.set_position(move_position)

    def roll_dice(self):
        self.dice.roll()
        return self.dice.value
    
    def add_piece_to_bar(self, stone):
        self.bar.add_to_bar(stone)
        print(f'added {stone} to bar')
        stone.add_to_history(-1)
    
    def list_pieces(self):
        for piece in self.pieces:
            print(piece)
    
    def my_score(self):
        return self.score
    
    def my_pieces(self):
        return self.pieces
    
    def __str__(self):
        return self.name
    
#! Vraci index move, ktery se ma provest v listu moves
    def choose_move(self, moves):
        print(Fore.LIGHTCYAN_EX + f'You have {len(moves)} possible moves' + Style.RESET_ALL)
        if self.player_number == 1:
            print(Fore.YELLOW + f'{moves}'+ Style.RESET_ALL)
        else:
            print(Fore.YELLOW + f'{moves[::-1]}'+ Style.RESET_ALL)

        while True:
            move = int(input(Fore.LIGHTCYAN_EX + 'Choose your move: ' + Style.RESET_ALL))
            if move < 0 or move > len(moves):
                print('Invalid input')
                continue
            else:
                break
        self.clear()
        print(Fore.MAGENTA + '---------------------------------------------------------')
        return int(move - 1)


#! Vola funkci pro generovani vsech moznych tahu, da hraci na vyber a pak tah provede
    def moveSetPlayer1(self, spikes, board):
        moves = []
        if self.diceValues == []:
            self.diceValues = self.roll_dice()
        currentDiceRolls = self.diceValues
        print(Fore.LIGHTCYAN_EX + f'Current dice rolls: {currentDiceRolls}' + Style.RESET_ALL)
        while len(self.diceValues) > 0:
            moves = self.generateAllPossibleMovesPlayer1(spikes, currentDiceRolls)
            if moves == []:
                print('No possible moves')
                break
            move = self.choose_move(moves)

            print(Fore.MAGENTA + f'Moving a piece from spike : {moves[move][0]}' + Style.RESET_ALL)
            print(Fore.MAGENTA + f'To spike : {moves[move][1]}' + Style.RESET_ALL)

            if moves[move][0] == 'BAR':
                diceToUse = 0 + moves[move][1] # 0 is the bar
                piece = self.bar.pop_from_bar()
                board.spikes[moves[move][1]-1].push(piece)
            else:
                diceToUse = moves[move][1] - moves[move][0]
                board.movePiece(self.player_number,moves[move][0]-1, moves[move][1]-1)
            print(Fore.MAGENTA + f'With the dice of value : {diceToUse}' + Style.RESET_ALL)
            self.diceValues.remove(diceToUse)


            board.display_board()
        print(Fore.YELLOW + 'No more moves' + Style.RESET_ALL)
        while True:
            input(Fore.YELLOW + 'Press enter to continue' + Style.RESET_ALL)
            self.clear()
            break
            
        
#! Vola funkci pro generovani vsech moznych tahu, da hraci na vyber a pak tah provede
    def moveSetPlayer2(self, spikes, board):
        moves = []
        if self.diceValues == []:
            self.diceValues = self.roll_dice()
        currentDiceRolls = self.diceValues
        print(Fore.LIGHTCYAN_EX+ f'Current dice rolls: {currentDiceRolls}' + Style.RESET_ALL)
        while len(self.diceValues) > 0:
            moves = self.generateAllPossibleMovesPlayer2(spikes, currentDiceRolls)
            if moves == []:
                print('No possible moves')
                break
            move = self.choose_move(moves[::-1])
            print(Fore.MAGENTA + f'Moving a piece from spike : {moves[move][0]}' + Style.RESET_ALL)
            print(Fore.MAGENTA + f'To spike : {moves[move][1]}' + Style.RESET_ALL)

            if moves[move][0] == 'BAR':
                diceToUse = 25 - moves[move][1] # 25 is the bar
                piece = self.bar.pop_from_bar()
                board.spikes[moves[move][1]-1].push(piece)
            else:
                diceToUse = moves[move][0] - moves[move][1]
                board.movePiece(self.player_number,moves[move][0]-1, moves[move][1]-1)
            
            print(Fore.MAGENTA + f'With the dice of value : {diceToUse}' + Style.RESET_ALL)
            self.diceValues.remove(diceToUse)

            board.display_board()
        print(Fore.YELLOW + 'No more moves' + Style.RESET_ALL)
        while True:
            input(Fore.YELLOW + 'Press enter to continue' + Style.RESET_ALL)
            self.clear()
            break
            

#! Projede vsechny spikes a vrati ty, ktere jsou stealable > bud jsou prazdne nebo maji jen jeden kamen soupere
    def listStealableSpikes(self, allSpikes):
        stealableSpikes = []
        for spike in allSpikes:
            if spike.isStealable(self.player_number):
                stealableSpikes.append(spike.my_index())
        if len(stealableSpikes) < 0:
            print('No stealable spikes')
        
        return stealableSpikes
    
#! Projede vsechny spikes a vrati ty, ktere jsou vlastnene hracem > ma na nich svoje kaminky
    def myCurrentSpikes(self, allSpikes):
        spikesInControl = []
        for spike in allSpikes:
            if spike.peek() != None:
                if spike.peek().owner() == self.player_number:
                    spikesInControl.append(spike)
        if len(spikesInControl) < 0:
            print('No spikes in control')

        return spikesInControl
    
#! Bere vsechny spikes hrace, vsechny spikes na ktere se da pohnout a vsechny mozne hodnoty kostek a vraci list vsech moznych tahu
    def generateAllPossibleMovesPlayer1(self, allSpikes, currentDiceRolls):
        moves = []
        stealableSpikes = self.listStealableSpikes(allSpikes)
        spikesInControl = self.myCurrentSpikes(allSpikes)
        #!Pokud jsou nejake kaminky na baru, tak se musi nejdrive pohnout s nimi
        if self.bar:
            for dice in currentDiceRolls:
                for spike in stealableSpikes:
                    if (spike <= 0 + dice):
                        if (len(allSpikes[spike]) <= 1):
                            print('stealable spike')
                            moves.append(('BAR', 0 + dice))
            return moves

        #!TODO NOT FUNCTIONAL
        for spike in spikesInControl:
            for dice in currentDiceRolls:
                if spike.my_index() + dice < 24:
                    if (spike.my_index() + dice) in stealableSpikes:
                        moves.append((spike.my_index() + 1, spike.my_index() + dice + 1))
                        # print('piece can move and steal')
        return moves

#! Bere vsechny spikes hrace, vsechny spikes na ktere se da pohnout a vsechny mozne hodnoty kostek a vraci list vsech moznych tahu
    def generateAllPossibleMovesPlayer2(self, allSpikes, currentDiceRolls):
        moves = []
        stealableSpikes = self.listStealableSpikes(allSpikes)
        spikesInControl = self.myCurrentSpikes(allSpikes)
        #!Pokud jsou nejake kaminky na baru, tak se musi nejdrive pohnout s nimi
        if self.bar:
            for dice in currentDiceRolls:
                for spike in stealableSpikes:
                    if (spike >= 25 - dice):
                        if (len(allSpikes[spike]) <= 1):
                            print('stealable spike')
                            moves.append(('BAR', 25 - dice))
            return moves
        
        #!TODO NOT FUNCTIONAL
        for spike in spikesInControl:
            for dice in currentDiceRolls:
                if spike.my_index() - dice >= 0:
                    if (spike.my_index() - dice) in stealableSpikes:
                        moves.append((spike.my_index() + 1, spike.my_index() - dice + 1))
                        # print('piece can move and steal')
        return moves




