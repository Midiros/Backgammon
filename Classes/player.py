from dice import Dice
from stone import Stone
from bar import Bar
from spike import Spike

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
        # self.pieces_out = []
        self.pieces = []
        self.bar = Bar()
        self.diceValues = []
        self.FinishedPieces = 0
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
                

    def move_piece(self, stone, move_position):
        # print(piece)
        stone.set_position(move_position)
        # print(piece.history)

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
    
    # def illegal_move(self, move, moves):
    #     while move < 0 or move > len(moves) - 1:
    #         print('Invalid input')
    #     return True


    def choose_move(self, moves):
        print(f'{self.diceValues}')
        print(f'You have {len(moves)} possible moves', end=' | ')
        # print(f'Available moves: {moves}')
        if self.player_number == 1:
            print(f'{moves}')
        else:
            print(f'{moves[::-1]}')

        while True:
            move = int(input('Choose your move: '))
            if move < 0 or move > len(moves) - 1:
                print('Invalid input')
                continue
            else:
                break
        return move




    def moveSetPlayer1(self, spikes, board):
        moves = []
        if self.diceValues == []:
            self.diceValues = self.roll_dice()
        currentDiceRolls = self.diceValues
        print(f'Current dice rolls: {currentDiceRolls}')
        while len(self.diceValues) > 0:
            moves = self.generateAllPossibleMovesPlayer1(spikes, currentDiceRolls)
            if moves == []:
                print('No possible moves')
                break
            move = self.choose_move(moves)

            print(f'Move a piece from spike : {moves[move][0]}')
            print(f'To spike : {moves[move][1]}')

            diceToUse = moves[move][1] - moves[move][0]
            print(f'With the dice of value : {diceToUse}')
            self.diceValues.remove(diceToUse)
            if moves[move][0] == 'BAR':
                pass
            board.movePiece(self.player_number,moves[move][0]-1, moves[move][1]-1)
            # if moves[move][1] > 24:
            #     self.FinishedPieces += 1
            #     barredOfPiece = spikes[moves[move][0]-1].peek()
                # self.pieces.remove(barredOfPiece)
                # print(f'Barred of piece: {barredOfPiece}')


            board.display_board()
        print('No more moves')
            # diceToUse = move[1] - move[0]
            

        
    def moveSetPlayer2(self, spikes, board):
        moves = []
        if self.diceValues == []:
            self.diceValues = self.roll_dice()
        currentDiceRolls = self.diceValues
        print(f'Current dice rolls: {currentDiceRolls}')
        while len(self.diceValues) > 0:
            moves = self.generateAllPossibleMovesPlayer2(spikes, currentDiceRolls)
            if moves == []:
                print('No possible moves')
                break
            move = self.choose_move(moves[::-1])
            print(f'Move a piece from spike : {moves[move][0]}')
            print(f'To spike : {moves[move][1]}')

            diceToUse = moves[move][0] - moves[move][1]
            print(f'With the dice of value : {diceToUse}')
            self.diceValues.remove(diceToUse)
            board.movePiece(self.player_number,moves[move][0]-1, moves[move][1]-1)
            # if moves[move][1] < 0:
            #     self.FinishedPieces += 1
            #     barredOfPiece = spikes[moves[move][0]-1].peek()
            #     # self.pieces.remove(barredOfPiece)
            #     print(f'Barred of piece: {barredOfPiece}')
            
            # print(f'pieces in the origin spike: {len(spikes[moves[move][0]-1])}')
            # print(f'pieces in the target spike: {len(spikes[moves[move][1]-1])}')
            # print(f'pieces in the origin spike: {len(spikes[moves[move][0]-1])}')
            # print(f'pieces in the target spike: {len(spikes[moves[move][1]-1])}')

            board.display_board()
        print('No more moves')
            # diceToUse = move[1] - move[0]
            








    def listStealableSpikes(self, allSpikes):
        stealableSpikes = []
        for spike in allSpikes:
            if spike.isStealable(self.player_number):
                stealableSpikes.append(spike.my_index())
                # print(spike.my_index())
        if len(stealableSpikes) < 0:
            print('No stealable spikes')
        
        
        # print(stealableSpikes)

        return stealableSpikes
    



    def myCurrentSpikes(self, allSpikes):
        spikesInControl = []
        for spike in allSpikes:
            if spike.peek() != None:
                if spike.peek().owner() == self.player_number:
                    spikesInControl.append(spike)
        if len(spikesInControl) < 0:
            print('No spikes in control')

        return spikesInControl








    def generateAllPossibleMovesPlayer1(self, allSpikes, currentDiceRolls):
        moves = []
        stealableSpikes = self.listStealableSpikes(allSpikes)
        spikesInControl = self.myCurrentSpikes(allSpikes)
        if self.bar:
            for dice in currentDiceRolls:
                moves.append(('BAR', -1 + dice))
            return moves

        for spike in spikesInControl:
            for dice in currentDiceRolls:
                if spike.my_index() + dice < 24:
                    if (spike.my_index() + dice) in stealableSpikes:
                        moves.append((spike.my_index() + 1, spike.my_index() + dice + 1))
                        # print('piece can move and steal')
                else:
                    if (spike.my_index() + dice > 23) in stealableSpikes:
                        if len(allSpikes[0:17]) == 0:
                        # print('piece can bare off')
                            moves.append((spike.my_index() + 1, spike.my_index() + dice + 1))
        return moves


    def generateAllPossibleMovesPlayer2(self, allSpikes, currentDiceRolls):
        moves = []
        stealableSpikes = self.listStealableSpikes(allSpikes)
        spikesInControl = self.myCurrentSpikes(allSpikes)
        if self.bar:
            for dice in currentDiceRolls:
                moves.append(('BAR', 24 - dice))
            return moves
        
        for spike in spikesInControl:
            for dice in currentDiceRolls:
                if spike.my_index() - dice >= 0:
                    if (spike.my_index() - dice) in stealableSpikes:
                        moves.append((spike.my_index() + 1, spike.my_index() - dice + 1))
                        # print('piece can move and steal')
                else:
                    if (spike.my_index() - dice < 0) in stealableSpikes:
                        if len(allSpikes[6:23]) == 0:
                            moves.append((spike.my_index() + 1, spike.my_index() - dice + 1))
                        # print('piece can bare off')

        return moves




