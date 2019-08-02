from D10_script import Character, Barbarian, Dice

player = Character(20)
enemy = Character()
barbarian = Barbarian()

for i in range(20):
    if player.character_state == "Dead":
        break
    enemy.attack(player)
    barbarian.attack(player)

print(barbarian)
print(f"health: {player.health} | strength: {player.strength} | damage: {player.damage} | armor: {player.armor}")
# else:
#     player.attack(enemy)
#     print(f"enemy health: {enemy.health} | enemy strength: {enemy.strength} | enemy damage: {enemy.damage} "
#           f"| enemy armor: {enemy.armor}")

