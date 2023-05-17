from stack import Stack

class Stone():
    def __init__(self, player_number,stone_index, position):
        if player_number not in [1, 2]:
            raise ValueError('Player number must be 1 or 2')
        elif stone_index not in range(15):
            raise ValueError('Stone index must be in range 0-14')
        elif position not in range(0,24):
            raise ValueError('Position must be in range 0-23')

        self.player_number = player_number
        self.stone_index = stone_index
        self.position = position
        self.history = Stack()
        self.history.push(position) # Pri vytvoreni kamene, prida startovni pozici


    def owner(self) -> int:
        return self.player_number
    


    def stone_index(self) -> int:
        return self.stone_index    

    def position(self) -> int:
        return self.position

    def history(self) -> list[int]:
        return self.history

    def set_player_number(self, player_number) -> None:
        self.player_number = player_number

    def set_position(self, position) -> None:
        self.position = position
        self.add_to_history(position)

    def get_position(self) -> int:
        return self.position

    def add_to_history(self, position) -> None:
        self.history.push(position)

    def __str__(self):
        return (str(self.stone_index) + ' stone at position ' + str(self.position) + ' belongs to player' + str(self.player_number))
    

# sutr = Stone(2, 6, 0)

# print(sutr)
# sutr.set_position(2)
# sutr.set_position(4)
# sutr.set_position(2)
# print(sutr.history)

