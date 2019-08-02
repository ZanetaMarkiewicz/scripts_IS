import random


def roll():
    return random.choice(range(1, 6))


print(roll())