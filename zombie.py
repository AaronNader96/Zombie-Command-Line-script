import random

class Human:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f'{self.name} has died.')

class Zombie:
    def __init__(self, name):
        self.name = name
        self.health = 50

    def attack(self, human):
        damage = random.randint(10, 20)
        human.take_damage(damage)
        print(f'{self.name} attacked {human.name} for {damage} damage.')

# Initialize some humans and zombies
humans = [Human('Alice'), Human('Bob'), Human('Charlie')]
zombies = [Zombie('Zombie 1'), Zombie('Zombie 2')]

# Game loop
while len(humans) > 0 and len(zombies) > 0:
    # Zombies attack a random human
    for zombie in zombies:
        human = random.choice(humans)
        zombie.attack(human)
        if human.health <= 0:
            humans.remove(human)

if len(humans) == 0:
    print('All humans have died. Zombies win!')
else:
    print('All zombies have been killed. Humans win!')
