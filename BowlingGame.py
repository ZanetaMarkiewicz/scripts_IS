class BowlingGame():

    def __init__(self):
        self.rolls = []

    def roll(self, pins_striked):
        self.rolls.append(pins_striked)

    @property
    def score(self):
        final_score = 0
        roll_index = 0
        for i in range(10):
            if self.rolls[roll_index] + self.rolls[roll_index + 1] == 10:
                final_score += 10 + self.rolls[roll_index + 2]
                roll_index += 2
            else:
                final_score += self.rolls[roll_index] + self.rolls[roll_index + 1]
                roll_index += 2

        return final_score
