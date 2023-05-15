from stack import Stack

class Stone():
    def __init__(self, player_number,stone_index, position):
        self.player_number = player_number
        self.stone_index = stone_index
        self.position = position
        self.history = Stack()
        self.history.push(position) # Pri vytvoreni kamene, prida startovni pozici

    def player_number(self):
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
        return (str(self.stone_index) + ' stone at position ' + str(self.position))
    

# sutr = Stone(1, 1, 1)

# print(sutr)
# sutr.set_position(2)
# sutr.set_position(4)
# sutr.set_position(2)
# print(sutr.history)

