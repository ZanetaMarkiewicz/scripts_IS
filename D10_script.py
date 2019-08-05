import random


class Dice(object):
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.choice(range(1, self.sides + 1))


# simple_dice = Dice()
#
# print(f"Rolled with number: {simple_dice.roll()}")


class Character(object):
    def __init__(self, health=10, strength=5, damage=2, armor=5):
        self.health = health
        self.strength = strength
        self.damage = damage
        self.armor = armor
        self.character_state = "Alive"

    def __str__(self):
        return f"I'm so kind of game character."

    def attack(self, target_character):
        target_character.defend(self.damage)

    def defend(self, damage):
        dice_to_defend = Dice()
        if dice_to_defend.roll() > 3:
            # damage = 0
            return

        damage_to_health = max(damage - self.armor, 0)
        self.armor = max(self.armor - damage, 0)
        self.health = max(self.health - damage_to_health, 0)
        if self.health == 0:
            print("Character has died...")
            self.character_state = "Dead"


class Barbarian(Character):
    def __init__(self, anger=1):
        super().__init__()
        self.anger = anger

    def attack(self, target_character):
        print(f"This is method from {self.__class__.__name__}")
        target_character.defend(self.damage + self.anger)