from stone import Stone
from stack import Stack

class Bar():
    def __init__(self):
        self.player1_bar = Stack()
        self.player2_bar = Stack()

    def add_to_bar(self, player_number, stone) -> None:
        if player_number == 1:
            self.player1_bar.push(stone)
        elif player_number == 2:
            self.player2_bar.push(stone)
        else:
            raise ValueError('Player number must be 1 or 2')
    
    def pop_from_bar(self, player_number) -> Stone:
        if player_number == 1:
            return self.player1_bar.pop()
        elif player_number == 2:
            return self.player2_bar.pop()
        else:
            raise ValueError('Player number must be 1 or 2')