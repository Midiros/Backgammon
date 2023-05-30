from stone import Stone
from stack import Stack

class Bar():
    def __init__(self):
        self.bar = Stack()

    def add_to_bar(self, stone) -> None:
            self.bar.push(stone)
    
    def pop_from_bar(self) -> Stone:
            return self.bar.pop()
        
    def __len__(self):
        return len(self.bar)