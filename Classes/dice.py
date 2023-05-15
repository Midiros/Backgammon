from random import randint


class Dice():
    def __init__(self, sides=6):
        self.sides = sides
        self.value = None
        self.roll()

    def roll(self):
        # roll the dice and generate a random value
        self.first_roll = randint(1, self.sides)
        self.second_roll = randint(1, self.sides)
        self.value = [self.first_roll, self.second_roll]
        # if the two rolls are equal, return the value 4 times instead of 2
        if self.first_roll == self.second_roll:
            self.value = [self.first_roll, self.first_roll, self.first_roll, self.first_roll]

        return self.value

    def whoStarts(self):
        self.first_roll = randint(1, self.sides)
        self.second_roll = randint(1, self.sides)
        self.value = [self.first_roll, self.second_roll]

        while self.first_roll == self.second_roll:
            self.first_roll = randint(1, self.sides)
            self.second_roll = randint(1, self.sides)
        if self.first_roll > self.second_roll:
            print('Player 1 starts')
            return (0, [self.first_roll, self.second_roll])
        else:
            print('Player 2 starts')
            return (1,[self.first_roll, self.second_roll])