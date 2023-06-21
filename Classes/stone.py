from stack import Stack
from colorama import Fore, Style

class Stone():
    def __init__(self, player_number,stone_index, position, player_name):
        if player_number not in [1, 2]:
            raise ValueError('Player number must be 1 or 2')
        elif stone_index not in range(15):
            raise ValueError('Stone index must be in range 0-14')

        self.player_number = player_number
        self.stone_index = stone_index
        self.position = position
        self.player_name = player_name
        self.history = []
        self.history.append(position) # Pri vytvoreni kamene, prida startovni pozici


    def owner(self) -> int:
        return self.player_number
    

    def player_name(self) -> str:
        return self.player_name

    def stone_index(self) -> int:
        return self.stone_index    

    def position(self) -> int:
        return self.position

    def history(self):
        return self.history

    def set_player_number(self, player_number) -> None:
        self.player_number = player_number

    def set_position(self, position) -> None:
        self.position = position
        self.add_to_history(position)

    def get_position(self) -> int:
        return self.position

    def add_to_history(self, position) -> None:
        self.history.append(position)

    def __str__(self):
        if self.position == 'BAR':
            return (Fore.LIGHTYELLOW_EX + 'Stone on bar owned by player: ' + str(self.player_name) + Style.RESET_ALL)
        else:
            return (Fore.LIGHTYELLOW_EX + 'Stone on spike: ' + str(self.position+1) + ' owned by player: ' + str(self.player_name) + Style.RESET_ALL)
    